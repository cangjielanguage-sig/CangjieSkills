### func on(WindowCallbackType, Callback1Argument\<UInt32>)

```cangjie
public func on(callbackType: WindowCallbackType, callback: Callback1Argument<UInt32>): Unit
```

**功能：** 注册keyboardHeightChange的回调。

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

### func resetAspectRatio()

```cangjie
public func resetAspectRatio(): Unit
```

**功能：** 重置窗口的宽高比。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|
  |1300004|Unauthorized operation.|

### func resize(UInt32, UInt32)

```cangjie
public func resize(width: UInt32, height: UInt32): Unit
```

**功能：** 设置窗口大小。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|UInt32|是|-|指示窗口的宽度。|
|height|UInt32|是|-|指示窗口的高度。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func setAspectRatio(Float64)

```cangjie
public func setAspectRatio(ratio: Float64): Unit
```

**功能：** 设置窗口的宽高比。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ratio|Float64|是|-|窗口除装饰外的宽高比。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|
  |1300004|Unauthorized operation.|

### func setPreferredOrientation(Orientation)

```cangjie
public func setPreferredOrientation(orientation: Orientation): Unit
```

**功能：** 为主窗口设置首选方向。它不会在不支持传感器旋转的设备上、2合1设备上或子窗口上生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|orientation|[Orientation](#enum-orientation)|是|-|窗口的方向配置。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |401|Parameter error. Possible cause: 1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types.|
  |1300002|This window state is abnormal.|