### func setWindowBrightness(Float32)

```cangjie
public func setWindowBrightness(brightness: Float32): Unit
```

**功能：** 允许应用主窗口设置屏幕亮度值。

> **说明：**
>
> 当前屏幕亮度规格：窗口设置屏幕亮度生效时，控制中心不可以调整系统屏幕亮度，窗口恢复默认系统亮度之后，控制中心可以调整系统屏幕亮度。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|brightness|Float32|是|-|屏幕亮度值。取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示默认亮度。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setWindowBrightness: This window state is abnormal.|

### func setWindowColorSpace(ColorSpace)

```cangjie
public func setWindowColorSpace(colorSpace: ColorSpace): Unit
```

**功能：** 设置当前窗口为广色域模式或默认色域模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorSpace|[ColorSpace](#enum-colorspace)|是|-|设置色域模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setWindowColorSpace: This window state is abnormal.|

### func setWindowDecorHeight(Int32)

```cangjie
public func setWindowDecorHeight(height: Int32): Unit
```

**功能：** 设置窗口的标题栏高度。

> **说明：**
>
> - 仅在2in1设备或平板设备的自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下，对存在标题栏和三键区的窗口形态生效。该接口需要在[loadContent()](#func-loadcontentstring)调用生效后使用。
> - 当主窗口进入全屏沉浸状态时，此时鼠标Hover到窗口标题栏热区时，会显示悬浮标题栏，悬浮标题栏高度固定为37.vp。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|height|Int32|是|-|设置的窗口标题栏高度，仅支持具有窗口标题栏的窗口。取值范围为[37,112]，范围外为非法参数，单位为vp。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|[Window] setWindowDecorHeight: Parameter error.|
  |801|[Window] setWindowDecorHeight: Capability not supported.|
  |1300002|[Window] setWindowDecorHeight: This window state is abnormal.|