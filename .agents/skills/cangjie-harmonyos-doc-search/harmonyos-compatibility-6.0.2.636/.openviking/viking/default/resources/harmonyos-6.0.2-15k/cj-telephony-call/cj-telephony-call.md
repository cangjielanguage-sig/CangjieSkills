# 拨打电话

## 场景介绍

开发者可以通过以下方式实现拨打电话的功能：

- 对于三方应用，开发者可以使用makeCall接口，拉起系统电话应用，用户可以自行呼出通话。

## 基本概念

- 通话状态码
  将当前的通话状态上报给app，可以根据当前的通话状态去做一些逻辑处理。例如在当前没有正在进行呼叫的时候，可以正常拨打新的一通电话。

| 名称                | 说明                               |
| :------------------ | :--------------------------------- |
| CALL_STATE_UNKNOWN | 无效状态，当获取呼叫状态失败时返回。   |
| CALL_STATE_IDLE    | 表示没有正在进行的呼叫。              |
| CALL_STATE_RINGING | 表示来电正在振铃或等待。              |
| CALL_STATE_OFFHOOK | 表示至少有一个呼叫处于拨号、通话中或呼叫保持状态，并且没有新的来电振铃或等待。 |

## 约束与限制

1. 仅支持在标准系统上运行。
2. 设备需插入可用的SIM卡。

## 接口说明

> **说明：**
>
> 为了保证应用的运行效率，大部分API调用都是异步的，对于异步调用的API均提供了callback和Promise两种方式，以下示例均采用callback函数，更多方式可以查阅[API参考](../../API_Reference/source_zh_cn/apis/TelephonyKit/cj-apis-telephony_call.md)。

| 接口名 | 描述 |
| :------------------------------------------- | :--------------------------------- |
| hasVoiceCapability() | 判断是否具有语音功能。 |
| makeCall(UIAbilityContext, String) | 转到拨号屏幕，显示被叫号码。  |

observer模块为开发者提供订阅和取消订阅通话业务状态的功能。具体API说明详见[接口文档](../../API_Reference/source_zh_cn/apis/TelephonyKit/cj-apis-telephony_observer.md)。

| 接口名 | 描述 |
| :------------------------------------------------------------ | :------------------ |
| on(ObserverEventType, Callback1Argument\<CallStateInfo>, ?ObserverOptions) | 监听通话状态变化。 |

## 开发步骤

以使用makeCall拨打电话为例：

1. 导入call和observer模块。
2. 调用hasVoiceCapability，确认当前设备是否支持拨号。
3. 调用makeCall接口，跳转到拨号界面并显示待拨号的号码。
4. （可选）订阅通话业务状态变化。

```cangjie
// import需要的模块
import kit.TelephonyKit.*
import ohos.base.Callback1Argument
import kit.AbilityKit.*

var ctx = None<UIAbilityContext>

@Entry
@Component
class EntryView {
    @State
    var message: String = "Hello World"

    func build() {
        Row {
            Column {
                Text(this.message).fontSize(50).fontWeight(FontWeight.Bold).onClick {
                    evt =>
                    let isSupport = TelephonyCall.hasVoiceCapability()
                    if (isSupport) {
                        // 如果设备支持呼叫能力，则继续跳转到拨号界面，并显示拨号的号码
                        TelephonyCall.makeCall(ctx.getOrThrow(), "130xxxx")
                        // 订阅通话业务状态变化（可选）
                        TelephonyObserver.on(ObserverEventType.CallStateChange, StateInfoCb(),
                            options: ObserverOptions(slotId: 0))
                    }
                }
            }.width(100.percent)
        }.height(100.percent)
    }
}

class StateInfoCb <: Callback1Argument<CallStateInfo> {
    public func invoke(data: CallStateInfo): Unit {
        AppLog.info("call state change, data is: ${data.state.getValue()}, ${data.number}")
    }
}
```

```cangjie
// main_ability.cj
import kit.AbilityKit.{LaunchReason, LaunchParam, Want, UIAbility}
import kit.ArkUI.WindowStage
import kit.UIKit.AppLog

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        windowStage.loadContent("EntryView")
        // declared in index.cj
        ctx = this.context
    }
}
```
