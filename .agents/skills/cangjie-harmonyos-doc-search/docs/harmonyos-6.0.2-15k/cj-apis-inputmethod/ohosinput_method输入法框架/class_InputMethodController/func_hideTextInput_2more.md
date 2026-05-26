### func hideTextInput()

```cangjie
public func hideTextInput(): Unit
```

**功能：** 退出文本编辑状态。

> **说明：**
>
> 调用接口时，若软键盘处于显示状态，调用接口后软键盘会被隐藏。
> 调用该接口不会解除与输入法的绑定，再次调用[showTextInput](#func-showtextinput)时，可重新进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |12800003|input method client error.|
  |12800008|input method manager service error.|
  |12800009|input method client is detached.|

- IllegalStateException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |unknown code|未知的错误码。|联系仓颉团队处理。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let controller = getController()
controller.hideTextInput()
```

### func off(IMFEventType, ?CallbackObject)

```cangjie
public func off(eventType: IMFEventType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅指定事件eventType的指定回调函数callback。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[IMFEventType](#enum-imfeventtype)|是|-|回调函数事件类型，除ImeChange外均支持。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 取消订阅的回调函数，需要与on接口传入的保持一致。<br/>参数不填写或为None时，取消订阅type对应的所有回调事件。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*
import kit.UIKit.*

// 此处代码可添加在依赖项定义中
class InsertTextCallback <: Callback1Argument<String> {
    InsertTextCallback(let f: (String) -> Unit) {}

    public func invoke(arg1: String): Unit {
        f(arg1)
    }
}

let controller = getController()
let callback = InsertTextCallback({
    p: String => AppLog.info("callback1 excute: ${p}")
})
controller.on(IMFEventType.InsertText, callback)
controller.off(IMFEventType.InsertText, callback: callback)
```