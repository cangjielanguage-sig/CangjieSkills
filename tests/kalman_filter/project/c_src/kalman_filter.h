#ifndef KALMAN_FILTER_H
#define KALMAN_FILTER_H

#include <stdint.h>

/**
 * Opaque Kalman filter handle.
 * state_dim: dimension of the state vector (n)
 * meas_dim: dimension of the measurement vector (m)
 *
 * Internal matrices (row-major storage):
 *   x: n x 1  state estimate
 *   P: n x n  error covariance
 *   F: n x n  state transition matrix
 *   H: m x n  observation matrix
 *   Q: n x n  process noise covariance
 *   R: m x m  measurement noise covariance
 *   K: n x m  Kalman gain (from last update)
 */
typedef struct KalmanFilter KalmanFilter;

/**
 * Create a Kalman filter with given state and measurement dimensions.
 * All internal matrices are initialized to zero.
 * Returns NULL on allocation failure.
 */
KalmanFilter* kf_create(int32_t state_dim, int32_t meas_dim);

/**
 * Destroy a Kalman filter and free all associated memory.
 */
void kf_destroy(KalmanFilter* kf);

/**
 * Set the state transition matrix F (row-major, n x n).
 */
void kf_set_transition(KalmanFilter* kf, const double* F);

/**
 * Set the observation matrix H (row-major, m x n).
 */
void kf_set_observation(KalmanFilter* kf, const double* H);

/**
 * Set the process noise covariance Q (row-major, n x n).
 */
void kf_set_process_noise(KalmanFilter* kf, const double* Q);

/**
 * Set the measurement noise covariance R (row-major, m x m).
 */
void kf_set_measurement_noise(KalmanFilter* kf, const double* R);

/**
 * Set the state vector x (n x 1).
 */
void kf_set_state(KalmanFilter* kf, const double* x);

/**
 * Set the error covariance matrix P (row-major, n x n).
 */
void kf_set_covariance(KalmanFilter* kf, const double* P);

/**
 * Perform the prediction step:
 *   x = F * x
 *   P = F * P * F^T + Q
 */
void kf_predict(KalmanFilter* kf);

/**
 * Perform the update step with measurement z (m x 1):
 *   y = z - H * x          (innovation)
 *   S = H * P * H^T + R    (innovation covariance)
 *   K = P * H^T * S^{-1}   (Kalman gain)
 *   x = x + K * y
 *   P = (I - K * H) * P
 */
void kf_update(KalmanFilter* kf, const double* z);

/**
 * Get the current state estimate x (output: n x 1).
 */
void kf_get_state(const KalmanFilter* kf, double* x_out);

/**
 * Get the current error covariance P (output: row-major, n x n).
 */
void kf_get_covariance(const KalmanFilter* kf, double* P_out);

/**
 * Get the Kalman gain from the last update (output: row-major, n x m).
 */
void kf_get_gain(const KalmanFilter* kf, double* K_out);

/**
 * Get the state dimension.
 */
int32_t kf_get_state_dim(const KalmanFilter* kf);

/**
 * Get the measurement dimension.
 */
int32_t kf_get_meas_dim(const KalmanFilter* kf);

#endif /* KALMAN_FILTER_H */
