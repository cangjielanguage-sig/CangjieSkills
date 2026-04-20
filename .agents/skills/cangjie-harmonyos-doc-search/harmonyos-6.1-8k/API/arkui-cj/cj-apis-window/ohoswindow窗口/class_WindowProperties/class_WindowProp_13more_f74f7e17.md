## class WindowProperties

```cangjie
public class WindowProperties {
    public var windowRect: Rect
    public var drawableRect: Rect
    public var windowType: WindowType
    public var isFullScreen: Bool
    public var isLayoutFullScreen: Bool
    public var focusable: Bool
    public var touchable: Bool
    public var brightness: Float32
    public var isKeepScreenOn: Bool
    public var isPrivacyMode: Bool
    public var isTransparent: Bool
    public var id: UInt32
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
}
```

**功能：** 窗口属性，不会自动更新。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var brightness

```cangjie
public var brightness: Float32
```

**功能：** 窗口亮度值。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 22

### var drawableRect

```cangjie
public var drawableRect: Rect
```

**功能：** 相对于窗口的位置和可绘制区域大小。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 22

### var focusable

```cangjie
public var focusable: Bool
```

**功能：** 窗口是否可以获得焦点。默认值为true。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 22

### var id

```cangjie
public var id: UInt32
```

**功能：** 窗口ID。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 22

### var isFullScreen

```cangjie
public var isFullScreen: Bool
```

**功能：** 窗口是否以全屏模式显示。默认值为false。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 22

### var isKeepScreenOn

```cangjie
public var isKeepScreenOn: Bool
```

**功能：** 是否保持屏幕常亮。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 22

### var isLayoutFullScreen

```cangjie
public var isLayoutFullScreen: Bool
```

**功能：** 窗口布局是否为全屏模式（窗口是否沉浸式）。默认值为false。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 22

### var isPrivacyMode

```cangjie
public var isPrivacyMode: Bool
```

**功能：** 是否处于隐私模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 22

### var isTransparent

```cangjie
public var isTransparent: Bool
```

**功能：** 是否透明。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 22

### var touchable

```cangjie
public var touchable: Bool
```

**功能：** 窗口是否可触摸。默认值为false。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 22

### var windowType

```cangjie
public var windowType: WindowType
```

**功能：** 窗口类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** [WindowType](#enum-windowtype)

**读写能力：** 可读写

**起始版本：** 22

### var windowRect

```cangjie
public var windowRect: Rect
```

**功能：** 窗口的位置和大小。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 22