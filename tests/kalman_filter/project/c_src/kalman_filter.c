#include "kalman_filter.h"
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct KalmanFilter {
    int32_t n;  /* state dimension */
    int32_t m;  /* measurement dimension */
    double* x;  /* n x 1: state */
    double* P;  /* n x n: covariance */
    double* F;  /* n x n: transition */
    double* H;  /* m x n: observation */
    double* Q;  /* n x n: process noise */
    double* R;  /* m x m: measurement noise */
    double* K;  /* n x m: Kalman gain */
    /* temporary work buffers */
    double* tmp_nn;   /* n x n */
    double* tmp_nn2;  /* n x n */
    double* tmp_mn;   /* m x n */
    double* tmp_mm;   /* m x m */
    double* tmp_nm;   /* n x m */
    double* tmp_n;    /* n x 1 */
    double* tmp_m;    /* m x 1 */
};

/* ---- Matrix helpers (row-major) ---- */

/* C = A * B, where A is (r x k), B is (k x c), C is (r x c) */
static void mat_mul(const double* A, const double* B, double* C,
                    int r, int k, int c)
{
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            double sum = 0.0;
            for (int p = 0; p < k; p++) {
                sum += A[i * k + p] * B[p * c + j];
            }
            C[i * c + j] = sum;
        }
    }
}

/* C = A * B^T, where A is (r x k), B is (c x k), C is (r x c) */
static void mat_mul_bt(const double* A, const double* B, double* C,
                       int r, int k, int c)
{
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            double sum = 0.0;
            for (int p = 0; p < k; p++) {
                sum += A[i * k + p] * B[j * k + p];
            }
            C[i * c + j] = sum;
        }
    }
}

/* C = A + B (element-wise), size = r x c */
static void mat_add(const double* A, const double* B, double* C, int r, int c)
{
    int total = r * c;
    for (int i = 0; i < total; i++) {
        C[i] = A[i] + B[i];
    }
}

/* C = A - B (element-wise), size = r x c */
static void mat_sub(const double* A, const double* B, double* C, int r, int c)
{
    int total = r * c;
    for (int i = 0; i < total; i++) {
        C[i] = A[i] - B[i];
    }
}

/* dst = src, size elements */
static void mat_copy(double* dst, const double* src, int size)
{
    memcpy(dst, src, (size_t)size * sizeof(double));
}

/* Set matrix to identity, size = n x n */
static void mat_identity(double* A, int n)
{
    memset(A, 0, (size_t)(n * n) * sizeof(double));
    for (int i = 0; i < n; i++) {
        A[i * n + i] = 1.0;
    }
}

/* In-place inversion of a small matrix (m x m) using Gauss-Jordan.
 * Returns 0 on success, -1 if singular.
 * Uses 'work' buffer of size m x 2m. */
static int mat_invert(double* A, int m, double* work)
{
    /* Build augmented matrix [A | I] in work (m x 2m) */
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            work[i * 2 * m + j] = A[i * m + j];
        }
        for (int j = 0; j < m; j++) {
            work[i * 2 * m + m + j] = (i == j) ? 1.0 : 0.0;
        }
    }

    /* Forward elimination with partial pivoting */
    for (int col = 0; col < m; col++) {
        /* Find pivot */
        int pivot = col;
        double max_val = fabs(work[col * 2 * m + col]);
        for (int row = col + 1; row < m; row++) {
            double val = fabs(work[row * 2 * m + col]);
            if (val > max_val) {
                max_val = val;
                pivot = row;
            }
        }
        if (max_val < 1e-15) return -1; /* singular */

        /* Swap rows */
        if (pivot != col) {
            for (int j = 0; j < 2 * m; j++) {
                double tmp = work[col * 2 * m + j];
                work[col * 2 * m + j] = work[pivot * 2 * m + j];
                work[pivot * 2 * m + j] = tmp;
            }
        }

        /* Scale pivot row */
        double diag = work[col * 2 * m + col];
        for (int j = 0; j < 2 * m; j++) {
            work[col * 2 * m + j] /= diag;
        }

        /* Eliminate column */
        for (int row = 0; row < m; row++) {
            if (row == col) continue;
            double factor = work[row * 2 * m + col];
            for (int j = 0; j < 2 * m; j++) {
                work[row * 2 * m + j] -= factor * work[col * 2 * m + j];
            }
        }
    }

    /* Extract inverse from right half */
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            A[i * m + j] = work[i * 2 * m + m + j];
        }
    }
    return 0;
}

