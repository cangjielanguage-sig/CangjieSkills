### func on(WindowCallbackType, Callback1Argument\<RectChangeOptions>)

```cangjie
public func on(callbackType: WindowCallbackType, callback: Callback1Argument<RectChangeOptions>): Unit
```

**功能：** 开启窗口矩形（窗口位置及窗口大小）变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|监听事件，固定为WindowCallbackType.WindowRectChange，即窗口矩形变化事件。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[RectChangeOptions](#class-rectchangeoptions)>|是|-|回调函数。返回当前窗口矩形变化值及变化原因。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|
  |801|Capability not supported. Failed to call the API due to limited device capabilities.|
  |1300002|This window state is abnormal.|
  |1300003|This window manager service works abnormally.|

### func recover()

```cangjie
public func recover(): Unit
```

**功能：** 将主窗口从全屏、最大化、分屏模式下还原为浮动窗口，并恢复到进入该模式之前的大小和位置，已经是浮动窗口模式不可再还原。

> **说明：**
>
> 此接口仅在多窗层叠布局效果下生效，仅2in1设备可用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|[Window] Recover: Capability not supported. |
  |1300002|[Window] Recover: This window state is abnormal.|

### func resetAspectRatio()

```cangjie
public func resetAspectRatio(): Unit
```

**功能：** 取消设置窗口内容布局的比例。

> **说明：**
>
> 仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为[WindowStatusType.FLOATING](#enum-windowstatustype)）下生效，调用后将清除持久化储存的比例信息。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] resetAspectRatio: This window state is abnormal.|
  |1300004|[Window] resetAspectRatio: Unauthorized operation.|