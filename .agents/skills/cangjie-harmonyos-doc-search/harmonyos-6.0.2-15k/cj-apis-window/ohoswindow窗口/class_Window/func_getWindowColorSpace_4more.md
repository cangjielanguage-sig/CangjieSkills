### func getWindowColorSpace()

```cangjie
public func getWindowColorSpace(): ColorSpace
```

**功能：** 获取当前窗口色域模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpace](#enum-colorspace)|当前色域模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] getWindowColorSpace: This window state is abnormal.|

### func getWindowDecorHeight()

```cangjie
public func getWindowDecorHeight(): Int32
```

**功能：** 获取窗口的标题栏高度。

> **说明：**
>
> 仅在2in1设备或平板设备的自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下，对存在标题栏和三键区的窗口形态生效。该接口需要在[loadContent()](#func-loadcontentstring)调用生效后使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回的窗口标题栏高度。该参数取值范围为[37,112]，单位为vp。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|[Window] getWindowDecorHeight: Capability not supported.|
  |1300002|[Window] getWindowDecorHeight: This window state is abnormal.|

### func getWindowLimits()

```cangjie
public func getWindowLimits(): WindowLimits
```

**功能：** 获取当前应用窗口的尺寸限制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WindowLimits](#class-windowlimits)|当前窗口尺寸限制。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|[Window] getWindowAvoidArea: Capability not supported.|
  |1300002|[Window] getWindowAvoidArea: This window state is abnormal.|

### func getWindowProperties()

```cangjie
public func getWindowProperties(): WindowProperties
```

**功能：** 获取当前窗口的属性，返回WindowProperties。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[WindowProperties](#class-windowproperties)|当前窗口属性。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|This window state is abnormal.|