### func minimize()

```cangjie
public func minimize(): Unit
```

**功能：** 最小化主窗口（如果调用者是主窗口）。主窗口可以在停靠栏中还原。对于2合1设备，可以通过调用recover()来还原。
隐藏子窗口（如果调用者是子窗口）。子窗口无法在停靠栏中还原。可以通过调用showWindow()再次使其可见。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |801|Capability not supported. Failed to call the API due to limited device capabilities.|
  |1300002|This window state is abnormal.|

### func moveWindowTo(Int32, Int32)

```cangjie
public func moveWindowTo(x: Int32, y: Int32): Unit
```

**功能：** 设置窗口位置。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int32|是|-|指示窗口的X坐标。|
|y|Int32|是|-|指示窗口的Y坐标。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func off(WindowCallbackType)

```cangjie
public func off(callbackType: WindowCallbackType): Unit
```

**功能：** 取消注册指定事件的回调。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|事件类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300016|Parameter error. Possible cause: 1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|

### func off(WindowCallbackType, Callback1Argument\<UInt32>)

```cangjie
public func off(callbackType: WindowCallbackType, callback: Callback1Argument<UInt32>): Unit
```

**功能：** 取消注册keyboardHeightChange的回调。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|值固定为KeyboardHeightChange，表示键盘高度变化事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<UInt32>|是|-|用于返回当前键盘高度的回调，该高度为整数，单位为px。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300016|Parameter error. Possible cause: 1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|