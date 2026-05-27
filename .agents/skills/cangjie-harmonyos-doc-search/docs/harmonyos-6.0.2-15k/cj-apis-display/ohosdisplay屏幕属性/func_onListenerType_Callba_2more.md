## func on(ListenerType, Callback1Argument\<Bool>)

```cangjie
public func on(`type`: ListenerType, callback: Callback1Argument<Bool>): Unit
```

**功能：** 开启屏幕截屏、投屏、录屏状态变化的监听。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|String|是|-|监听事件。监听事件，固定为'LISTNER_TYPE_CAPTURE_STATUS_CHANGE'表示设备截屏、投屏或者录屏状态发生变化。|
|callback|Callback1Argument&lt;Bool&gt;|是|-|回调函数。表示设备截屏、投屏、录屏状态发生变化。true表示设备开始截屏、投屏或者录屏，false表示结束截屏、投屏、录屏。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |202|Parameter error: type is not supported.|
  |401|Parameter error: type is not supported.|

**示例:**

```cangjie
import ohos.display.*

class TestCallback <: Callback1Argument<Bool> {
    public init() {}
    public open func invoke(value: Bool): Unit {
        AppLog.info("Listening fold capture status: " + value.toString())
    }
}

let testCallback = TestCallback()
var temp: Unit = on(LISTNER_TYPE_CAPTURE_STATUS_CHANGE, testCallback)
```

## func on(ListenerType, Callback1Argument\<FoldDisplayMode>)

```cangjie
public func on(`type`: ListenerType, callback: Callback1Argument<FoldDisplayMode>): Unit
```

**功能：** 开启折叠设备屏幕显示模式变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|String|是|-|监听事件。固定为'LISTNER_TYPE_FOLD_DISPLAY_MODE_CHANGE'，表示折叠设备折叠状态发生变化。|
|callback|Callback1Argument&lt;[FoldDisplayMode](#enum-folddisplaymode)&gt;|是|-|回调函数。表示折叠设备屏幕显示模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |202|Parameter error: type is not supported.|
  |401|Parameter error: type is not supported.|

**示例:**

```cangjie
import ohos.display.*

class TestCallback <: Callback1Argument<FoldDisplayMode> {
    public init() {}
    public open func invoke(value: FoldDisplayMode): Unit {
        AppLog.info(
            "Display fold status changed, current fold status: " + match (value) {
            case FOLD_DISPLAY_MODE_UNKNOWN => "FOLD_DISPLAY_MODE_UNKNOWN"
            case FOLD_DISPLAY_MODE_FULL => "FOLD_DISPLAY_MODE_FULL"
            case FOLD_DISPLAY_MODE_MAIN => "FOLD_DISPLAY_MODE_MAIN"
            case FOLD_DISPLAY_MODE_SUB => "FOLD_DISPLAY_MODE_SUB"
            case FOLD_DISPLAY_MODE_COORDINATION => "FOLD_DISPLAY_MODE_COORDINATION"
            case _ => "Failed to get fold display mode."
        })
    }
}

let testCallback = TestCallback()
var temp: Unit = on(LISTNER_TYPE_FOLD_DISPLAY_MODE_CHANGE, testCallback)
```