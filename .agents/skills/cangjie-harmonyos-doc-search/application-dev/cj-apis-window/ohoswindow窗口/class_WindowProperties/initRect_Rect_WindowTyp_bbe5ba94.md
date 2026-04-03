### init(Rect, Rect, WindowType, Bool, Bool, Bool, Bool, Float32, Bool, Bool, Bool, UInt32)

```cangjie
public init(
    windowRect!: Rect,
    drawableRect!: Rect,
    windowType!: WindowType,
    isFullScreen!: Bool,
    isLayoutFullScreen!: Bool,
    focusable!: Bool,
    touchable!: Bool,
    brightness!: Float32,
    isKeepScreenOn!: Bool,
    isPrivacyMode!: Bool,
    isTransparent!: Bool,
    id!: UInt32
)
```

**功能：** WindowProperties构造函数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|windowRect|[Rect](#class-rect)|是|-| **命名参数。** 窗口矩形。|
|drawableRect|[Rect](#class-rect)|是|-| **命名参数。** 可绘制矩形。|
|windowType|[WindowType](#enum-windowtype)|是|-| **命名参数。** 窗口类型。|
|isFullScreen|Bool|是|-| **命名参数。** 是否全屏。|
|isLayoutFullScreen|Bool|是|-| **命名参数。** 是否布局全屏。|
|focusable|Bool|是|-| **命名参数。** 是否可获得焦点。|
|touchable|Bool|是|-| **命名参数。** 是否可触摸。|
|brightness|Float32|是|-| **命名参数。** 亮度值。|
|isKeepScreenOn|Bool|是|-| **命名参数。** 是否保持屏幕常亮。|
|isPrivacyMode|Bool|是|-| **命名参数。** 是否隐私模式。|
|isTransparent|Bool|是|-| **命名参数。** 是否透明。|
|id|UInt32|是|-| **命名参数。** 窗口ID。|