package kalman

import std.math.*
import std.collection.*

let KF_PI = 3.14159265358979323846

/**
 * Represents a 2D position.
 */
public struct Position {
    public var x: Float64
    public var y: Float64

    public init(x: Float64, y: Float64) {
        this.x = x
        this.y = y
    }
}

/**
 * Represents a 2D target state (position + velocity).
 */
public struct TargetState {
    public var px: Float64  // position x
    public var py: Float64  // position y
    public var vx: Float64  // velocity x
    public var vy: Float64  // velocity y

    public init(px: Float64, py: Float64, vx: Float64, vy: Float64) {
        this.px = px
        this.py = py
        this.vx = vx
        this.vy = vy
    }
}

/**
 * Result of a single tracking step.
 */
public struct TrackingStep {
    public let time: Float64
    public let trueState: TargetState
    public let measurement: Position
    public let estimated: TargetState
    public let positionError: Float64

    public init(time: Float64, trueState: TargetState, measurement: Position,
                estimated: TargetState, positionError: Float64) {
        this.time = time
        this.trueState = trueState
        this.measurement = measurement
        this.estimated = estimated
        this.positionError = positionError
    }
}

/**
 * A simple linear congruential random number generator for deterministic simulation.
 * Uses xorshift64 algorithm for pseudo-random generation and Box-Muller transform
 * for Gaussian distribution.
 */
public class SimpleRandom {
    private var state: UInt64

    public init(seed: UInt64) {
        state = if (seed == 0) { 1 } else { seed }
    }

    /** Generate next uniform random number in [0, 1) using xorshift64 */
    public func nextUniform(): Float64 {
        state = state ^ (state << 13)
        state = state ^ (state >> 7)
        state = state ^ (state << 17)
        return Float64(state % 1000000000) / 1000000000.0
    }

    /** Generate next Gaussian (normal) random number with mean 0 and std 1 */
    public func nextGaussian(): Float64 {
        var u1 = nextUniform()
        while (u1 < 1.0e-10) {
            u1 = nextUniform()
        }
        let u2 = nextUniform()
        return sqrt(-2.0 * log(u1)) * cos(2.0 * KF_PI * u2)
    }

    /** Generate Gaussian with specified mean and standard deviation */
    public func nextGaussian(mean: Float64, std: Float64): Float64 {
        return mean + std * nextGaussian()
    }
}

/**
 * 2D target tracking simulator using Kalman filter.
 *
 * Models a target moving in 2D with constant velocity model.
 * State vector: [px, py, vx, vy] (position and velocity)
 * Measurement: [px, py] (position only, with noise)
 *
 * The simulation generates ground truth trajectory, adds measurement noise,
 * and uses the Kalman filter to estimate the target state.
 */
public class TargetTracker {
    private let dt: Float64
    private let processNoise: Float64
    private let measurementNoise: Float64
    private let kf: KalmanFilter

    /**
     * Create a target tracker.
     * @param dt time step (seconds)
     * @param processNoise process noise standard deviation (acceleration noise)
     * @param measurementNoise measurement noise standard deviation (position noise)
     */
    public init(dt: Float64, processNoise: Float64, measurementNoise: Float64) {
        this.dt = dt
        this.processNoise = processNoise
        this.measurementNoise = measurementNoise

        // State: [px, py, vx, vy], Measurement: [px, py]
        kf = KalmanFilter(4, 2)

        // State transition matrix F (constant velocity model):
        // px' = px + vx*dt
        // py' = py + vy*dt
        // vx' = vx
        // vy' = vy
        let F: Array<Float64> = [
            1.0, 0.0, dt,  0.0,
            0.0, 1.0, 0.0, dt,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
        ]
        kf.setTransition(F)

        // Observation matrix H (observe position only):
        let H: Array<Float64> = [
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0
        ]
        kf.setObservation(H)

        // Process noise covariance Q (based on constant velocity + acceleration noise)
        let q = processNoise * processNoise
        let dt2 = dt * dt
        let dt3 = dt2 * dt
        let dt4 = dt3 * dt
        let Q: Array<Float64> = [
            dt4 / 4.0 * q, 0.0,            dt3 / 2.0 * q, 0.0,
            0.0,            dt4 / 4.0 * q, 0.0,            dt3 / 2.0 * q,
            dt3 / 2.0 * q, 0.0,            dt2 * q,        0.0,
            0.0,            dt3 / 2.0 * q, 0.0,            dt2 * q
        ]
        kf.setProcessNoise(Q)

        // Measurement noise covariance R
        let r = measurementNoise * measurementNoise
        let R: Array<Float64> = [
            r,   0.0,
            0.0, r
        ]
        kf.setMeasurementNoise(R)
    }

