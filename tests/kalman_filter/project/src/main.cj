package kalman

import std.math.*

main(): Int64 {
    println("=== Kalman Filter Target Tracking Demo ===")
    println()

    // Create tracker: dt=1.0s, process noise=0.5 m/s^2, measurement noise=10.0 m
    let tracker = TargetTracker(1.0, 0.5, 10.0)

    // True initial state: position (0, 0), velocity (10, 5) m/s
    let trueInitial = TargetState(0.0, 0.0, 10.0, 5.0)

    // Initialize filter with noisy initial estimate
    let initEstimate = TargetState(5.0, -3.0, 8.0, 6.0)
    tracker.initialize(initEstimate, 20.0, 5.0)

    // Run simulation for 50 steps
    let results = tracker.simulate(trueInitial, 50, 42)

    // Print results
    println("Step  Time   TrueX    TrueY    MeasX    MeasY    EstX     EstY     Error")
    println("----  ----   -----    -----    -----    -----    ----     ----     -----")

    var totalError = 0.0
    for (i in 0..results.size) {
        let r = results[i]
        if (i % 5 == 0 || i == results.size - 1) {
            println("${i + 1}     ${r.time}   ${formatF(r.trueState.px)}  ${formatF(r.trueState.py)}  ${formatF(r.measurement.x)}  ${formatF(r.measurement.y)}  ${formatF(r.estimated.px)}  ${formatF(r.estimated.py)}  ${formatF(r.positionError)}")
        }
        totalError += r.positionError
    }

    let avgError = totalError / Float64(results.size)
    println()
    println("Average position error: ${formatF(avgError)} m")

    // Check convergence: last 10 steps should have smaller error than first 10
    var earlyError = 0.0
    var lateError = 0.0
    for (i in 0..10) {
        earlyError += results[i].positionError
    }
    for (i in results.size - 10..results.size) {
        lateError += results[i].positionError
    }
    earlyError = earlyError / 10.0
    lateError = lateError / 10.0
    println("Early avg error (first 10): ${formatF(earlyError)} m")
    println("Late avg error (last 10):   ${formatF(lateError)} m")
    println("Filter converged: ${lateError < earlyError}")

    tracker.destroy()
    return 0
}

func formatF(v: Float64): String {
    // Simple formatting: keep 2 decimal places
    let sign = if (v < 0.0) { "-" } else { "" }
    let absV = abs(v)
    let intPart = Int64(absV)
    let fracPart = Int64((absV - Float64(intPart)) * 100.0 + 0.5)
    if (fracPart >= 100) {
        return "${sign}${intPart + 1}.00"
    }
    let fracStr = if (fracPart < 10) { "0${fracPart}" } else { "${fracPart}" }
    return "${sign}${intPart}.${fracStr}"
}
