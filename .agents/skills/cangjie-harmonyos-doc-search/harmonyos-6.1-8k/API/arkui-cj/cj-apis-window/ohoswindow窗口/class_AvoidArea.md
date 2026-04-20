## class AvoidArea

```cangjie
public class AvoidArea {
    public var visible: Bool
    public var leftRect: Rect
    public var topRect: Rect
    public var rightRect: Rect
    public var bottomRect: Rect
    public init(
        visible!: Bool,
        leftRect!: Rect,
        topRect!: Rect,
        rightRect!: Rect,
        bottomRect!: Rect
    )
}
```

**功能：** 避免区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var bottomRect

```cangjie
public var bottomRect: Rect
```

**功能：** 屏幕底部的矩形。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 22

### var leftRect

```cangjie
public var leftRect: Rect
```

**功能：** 屏幕左侧的矩形。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 22

### var rightRect

```cangjie
public var rightRect: Rect
```

**功能：** 屏幕右侧的矩形。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 22

### var topRect

```cangjie
public var topRect: Rect
```

**功能：** 屏幕顶部的矩形。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 22

### var visible

```cangjie
public var visible: Bool
```

**功能：** 避免区域是否在屏幕上可见。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 22

### init(Bool, Rect, Rect, Rect, Rect)

```cangjie
public init(
    visible!: Bool,
    leftRect!: Rect,
    topRect!: Rect,
    rightRect!: Rect,
    bottomRect!: Rect
)
```

**功能：** AvoidArea构造函数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|visible|Bool|是|-| **命名参数。** 避免区域是否可见。|
|leftRect|[Rect](#class-rect)|是|-| **命名参数。** 左侧矩形。|
|topRect|[Rect](#class-rect)|是|-| **命名参数。** 顶部矩形。|
|rightRect|[Rect](#class-rect)|是|-| **命名参数。** 右侧矩形。|
|bottomRect|[Rect](#class-rect)|是|-| **命名参数。** 底部矩形。|