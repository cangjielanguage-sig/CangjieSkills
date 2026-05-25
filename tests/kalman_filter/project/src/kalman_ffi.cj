package kalman

/**
 * FFI declarations for the C Kalman filter library.
 * All functions require unsafe context to call.
 */
foreign {
    func kf_create(state_dim: Int32, meas_dim: Int32): CPointer<Unit>
    func kf_destroy(kf: CPointer<Unit>): Unit
    func kf_set_transition(kf: CPointer<Unit>, F: CPointer<Float64>): Unit
    func kf_set_observation(kf: CPointer<Unit>, H: CPointer<Float64>): Unit
    func kf_set_process_noise(kf: CPointer<Unit>, Q: CPointer<Float64>): Unit
    func kf_set_measurement_noise(kf: CPointer<Unit>, R: CPointer<Float64>): Unit
    func kf_set_state(kf: CPointer<Unit>, x: CPointer<Float64>): Unit
    func kf_set_covariance(kf: CPointer<Unit>, P: CPointer<Float64>): Unit
    func kf_predict(kf: CPointer<Unit>): Unit
    func kf_update(kf: CPointer<Unit>, z: CPointer<Float64>): Unit
    func kf_get_state(kf: CPointer<Unit>, x_out: CPointer<Float64>): Unit
    func kf_get_covariance(kf: CPointer<Unit>, P_out: CPointer<Float64>): Unit
    func kf_get_gain(kf: CPointer<Unit>, K_out: CPointer<Float64>): Unit
    func kf_get_state_dim(kf: CPointer<Unit>): Int32
    func kf_get_meas_dim(kf: CPointer<Unit>): Int32
}
