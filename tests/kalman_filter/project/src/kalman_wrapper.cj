package kalman

/**
 * Exception type for Kalman filter operations.
 */
public class KalmanException <: Exception {
    public init(message: String) {
        super(message)
    }
}

/**
 * Safe Cangjie wrapper around the C Kalman filter library.
 * Manages the lifecycle of the C filter handle and provides
 * a convenient API using Array<Float64>.
 *
 * Usage:
 *   let kf = KalmanFilter(4, 2)
 *   kf.setTransition(F)
 *   kf.setObservation(H)
 *   kf.setProcessNoise(Q)
 *   kf.setMeasurementNoise(R)
 *   kf.setState(x0)
 *   kf.setCovariance(P0)
 *   kf.predict()
 *   kf.update(measurement)
 *   let state = kf.getState()
 */
public class KalmanFilter {
    private let handle: CPointer<Unit>
    private let _stateDim: Int64
    private let _measDim: Int64
    private var _destroyed: Bool = false

    /**
     * Create a Kalman filter with given state and measurement dimensions.
     * @param stateDim state vector dimension (must be > 0)
     * @param measDim measurement vector dimension (must be > 0)
     * @throws KalmanException if creation fails
     */
    public init(stateDim: Int64, measDim: Int64) {
        if (stateDim <= 0 || measDim <= 0) {
            throw KalmanException("Dimensions must be positive: stateDim=${stateDim}, measDim=${measDim}")
        }
        _stateDim = stateDim
        _measDim = measDim
        handle = unsafe { kf_create(Int32(stateDim), Int32(measDim)) }
        if (handle.isNull()) {
            throw KalmanException("Failed to create Kalman filter")
        }
    }

    /**
     * Destroy the filter and release C memory.
     * Safe to call multiple times.
     */
    public func destroy(): Unit {
        if (!_destroyed) {
            unsafe { kf_destroy(handle) }
            _destroyed = true
        }
    }

    /** State vector dimension */
    public prop stateDim: Int64 {
        get() { _stateDim }
    }

    /** Measurement vector dimension */
    public prop measDim: Int64 {
        get() { _measDim }
    }

    private func checkNotDestroyed(): Unit {
        if (_destroyed) {
            throw KalmanException("Filter has been destroyed")
        }
    }

    /**
     * Set the state transition matrix F (row-major, stateDim x stateDim).
     */
    public func setTransition(F: Array<Float64>): Unit {
        checkNotDestroyed()
        if (F.size != _stateDim * _stateDim) {
            throw KalmanException("F size mismatch: expected ${_stateDim * _stateDim}, got ${F.size}")
        }
        unsafe {
            let h = acquireArrayRawData(F)
            kf_set_transition(handle, h.pointer)
            releaseArrayRawData(h)
        }
    }

    /**
     * Set the observation matrix H (row-major, measDim x stateDim).
     */
    public func setObservation(H: Array<Float64>): Unit {
        checkNotDestroyed()
        if (H.size != _measDim * _stateDim) {
            throw KalmanException("H size mismatch: expected ${_measDim * _stateDim}, got ${H.size}")
        }
        unsafe {
            let h = acquireArrayRawData(H)
            kf_set_observation(handle, h.pointer)
            releaseArrayRawData(h)
        }
    }

    /**
     * Set the process noise covariance Q (row-major, stateDim x stateDim).
     */
    public func setProcessNoise(Q: Array<Float64>): Unit {
        checkNotDestroyed()
        if (Q.size != _stateDim * _stateDim) {
            throw KalmanException("Q size mismatch: expected ${_stateDim * _stateDim}, got ${Q.size}")
        }
        unsafe {
            let h = acquireArrayRawData(Q)
            kf_set_process_noise(handle, h.pointer)
            releaseArrayRawData(h)
        }
    }

    /**
     * Set the measurement noise covariance R (row-major, measDim x measDim).
     */
    public func setMeasurementNoise(R: Array<Float64>): Unit {
        checkNotDestroyed()
        if (R.size != _measDim * _measDim) {
            throw KalmanException("R size mismatch: expected ${_measDim * _measDim}, got ${R.size}")
        }
        unsafe {
            let h = acquireArrayRawData(R)
            kf_set_measurement_noise(handle, h.pointer)
            releaseArrayRawData(h)
        }
    }

    /**
     * Set the state vector x (stateDim x 1).
     */
    public func setState(x: Array<Float64>): Unit {
        checkNotDestroyed()
        if (x.size != _stateDim) {
            throw KalmanException("State size mismatch: expected ${_stateDim}, got ${x.size}")
        }
        unsafe {
            let h = acquireArrayRawData(x)
            kf_set_state(handle, h.pointer)
            releaseArrayRawData(h)
        }
    }

    /**
     * Set the error covariance matrix P (row-major, stateDim x stateDim).
     */
    public func setCovariance(P: Array<Float64>): Unit {
        checkNotDestroyed()
        if (P.size != _stateDim * _stateDim) {
            throw KalmanException("P size mismatch: expected ${_stateDim * _stateDim}, got ${P.size}")
        }
        unsafe {
            let h = acquireArrayRawData(P)
            kf_set_covariance(handle, h.pointer)
            releaseArrayRawData(h)
        }
    }

    /**
     * Perform the prediction step.
     */
    public func predict(): Unit {
        checkNotDestroyed()
        unsafe { kf_predict(handle) }
    }

    /**
     * Perform the update step with measurement z.
     * @param z measurement vector (measDim x 1)
     */
    public func update(z: Array<Float64>): Unit {
        checkNotDestroyed()
        if (z.size != _measDim) {
            throw KalmanException("Measurement size mismatch: expected ${_measDim}, got ${z.size}")
        }
        unsafe {
            let h = acquireArrayRawData(z)
            kf_update(handle, h.pointer)
            releaseArrayRawData(h)
        }
    }

    /**
     * Get the current state estimate.
     * @return state vector (stateDim x 1)
     */
    public func getState(): Array<Float64> {
        checkNotDestroyed()
        let result = Array<Float64>(_stateDim, repeat: 0.0)
        unsafe {
            let h = acquireArrayRawData(result)
            kf_get_state(handle, h.pointer)
            releaseArrayRawData(h)
        }
        return result
    }

    /**
     * Get the current error covariance.
     * @return covariance matrix (row-major, stateDim x stateDim)
     */
    public func getCovariance(): Array<Float64> {
        checkNotDestroyed()
        let result = Array<Float64>(_stateDim * _stateDim, repeat: 0.0)
        unsafe {
            let h = acquireArrayRawData(result)
            kf_get_covariance(handle, h.pointer)
            releaseArrayRawData(h)
        }
        return result
    }

    /**
     * Get the Kalman gain from the last update.
     * @return Kalman gain matrix (row-major, stateDim x measDim)
     */
    public func getGain(): Array<Float64> {
        checkNotDestroyed()
        let result = Array<Float64>(_stateDim * _measDim, repeat: 0.0)
        unsafe {
            let h = acquireArrayRawData(result)
            kf_get_gain(handle, h.pointer)
            releaseArrayRawData(h)
        }
        return result
    }
}
