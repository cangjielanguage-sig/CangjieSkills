### func off(WindowCallbackType, Callback1Argument\<TitleButtonRect>)

```cangjie
public func off(callbackType: WindowCallbackType, callback: Callback1Argument<TitleButtonRect>): Unit
```

**功能：** 关闭窗口标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听。

> **说明：**
>
> 仅在2in1设备中，对存在标题栏和三键区的窗口形态生效。该接口需要在[loadContent()](#func-loadcontentstring)调用生效后使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|监听事件类型，固定为WindowCallbackType.WindowTitleButtonRectChange，即标题栏上的最小化、最大化、关闭按钮矩形区域变化事件。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[TitleButtonRect](#class-titlebuttonrect)>|是|-|回调函数。返回当前标题栏上的最小化、最大化、关闭按钮矩形区域。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|
  |801|Capability not supported. Failed to call the API due to limited device capabilities.|
  |1300002|This window state is abnormal.|

### func off(WindowCallbackType, Callback1Argument\<RectChangeOptions>)

```cangjie
public func off(callbackType: WindowCallbackType, callback: Callback1Argument<RectChangeOptions>): Unit
```

**功能：** 关闭窗口矩形（窗口位置及窗口大小）变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|监听事件，固定为WindowCallbackType.WindowRectChange，即窗口矩形变化事件。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[RectChangeOptions](#class-rectchangeoptions)>|是|-|回调函数。返回当前的窗口矩形及变化原因。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|
  |801|Capability not supported. Failed to call the API due to limited device capabilities.|
  |1300002|This window state is abnormal.|
  |1300003|This window manager service works abnormally.|