    /**
     * Initialize the tracker with an initial state estimate and uncertainty.
     * @param initialState initial state estimate [px, py, vx, vy]
     * @param posUncertainty initial position uncertainty
     * @param velUncertainty initial velocity uncertainty
     */
    public func initialize(initialState: TargetState, posUncertainty: Float64,
                          velUncertainty: Float64): Unit {
        let x0: Array<Float64> = [initialState.px, initialState.py,
                                   initialState.vx, initialState.vy]
        kf.setState(x0)

        let pu2 = posUncertainty * posUncertainty
        let vu2 = velUncertainty * velUncertainty
        let P0: Array<Float64> = [
            pu2, 0.0, 0.0, 0.0,
            0.0, pu2, 0.0, 0.0,
            0.0, 0.0, vu2, 0.0,
            0.0, 0.0, 0.0, vu2
        ]
        kf.setCovariance(P0)
    }

    /**
     * Run a complete tracking simulation.
     * @param trueInitial true initial state of the target
     * @param steps number of simulation steps
     * @param seed random seed for reproducibility
     * @return list of tracking results for each step
     */
    public func simulate(trueInitial: TargetState, steps: Int64,
                         seed: UInt64): ArrayList<TrackingStep> {
        let rng = SimpleRandom(seed)
        let results = ArrayList<TrackingStep>()

        var trueState = trueInitial

        for (i in 0..steps) {
            let time = Float64(i + 1) * dt

            // True state propagation (constant velocity + process noise)
            let ax = processNoise * rng.nextGaussian()
            let ay = processNoise * rng.nextGaussian()
            trueState = TargetState(
                trueState.px + trueState.vx * dt + 0.5 * ax * dt * dt,
                trueState.py + trueState.vy * dt + 0.5 * ay * dt * dt,
                trueState.vx + ax * dt,
                trueState.vy + ay * dt
            )

            // Generate noisy measurement
            let measX = trueState.px + measurementNoise * rng.nextGaussian()
            let measY = trueState.py + measurementNoise * rng.nextGaussian()
            let measurement = Position(measX, measY)

            // Kalman filter predict + update
            kf.predict()
            kf.update([measX, measY])

            // Get estimated state
            let state = kf.getState()
            let estimated = TargetState(state[0], state[1], state[2], state[3])

            // Compute position error
            let errX = estimated.px - trueState.px
            let errY = estimated.py - trueState.py
            let posError = sqrt(errX * errX + errY * errY)

            results.add(TrackingStep(time, trueState, measurement, estimated, posError))
        }

        return results
    }

    /** Get the current Kalman filter state estimate */
    public func getState(): Array<Float64> {
        return kf.getState()
    }

    /** Get the current error covariance */
    public func getCovariance(): Array<Float64> {
        return kf.getCovariance()
    }

    /** Perform a single predict step */
    public func predict(): Unit {
        kf.predict()
    }

    /** Perform a single update step */
    public func update(measurement: Position): Unit {
        kf.update([measurement.x, measurement.y])
    }

    /** Destroy the underlying filter */
    public func destroy(): Unit {
        kf.destroy()
    }
}
