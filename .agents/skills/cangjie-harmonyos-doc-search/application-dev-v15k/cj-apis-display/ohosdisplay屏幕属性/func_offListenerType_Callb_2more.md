## func off(ListenerType, Callback1Argument\<FoldDisplayMode>)

```cangjie
public func off(`type`: ListenerType, callback: Callback1Argument<FoldDisplayMode>): Unit
```

**功能：** 关闭折叠设备屏幕显示模式变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|String|是|-|监听事件。固定为'LISTNER_TYPE_FOLD_DISPLAY_MODE_CHANGE'，表示折叠设备折叠状态发生变化。|
|callback|Callback1Argument&lt;[FoldDisplayMode](#enum-folddisplaymode)&gt;|是|-|需要取消注册的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

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
var temp: Unit = off(LISTNER_TYPE_FOLD_DISPLAY_MODE_CHANGE, testCallback)
```

## func on(ListenerType, Callback1Argument\<UInt64>)

```cangjie
public func on(`type`: ListenerType, callback: Callback1Argument<UInt64>): Unit
```

**功能：** 开启显示设备变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ListenerType](#enum-listenertype)|是|-|监听事件。 type为"LISTNER_TYPE_CHANGE"，表示改变显示设备事件。|
|callback|Callback1Argument&lt;UInt64&gt;|是|-|回调函数。返回监听到的显示设备的id，该参数应为整数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |202|Parameter error:type is not supported.|
  |401|Parameter error:type is not supported.|

**示例:**

```cangjie
import ohos.display.*

class TestCallback <: Callback1Argument<UInt64> {
    public init() {}
    public open func invoke(value: UInt64): Unit {
        AppLog.info("Display change, ID: ${value}")
    }
}

let testCallback = TestCallback()
var temp: Unit = on(LISTNER_TYPE_CHANGE, testCallback)
```