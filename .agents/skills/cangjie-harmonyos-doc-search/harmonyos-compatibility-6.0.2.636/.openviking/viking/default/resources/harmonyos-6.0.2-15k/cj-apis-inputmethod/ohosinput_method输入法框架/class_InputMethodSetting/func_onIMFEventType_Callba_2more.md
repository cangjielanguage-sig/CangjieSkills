### func on(IMFEventType, Callback2Argument\<InputMethodProperty,InputMethodSubtype>)

```cangjie
public func on(eventType: IMFEventType, callback: Callback2Argument<InputMethodProperty, InputMethodSubtype>): Unit
```

**功能：** 订阅eventType指定的事件。使用callback异步回调。当前仅支持ImeChange。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[IMFEventType](#enum-imfeventtype)|是|-|回调函数事件类型，当前仅支持ImeChange。|
|callback|[Callback2Argument](../BasicServicesKit/cj-apis-base.md#class-callback2argument)\<[InputMethodProperty](#class-inputmethodproperty),[InputMethodSubtype](#class-inputmethodsubtype)>|是|-|回调函数，返回输入法属性对象及子类型对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*
import kit.UIKit.*

// 此处代码可添加在依赖项定义中
class ImeCallback <: Callback2Argument<InputMethodProperty, InputMethodSubtype> {
    ImeCallback(let f: (InputMethodProperty, InputMethodSubtype) -> Unit) {}

    public func invoke(arg1: InputMethodProperty, arg2: InputMethodSubtype): Unit {
        f(arg1, arg2)
    }
}

let setting = getSetting()
let callback = ImeCallback({
    p1: InputMethodProperty, p2: InputMethodSubtype =>
        AppLog.info("InputMethodProperty is ${p1.toString()}")
        AppLog.info("InputMethodSubtype is ${p2.toString()}")
})
setting.on(IMFEventType.ImeChange, callback)
```

### func showOptionalInputMethods()

```cangjie
public func showOptionalInputMethods(): Bool
```

**功能：** 显示输入法选择对话框。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当输入法选择对话框显示成功为true；否则为false。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |12800008|input method manager service error.|

- IllegalStateException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |unknown code|未知的错误码。|联系仓颉团队处理。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let setting = getSetting()
setting.showOptionalInputMethods()
```