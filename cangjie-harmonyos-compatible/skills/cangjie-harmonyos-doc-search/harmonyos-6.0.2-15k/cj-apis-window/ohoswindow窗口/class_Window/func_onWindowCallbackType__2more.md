### func on(WindowCallbackType, Callback1Argument\<WindowStatusType>)

```cangjie
public func on(callbackType: WindowCallbackType, callback: Callback1Argument<WindowStatusType>): Unit
```

**功能：** 开启窗口模式变化的监听。当窗口[windowStatus](#enum-windowstatustype)发生变化时进行通知（此时窗口属性可能还没有更新）。

> **说明：**
>
> 在2in1设备上调用本接口时，在窗口最大化状态时返回值对应为[WindowStatusType.FULL_SCREEN](#enum-windowstatustype)。
若想在2in1设备上区分当前窗口状态为最大化还是全屏，可在窗口状态为[WindowStatusType.FULL_SCREEN](#enum-windowstatustype)的情况下，再调用 [getImmersiveModeEnabledState()](#func-getimmersivemodeenabledstate) 接口进行进一步判断，到底是最大化状态还是全屏状态。若接口返回true则表示当前窗口为全屏状态，若接口返回false则表示当前窗口为最大化状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|监听事件，固定为WindowCallbackType.WindowStatusChange，即窗口模式变化事件。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[WindowStatusType](#enum-windowstatustype)>|是|-|回调函数。返回当前的窗口模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|
  |801|Capability not supported. Failed to call the API due to limited device capabilities.|

### func on(WindowCallbackType, Callback1Argument\<TitleButtonRect>)

```cangjie
public func on(callbackType: WindowCallbackType, callback: Callback1Argument<TitleButtonRect>): Unit
```

**功能：** 开启窗口标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听。

> **说明：**
>
> 仅在2in1设备中，对存在标题栏和三键区的窗口形态生效。该接口需要在[loadContent()](#func-loadcontentstring)调用生效后使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|监听事件类型，固定为WindowCallbackType.WindowTitleButtonRectChange，即标题栏上的最小化、最大化、关闭按钮矩形区域变化事件。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[TitleButtonRect](#class-titlebuttonrect)>|是|-|回调函数。返回当前标题栏上的最小化、最大化、关闭按钮矩形区域。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|
  |801|Capability not supported. Failed to call the API due to limited device capabilities.|
  |1300002|This window state is abnormal.|