/* ---- Kalman filter API ---- */

KalmanFilter* kf_create(int32_t state_dim, int32_t meas_dim)
{
    if (state_dim <= 0 || meas_dim <= 0) return NULL;

    KalmanFilter* kf = (KalmanFilter*)calloc(1, sizeof(KalmanFilter));
    if (!kf) return NULL;

    int n = state_dim;
    int m = meas_dim;
    kf->n = n;
    kf->m = m;

    /* Allocate all matrices */
    kf->x = (double*)calloc((size_t)(n), sizeof(double));
    kf->P = (double*)calloc((size_t)(n * n), sizeof(double));
    kf->F = (double*)calloc((size_t)(n * n), sizeof(double));
    kf->H = (double*)calloc((size_t)(m * n), sizeof(double));
    kf->Q = (double*)calloc((size_t)(n * n), sizeof(double));
    kf->R = (double*)calloc((size_t)(m * m), sizeof(double));
    kf->K = (double*)calloc((size_t)(n * m), sizeof(double));

    /* Work buffers */
    kf->tmp_nn  = (double*)calloc((size_t)(n * n), sizeof(double));
    kf->tmp_nn2 = (double*)calloc((size_t)(n * n), sizeof(double));
    kf->tmp_mn  = (double*)calloc((size_t)(m * n), sizeof(double));
    kf->tmp_mm  = (double*)calloc((size_t)(m * m), sizeof(double));
    kf->tmp_nm  = (double*)calloc((size_t)(n * m), sizeof(double));
    kf->tmp_n   = (double*)calloc((size_t)(n), sizeof(double));
    kf->tmp_m   = (double*)calloc((size_t)(m), sizeof(double));

    /* Check allocations */
    if (!kf->x || !kf->P || !kf->F || !kf->H || !kf->Q || !kf->R || !kf->K ||
        !kf->tmp_nn || !kf->tmp_nn2 || !kf->tmp_mn || !kf->tmp_mm ||
        !kf->tmp_nm || !kf->tmp_n || !kf->tmp_m) {
        kf_destroy(kf);
        return NULL;
    }

    /* Initialize F to identity */
    mat_identity(kf->F, n);
    /* Initialize P to identity */
    mat_identity(kf->P, n);

    return kf;
}

void kf_destroy(KalmanFilter* kf)
{
    if (!kf) return;
    free(kf->x);
    free(kf->P);
    free(kf->F);
    free(kf->H);
    free(kf->Q);
    free(kf->R);
    free(kf->K);
    free(kf->tmp_nn);
    free(kf->tmp_nn2);
    free(kf->tmp_mn);
    free(kf->tmp_mm);
    free(kf->tmp_nm);
    free(kf->tmp_n);
    free(kf->tmp_m);
    free(kf);
}

void kf_set_transition(KalmanFilter* kf, const double* F)
{
    if (kf && F) mat_copy(kf->F, F, kf->n * kf->n);
}

void kf_set_observation(KalmanFilter* kf, const double* H)
{
    if (kf && H) mat_copy(kf->H, H, kf->m * kf->n);
}

void kf_set_process_noise(KalmanFilter* kf, const double* Q)
{
    if (kf && Q) mat_copy(kf->Q, Q, kf->n * kf->n);
}

void kf_set_measurement_noise(KalmanFilter* kf, const double* R)
{
    if (kf && R) mat_copy(kf->R, R, kf->m * kf->m);
}

void kf_set_state(KalmanFilter* kf, const double* x)
{
    if (kf && x) mat_copy(kf->x, x, kf->n);
}

void kf_set_covariance(KalmanFilter* kf, const double* P)
{
    if (kf && P) mat_copy(kf->P, P, kf->n * kf->n);
}

