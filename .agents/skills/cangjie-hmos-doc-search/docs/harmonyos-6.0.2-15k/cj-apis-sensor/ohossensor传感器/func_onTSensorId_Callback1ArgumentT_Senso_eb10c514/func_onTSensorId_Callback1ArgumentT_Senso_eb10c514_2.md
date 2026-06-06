// 此处代码可添加在依赖项定义中
class SensorCallback <: Callback1Argument<OrientationResponse> {
    init() {}
    public func invoke(arg: OrientationResponse): Unit {
        AppLog.error(
            "Succeeded in getting SensorCallback arg: steps: ${arg.timestamp}, alpha: ${arg.alpha},  beta: ${arg.beta},  gamma: ${arg.gamma}"
        )
    }
}

let callback = SensorCallback()
try {
    on(SensorId.ORIENTATION, callback,
        option: SensorOptions(IntervalOption.SensorNumber(2_000_000)))
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```