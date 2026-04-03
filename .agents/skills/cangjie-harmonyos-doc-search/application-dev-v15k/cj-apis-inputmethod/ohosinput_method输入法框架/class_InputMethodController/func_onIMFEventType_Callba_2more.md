### func on(IMFEventType, Callback1Argument\<Range>)

```cangjie
public func on(eventType: IMFEventType, callback: Callback1Argument<Range>): Unit
```

**功能：** 订阅eventType指定的事件。使用callback异步回调。当前仅支持SelectByRange。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[IMFEventType](#enum-imfeventtype)|是|-|回调函数事件类型，当前仅支持SelectByRange。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[Range](#class-range)>|是|-|回调函数，返回需要选中的文本范围。<br/>根据传入的文本范围，开发者在回调函数中编辑框中相应文本。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.|
  |12800009|input method client is detached.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*
import kit.UIKit.*
import kit.IMEKit.Range as IMERange

// 此处代码可添加在依赖项定义中
class SelectByRangeCallback <: Callback1Argument<IMERange> {
    SelectByRangeCallback(let f: (IMERange) -> Unit) {}

    public func invoke(arg1: IMERange): Unit {
        f(arg1)
    }
}

let controller = getController()
let callback = SelectByRangeCallback({
    p: IMERange => AppLog.info("callback1 excute: range start ${p.start}, range end ${p.end}")
})
controller.on(IMFEventType.SelectByRange, callback)
```

### func on(IMFEventType, Callback1Argument\<Movement>)

```cangjie
public func on(eventType: IMFEventType, callback: Callback1Argument<Movement>): Unit
```

**功能：** 订阅eventType指定的事件。使用callback异步回调。当前仅支持SelectByMovement。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[IMFEventType](#enum-imfeventtype)|是|-|回调函数事件类型，当前仅支持SelectByMovement。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[Movement](#class-movement)>|是|-|回调函数，返回光标移动的方向。<br/>根据传入的光标移动方向，选中编辑框中相应文本。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.|
  |12800009|input method client is detached.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*
import kit.UIKit.*

// 此处代码可添加在依赖项定义中
class SelectBMCallback <: Callback1Argument<Movement> {
    SelectBMCallback(let f: (Movement) -> Unit) {}

    public func invoke(arg1: Movement): Unit {
        f(arg1)
    }
}

let controller = getController()
let callback = SelectBMCallback({
    p: Movement =>
        let direction = match(p.direction) {
            case CURSOR_UP => "up"
            case _ => "others"
        }
        AppLog.info("callback1 excute: ${direction}")
})
controller.on(IMFEventType.SelectByMovement, callback)
```