## func off(ListenerType)

```cangjie
public func off(listenerType: ListenerType): Unit
```

**功能：** 禁用所有显示屏设备变化的监听器。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|listenerType|[ListenerType](#enum-listenertype)|是|-|监听事件类型。|

## func off(ListenerType, Callback1Argument\<FoldDisplayMode>)

```cangjie
public func off(listenerType: ListenerType, callback: Callback1Argument<FoldDisplayMode>): Unit
```

**功能：** 取消注册折叠显示模式变化的回调。

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
import ohos.display.*
class TestCallback <: Callback1Argument<FoldDisplayMode> {
    public init() {}
    public open func invoke(value: FoldDisplayMode): Unit {
        AppLog.info(
            "Display fold status changed, current fold status: " + match (value) {
                case FoldDisplayModeUnknown => "FoldDisplayModeUnknown"
                case FoldDisplayModeFull => "FoldDisplayModeFull"
                case FoldDisplayModeMain => "FoldDisplayModeMain"
                case FoldDisplayModeSub => "FoldDisplayModeSub"
                case FoldDisplayModeCoordination => "FoldDisplayModeCoordination"
                case _ => "Failed to get fold display mode."
            })
    }
}
let testCallback = TestCallback()
try {
    var temp: Unit = off(ListenerTypeFoldDisplayModeChange, testCallback)
} catch (e: BusinessException) {
    AppLog.error(exception.toString())
}
```