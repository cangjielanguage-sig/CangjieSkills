### func off(WindowCallbackType, Callback0Argument)

```cangjie
public func off(callbackType: WindowCallbackType, callback: Callback0Argument): Unit
```

**功能：** 关闭窗口事件监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|监听事件类型，当输入WindowCallbackType.TouchOutside时是本窗口范围外的点击事件的监听；<br>输入WindowCallbackType.Screenshot时截屏事件的监听；<br>输入WindowCallbackType.DialogTargetTouch时模态窗口目标窗口的点击事件的监听；<br>输入WindowCallbackType.NoInteractionDetected为本窗口在指定超时时间内无交互的事件。<br>输入WindowCallbackType.SubWindowClose为子窗口关闭事件。|
|callback|[Callback0Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-|回调函数实例对象。<br>当type为WindowCallbackType.TouchOutside时，为点击事件发生在本窗口范围之外的回调。<br>当type为WindowCallbackType.Screenshot时， 为截屏事件时的回调。<br>当type为WindowCallbackType.DialogTargetTouch时，为点击事件发生在模态窗口目标窗口的回调。<br>当type为WindowCallbackType.NoInteractionDetected时，为本窗口在指定超时时间内无交互事件时的回调。<br>当type为WindowCallbackType.SubWindowClose时，为点击子窗口右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑需要有Bool类型的返回值，该返回值决定当前子窗是否继续关闭，true表示不关闭子窗，false表示关闭子窗。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|