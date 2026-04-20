## class Window

```cangjie
public class Window {}
```

**功能：** 窗口类。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### func destroyWindow()

```cangjie
public func destroyWindow(): Unit
```

**功能：** 销毁此窗口。此API仅对系统窗口或应用程序子窗口生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func getWindowAvoidArea(AvoidAreaType)

```cangjie
public func getWindowAvoidArea(areaType: AvoidAreaType): AvoidArea
```

**功能：** 获取避免区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|areaType|[AvoidAreaType](#enum-avoidareatype)|是|-|区域类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[AvoidArea](#class-avoidarea)|返回窗口无法显示的区域。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |401|Parameter error. Possible causes:<br> 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
  |1300002|This window state is abnormal.|

### func getWindowColorSpace()

```cangjie
public func getWindowColorSpace(): ColorSpace
```

**功能：** 获取设置的颜色空间。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpace](#enum-colorspace)|返回获取的颜色空间。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func getWindowProperties()

```cangjie
public func getWindowProperties(): WindowProperties
```

**功能：** 获取当前窗口的属性。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[WindowProperties](#class-windowproperties)|返回窗口属性。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func isWindowShowing()

```cangjie
public func isWindowShowing(): Bool
```

**功能：** 窗口是否显示。值true表示窗口显示，false表示相反。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回窗口是否显示。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func isWideGamutSupported()

```cangjie
public func isWideGamutSupported(): Bool
```

**功能：** 窗口是否支持宽色域设置。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|值true表示支持宽色域颜色空间，false表示相反。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|