## func off(ListenerType)

```cangjie
public func off(`type`: ListenerType): Unit
```

**功能：** 关闭显示设备变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ListenerType](#enum-listenertype)|是|-|监听事件类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.|

**示例:**

```cangjie
import ohos.display.*

var temp: Unit = off(LISTNER_TYPE_CHANGE)
```

## func off(ListenerType, Callback1Argument\<UInt64>)

```cangjie
public func off(`type`: ListenerType, callback: Callback1Argument<UInt64>): Unit
```

**功能：** 关闭显示设备变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ListenerType](#enum-listenertype)|是|-|监听事件。 type为"LISTNER_TYPE_CHANGE"，表示改变显示设备事件。例如：显示器方向改变。|
|callback|Callback1Argument&lt;UInt64&gt;|是|-|需要取消注册的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |202|Parameter error: type is not supported.|
  |401|Parameter error: type is not supported.|

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
var temp: Unit = off(LISTNER_TYPE_CHANGE, testCallback)
```

## func off(ListenerType, Callback1Argument\<FoldStatus>)

```cangjie
public func off(`type`: ListenerType, callback: Callback1Argument<FoldStatus>): Unit
```

**功能：** 关闭折叠设备折叠状态变化的监听。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|String|是|-| 监听事件。固定为'LISTNER_TYPE_FOLD_STATUS_CHANGE'，表示折叠设备折叠状态发生变化。 |
|callback|Callback1Argument&lt;[FoldStatus](#enum-foldstatus)&gt;|是|-|回调函数。表示折叠设备折叠状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |202|Parameter error: type is not supported.|
  |401|Parameter error: type is not supported.|

**示例:**

```cangjie
import ohos.display.*

class TestCallback <: Callback1Argument<FoldStatus> {
    public init() {}
    public open func invoke(value: FoldStatus): Unit {
        AppLog.info(
            "Display fold status changed, current fold status: " + match (value) {
            case FOLD_STATUS_UNKNOWN => "FOLD_STATUS_UNKNOWN"
            case FOLD_STATUS_EXPANDED => "FOLD_STATUS_EXPANDED"
            case FOLD_STATUS_FOLDED => "FOLD_STATUS_FOLDED"
            case FOLD_STATUS_HALF_FOLDED => "FOLD_STATUS_HALF_FOLDED"
            case _ => "Failed to get fold status."
        })
    }
}

let testCallback = TestCallback()
var temp: Unit = on(LISTNER_TYPE_FOLD_STATUS_CHANGE, testCallback)
```