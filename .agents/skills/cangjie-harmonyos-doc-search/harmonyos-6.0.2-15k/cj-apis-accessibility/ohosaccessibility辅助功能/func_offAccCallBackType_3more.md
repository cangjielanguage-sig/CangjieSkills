## func off(AccCallBackType)

```cangjie
public func off(`type`: AccCallBackType): Unit
```

**功能：** 取消监听辅助应用或触摸浏览功能启用状态变化事件。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AccCallBackType](#enum-acccallbacktype)|是|-|取消监听的事件名。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.|

## func on(AccCallBackType, Callback1Argument\<Bool>)

```cangjie
public func on(`type`: AccCallBackType, callback: Callback1Argument<Bool>): Unit
```

**功能：** 监听辅助应用或触摸浏览功能启用状态变化事件，使用callback异步回调。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AccCallBackType](#enum-acccallbacktype)|是|-|监听的事件名。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Bool>|是|-|回调函数，此状态为全局辅助应用启用状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AccessibilityKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class AccCallback <: Callback1Argument<Bool> {
    public func invoke(arg: Bool) {
        AppLog.info("callback: ${arg}")
    }
}

try {
    let cb = AccCallback()
    on(AccCallBackType.ACCCALLBACKTYPE_ACCESSIBILITYSTATECHANGE, cb)
    AppLog.info("on accessibilityStateChange")
    off(AccCallBackType.ACCCALLBACKTYPE_ACCESSIBILITYSTATECHANGE)
    AppLog.info("off accessibilityStateChange")
} catch (e: Exception) {
    AppLog.error("on/off accessibilityStateChange: ${e.toString()}")
}
```

## func sendAccessibilityEvent(EventInfo)

```cangjie
public func sendAccessibilityEvent(event: EventInfo): Unit
```

**功能：** 发送无障碍事件。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[EventInfo](#class-eventinfo)|是|-|无障碍事件对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AccessibilityKit.*
import ohos.base.*

try {
    let act: Action = Action.ACTION_FOCUS
    let evenInfo: EventInfo = EventInfo(`type`: EventType.EVENTTYPE_ACCESSIBILITYFOCUS, bundleName: "testDemo", triggerAction: act)
    sendAccessibilityEvent(evenInfo)
    AppLog.info("sendAccessibilityEvent")
} catch (e: Exception) {
    AppLog.error("sendAccessibilityEvent: ${e.toString()}")
}
```