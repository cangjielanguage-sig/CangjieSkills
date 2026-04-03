### func setWindowDecorVisible(Bool)

```cangjie
public func setWindowDecorVisible(isVisible: Bool): Unit
```

**功能：** 设置窗口标题栏是否可见。

> **说明：**
>
> - 对存在标题栏和三键区的窗口形态生效。该接口需要在[loadContent()](#func-loadcontentstring)调用生效后使用。
> - 设置窗口标题栏不可见后，当主窗口进入全屏沉浸状态时，此时鼠标Hover到上方窗口标题栏热区上会显示悬浮标题栏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isVisible|Bool|是|-|设置标题栏是否可见，true为可见，false为隐藏。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|[Window] setWindowDecorVisible: Capability not supported. |
  |1300002|[Window] setWindowDecorVisible: This window state is abnormal.|

### func setWindowFocusable(Bool)

```cangjie
public func setWindowFocusable(isFocusable: Bool): Unit
```

**功能：** 设置使用点击或其他方式使该窗口获焦的场景时，该窗口是否支持窗口焦点从点击前的获焦窗口切换到该窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isFocusable|Bool|是|-|点击时是否支持切换焦点窗口。true表示支持；false表示不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setWindowFocusable: This window state is abnormal.|

### func setWindowGrayScale(Float32)

```cangjie
public func setWindowGrayScale(grayScale: Float32): Unit
```

**功能：** 设置窗口灰阶。

> **说明：**
>
> 该接口需要在调用[loadContent()](#func-loadcontentstring)使窗口加载页面内容后调用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|grayScale|Float32|是|-|窗口灰阶。取值范围为[0.0, 1.0]。0.0表示窗口图像无变化，1.0表示窗口图像完全转为灰度图像，0.0至1.0之间时效果呈线性变化。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|[Window] setWindowGrayScale: Parameter error. |
  |1300002|[Window] setWindowGrayScale: This window state is abnormal.|

### func setWindowKeepScreenOn(Bool)

```cangjie
public func setWindowKeepScreenOn(isKeepScreenOn: Bool): Unit
```

**功能：** 设置屏幕是否为常亮状态。

> **说明：**
>
> 规范使用该接口：仅在必要场景（导航、视频播放、绘画、游戏等场景）下，设置该属性为true；退出上述场景后，应当重置该属性为false；其他场景（无屏幕互动、音频播放等）下，不使用该接口；系统检测到非规范使用该接口时，可能会恢复自动灭屏功能。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isKeepScreenOn|Bool|是|-|设置屏幕是否为常亮状态。true表示常亮；false表示不常亮。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setWindowKeepScreenOn: This window state is abnormal.|