void kf_predict(KalmanFilter* kf)
{
    if (!kf) return;
    int n = kf->n;

    /* x = F * x */
    mat_mul(kf->F, kf->x, kf->tmp_n, n, n, 1);
    mat_copy(kf->x, kf->tmp_n, n);

    /* P = F * P * F^T + Q */
    mat_mul(kf->F, kf->P, kf->tmp_nn, n, n, n);   /* tmp_nn = F * P */
    mat_mul_bt(kf->tmp_nn, kf->F, kf->tmp_nn2, n, n, n); /* tmp_nn2 = (F*P) * F^T */
    mat_add(kf->tmp_nn2, kf->Q, kf->P, n, n);      /* P = F*P*F^T + Q */
}

void kf_update(KalmanFilter* kf, const double* z)
{
    if (!kf || !z) return;
    int n = kf->n;
    int m = kf->m;

    /* y = z - H * x */
    mat_mul(kf->H, kf->x, kf->tmp_m, m, n, 1);     /* tmp_m = H * x */
    mat_sub(z, kf->tmp_m, kf->tmp_m, m, 1);         /* tmp_m = z - H*x = y */

    /* S = H * P * H^T + R */
    mat_mul(kf->H, kf->P, kf->tmp_mn, m, n, n);     /* tmp_mn = H * P */
    mat_mul_bt(kf->tmp_mn, kf->H, kf->tmp_mm, m, n, m); /* tmp_mm = H*P*H^T */
    mat_add(kf->tmp_mm, kf->R, kf->tmp_mm, m, m);   /* tmp_mm = S = H*P*H^T + R */

    /* K = P * H^T * S^{-1} */
    /* First compute P * H^T -> tmp_nm (n x m) */
    mat_mul_bt(kf->P, kf->H, kf->tmp_nm, n, n, m);  /* tmp_nm = P * H^T */

    /* Invert S in-place: tmp_mm = S^{-1} */
    /* Need work buffer of size m x 2m - reuse tmp_mn which is m x n, 
       but we need m x 2m. Allocate on stack for small m, or use a separate buffer.
       For simplicity, allocate temporarily. */
    {
        double* inv_work = (double*)malloc((size_t)(m * 2 * m) * sizeof(double));
        if (inv_work) {
            mat_invert(kf->tmp_mm, m, inv_work);  /* tmp_mm = S^{-1} */
            free(inv_work);
        }
    }

    /* K = (P * H^T) * S^{-1} = tmp_nm * tmp_mm */
    mat_mul(kf->tmp_nm, kf->tmp_mm, kf->K, n, m, m); /* K = P*H^T*S^{-1} */

    /* x = x + K * y */
    mat_mul(kf->K, kf->tmp_m, kf->tmp_n, n, m, 1);  /* tmp_n = K * y */
    mat_add(kf->x, kf->tmp_n, kf->x, n, 1);          /* x = x + K*y */

    /* P = (I - K * H) * P */
    mat_mul(kf->K, kf->H, kf->tmp_nn, n, m, n);      /* tmp_nn = K * H */
    mat_identity(kf->tmp_nn2, n);                       /* tmp_nn2 = I */
    mat_sub(kf->tmp_nn2, kf->tmp_nn, kf->tmp_nn, n, n); /* tmp_nn = I - K*H */
    mat_mul(kf->tmp_nn, kf->P, kf->tmp_nn2, n, n, n);   /* tmp_nn2 = (I-K*H)*P */
    mat_copy(kf->P, kf->tmp_nn2, n * n);                 /* P = (I-K*H)*P */
}

void kf_get_state(const KalmanFilter* kf, double* x_out)
{
    if (kf && x_out) mat_copy(x_out, kf->x, kf->n);
}

void kf_get_covariance(const KalmanFilter* kf, double* P_out)
{
    if (kf && P_out) mat_copy(P_out, kf->P, kf->n * kf->n);
}

void kf_get_gain(const KalmanFilter* kf, double* K_out)
{
    if (kf && K_out) mat_copy(K_out, kf->K, kf->n * kf->m);
}

int32_t kf_get_state_dim(const KalmanFilter* kf)
{
    return kf ? kf->n : 0;
}

int32_t kf_get_meas_dim(const KalmanFilter* kf)
{
    return kf ? kf->m : 0;
}
