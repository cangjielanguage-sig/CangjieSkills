## class FoldCreaseRegion

```cangjie
public class FoldCreaseRegion {
    public let displayId: UInt32
    public let creaseRects: Array<Rect>
    public init(
        displayId!: UInt32,
        creaseRects!: Array<Rect>
    )
}
```

**功能：** 构造一个FoldCreaseRegion类型的对象。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### let displayId

```cangjie
public let displayId: UInt32
```

**功能：** 显示ID，用于标识crease所在的屏幕。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**功能：** 折叠 crease 区域。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### let creaseRects

```cangjie
public let creaseRects: Array<Rect>
```

**功能：** crease 区域。

**类型：** Array\<[Rect](#class-rect)>

**读写能力：** 只读

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### init(UInt32, Array\<Rect>)

```cangjie
public init(
    displayId!: UInt32,
    creaseRects!: Array<Rect>
)
```

**功能：** FoldCreaseRegion构造函数。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|displayId|UInt32|是|-| **命名参数。** 显示屏ID。|
|creaseRects|Array\<[Rect](#class-rect)>|是|-| **命名参数。** crease区域。|

## class Rect

```cangjie
public class Rect {
    public var left: Int32
    public var top: Int32
    public var width: UInt32
    public var height: UInt32
    public init(
    left!: Int32,
    top!: Int32,
    width!: UInt32,
    height!: UInt32
    )
}
```

**功能：** 矩形。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var height

```cangjie
public var height: UInt32
```

**功能：** 矩形高度，以像素为单位。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var left

```cangjie
public var left: Int32
```

**功能：** 矩形左上顶点的Y轴坐标，以像素为单位。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var top

```cangjie
public var top: Int32
```

**功能：** 矩形左上顶点的Y轴坐标，以像素为单位。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var width

```cangjie
public var width: UInt32
```

**功能：** 矩形宽度，以像素为单位。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### init(Int32, Int32, UInt32, UInt32)

```cangjie
public init(
    left!: Int32,
    top!: Int32,
    width!: UInt32,
    height!: UInt32
)
```

**功能：** Rect构造函数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|Int32|是|-| **命名参数。** 矩形左边界坐标。|
|top|Int32|是|-| **命名参数。** 矩形上边界坐标。|
|width|UInt32|是|-| **命名参数。** 矩形宽度。|
|height|UInt32|是|-| **命名参数。** 矩形高度。|