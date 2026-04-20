## func on(ListenerType, Callback1Argument\<FoldDisplayMode>)

```cangjie
public func on(listenerType: ListenerType, callback: Callback1Argument<FoldDisplayMode>): Unit
```

**功能：** 注册折叠显示模式变化的回调。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|listenerType|[ListenerType](#enum-listenertype)|是|-|折叠显示模式变化的事件。|
|callback|Callback1Argument\<[FoldDisplayMode](#enum-folddisplaymode)>|是|-|用于返回当前折叠显示模式的回调。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |401|Parameter error. Possible causes:<br> 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
  |1400003|This display manager service works abnormally.|

**示例：**

<!-- code_check_manual -->

```cangjie
import kit.ArkUI.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.callback_invoke.Callback1Argument
import ohos.business_exception.BusinessException

class TestCallback <: Callback1Argument<FoldDisplayMode> {
    public init() {}
    public open func invoke(error: ?BusinessException, value: FoldDisplayMode): Unit {
        Hilog.info(0, "CangjieTest", "Display fold status changed, current fold status: " + match (value) {
            case FoldDisplayModeUnknown => "FoldDisplayModeUnknown"
            case FoldDisplayModeFull => "FoldDisplayModeFull"
            case FoldDisplayModeMain => "FoldDisplayModeMain"
            case FoldDisplayModeSub => "FoldDisplayModeSub"
            case FoldDisplayModeCoordination => "FoldDisplayModeCoordination"
            case _ => "Failed to get fold display mode."
        })
    }
}

func test() {
    let testCallback = TestCallback()
    try {
        var temp: Unit = on(ListenerTypeFoldDisplayModeChange, testCallback)
    } catch (e: BusinessException) {
        Hilog.error(0, "CangjieTest", e.toString())
    }
}
```