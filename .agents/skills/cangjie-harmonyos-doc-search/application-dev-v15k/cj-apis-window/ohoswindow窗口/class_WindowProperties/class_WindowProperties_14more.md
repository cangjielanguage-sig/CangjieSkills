## class WindowProperties

```cangjie
public class WindowProperties {
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
}
```

**功能：** 窗口属性。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### let windowRect

```cangjie
public let windowRect: Rect
```

**功能：** 表示窗口尺寸，可在页面生命周期[onPageShow](./cj-custom-component-lifecycle.md#func-onpageshow)或应用生命周期[onForeground](../apis/AbilityKit/cj-apis-ability.md#func-onforeground)阶段获取。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**起始版本：** 19

### let drawableRect

```cangjie
public let drawableRect: Rect
```

**功能：** 表示窗口内可绘制区域尺寸，其中左边界上边界是相对窗口计算。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**起始版本：** 19

### let winType

```cangjie
public let winType: WindowType
```

**功能：** 表示窗口类型。

**类型：** [WindowType](#enum-windowtype)

**读写能力：** 只读

**起始版本：** 19

### let isFullScreen

```cangjie
public let isFullScreen: Bool
```

**功能：** 表示是否全屏，初始为false。true表示全屏；false表示非全屏。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isLayoutFullScreen

```cangjie
public let isLayoutFullScreen: Bool
```

**功能：** 表示窗口是否为沉浸式，初始为false。true表示沉浸式；false表示非沉浸式。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let focusable

```cangjie
public let focusable: Bool
```

**功能：** 表示窗口是否可聚焦，初始为true。true表示可聚焦；false表示不可聚焦。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let touchable

```cangjie
public let touchable: Bool
```

**功能：** 表示窗口是否可触摸，初始为true。true表示可触摸；false表示不可触摸。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let brightness

```cangjie
public let brightness: Float32
```

**功能：** 表示屏幕亮度。可设置的亮度范围为[0.0, 1.0]，其取1.0时表示最大亮度值。如果窗口没有设置亮度值，表示亮度跟随系统，此时获取到的亮度值为-1。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### let isKeepScreenOn

```cangjie
public let isKeepScreenOn: Bool
```

**功能：** 表示屏幕是否常亮，初始为false。true表示常亮；false表示不常亮。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isPrivacyMode

```cangjie
public let isPrivacyMode: Bool
```

**功能：** 表示隐私模式是否开启，初始为false。true表示模式开启；false表示模式关闭。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isRoundCorner

```cangjie
public let isRoundCorner: Bool
```

**功能：** 表示窗口是否为圆角。初始为false。true表示圆角；false表示非圆角。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isTransparent

```cangjie
public let isTransparent: Bool
```

**功能：** 表示窗口是否透明。初始为false。true表示透明；false表示不透明。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let id

```cangjie
public let id: UInt32
```

**功能：** 表示窗口ID，初始值为0。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19