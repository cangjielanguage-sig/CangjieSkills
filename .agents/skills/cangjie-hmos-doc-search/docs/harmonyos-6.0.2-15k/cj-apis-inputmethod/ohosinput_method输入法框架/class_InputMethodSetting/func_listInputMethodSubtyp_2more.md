### func listInputMethodSubtype(InputMethodProperty)

```cangjie
public func listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Array<InputMethodSubtype>
```

**功能：** 获取指定输入法应用的所有子类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|inputMethodProperty|[InputMethodProperty](#class-inputmethodproperty)|是|-|输入法应用属性。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[InputMethodSubtype](#class-inputmethodsubtype)>|返回指定输入法应用的所有子类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.|
  |12800001|package manager error.|
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

let im = getCurrentInputMethod()
let setting = getSetting()
setting.listInputMethodSubtype(im)
```

### func off(IMFEventType, ?Callback2Argument\<InputMethodProperty,InputMethodSubtype>)

```cangjie
public func off(
    eventType: IMFEventType,
    callback!: ?Callback2Argument<InputMethodProperty, InputMethodSubtype> = None
) : Unit
```

**功能：** 取消订阅eventType指定的事件。当前仅支持ImeChange。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[IMFEventType](#enum-imfeventtype)|是|-|回调函数事件类型，当前仅支持ImeChange。|
|callback|?[Callback2Argument](../BasicServicesKit/cj-apis-base.md#class-callback2argument)\<[InputMethodProperty](#class-inputmethodproperty),[InputMethodSubtype](#class-inputmethodsubtype)>|否|None| **命名参数。** 回调函数，返回取消订阅的输入法属性对象及子类型对象。|

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
setting.off(IMFEventType.ImeChange, callback: callback)
```