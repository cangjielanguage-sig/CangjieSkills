### WindowProperties(Rect, Rect, WindowType, Bool, Bool, Bool, Bool, Float32, Bool, Bool, Bool, Bool, UInt32)

```cangjie
public WindowProperties(
    public let windowRect: Rect,
    public let drawableRect: Rect,
    public let winType: WindowType,
    public let isFullScreen: Bool,
    public let isLayoutFullScreen: Bool,
    public let focusable: Bool,
    public let touchable: Bool,
    public let brightness: Float32,
    public let isKeepScreenOn: Bool,
    public let isPrivacyMode: Bool,
    public let isRoundCorner: Bool,
    public let isTransparent: Bool,
    public let id: UInt32
)
```

**功能：** 构建一个WindowProperties类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|windowRect|[Rect](#class-rect)|是|-|窗口尺寸，可在页面生命周期[onPageShow](./cj-custom-component-lifecycle.md#func-onpageshow)或应用生命周期[onForeground](../apis/AbilityKit/cj-apis-ability.md#func-onforeground)阶段获取。|
|drawableRect|[Rect](#class-rect)|是|-|窗口内可绘制区域尺寸，其中左边界上边界是相对窗口计算。|
|winType|[WindowType](#enum-windowtype)|是|-|窗口类型。|
|isFullScreen|Bool|是|-|是否全屏，初始为false。true表示全屏；false表示非全屏。|
|isLayoutFullScreen|Bool|是|-|窗口是否为沉浸式，初始为false。true表示沉浸式；false表示非沉浸式。|
|focusable|Bool|是|-|窗口是否可聚焦，初始为true。true表示可聚焦；false表示不可聚焦。|
|touchable|Bool|是|-|窗口是否可触摸，初始为true。true表示可触摸；false表示不可触摸|
|brightness|Float32|是|-|屏幕亮度。可设置的亮度范围为[0.0, 1.0]，其取1.0时表示最大亮度值。如果窗口没有设置亮度值，表示亮度跟随系统，此时获取到的亮度值为-1。|
|isKeepScreenOn|Bool|是|-|屏幕是否常亮，初始为false。true表示常亮；false表示不常亮。|
|isPrivacyMode|Bool|是|-|窗口是否为隐私模式。true表示模式开启；false表示模式关闭。|
|isRoundCorner|Bool|是|-|窗口是否为圆角。默认为false。true表示圆角；false表示非圆角。|
|isTransparent|Bool|是|-|窗口是否透明。默认为false。true表示透明；false表示不透明。|
|id|UInt32|是|-|窗口ID。<br>初始值：0<br>|