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

**功能：** 窗口矩形区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var height

```cangjie
public var height: UInt32
```

**功能：** 矩形区域的高度，单位为px。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 22

### var left

```cangjie
public var left: Int32
```

**功能：** 矩形区域的左边界，单位为px。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 22

### var top

```cangjie
public var top: Int32
```

**功能：** 矩形区域的上边界，单位为px。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 22

### var width

```cangjie
public var width: UInt32
```

**功能：** 矩形区域的宽度，单位为px。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** UInt32

**读写能力：** 可读写

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
|left|Int32|是|-| **命名参数。** 矩形区域的左边界，单位为px。|
|top|Int32|是|-| **命名参数。** 矩形区域的上边界，单位为px。|
|width|UInt32|是|-| **命名参数。** 矩形区域的宽度，单位为px。|
|height|UInt32|是|-| **命名参数。** 矩形区域的高度，单位为px。|

## class Size

```cangjie
public class Size {
    public var width: UInt32
    public var height: UInt32
    public init(
        width!: UInt32,
        height!: UInt32
    )
}
```

**功能：** 窗口大小。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var height

```cangjie
public var height: UInt32
```

**功能：** 窗口的高度。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var width

```cangjie
public var width: UInt32
```

**功能：** 窗口的宽度。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### init(UInt32, UInt32)

```cangjie
public init(
    width!: UInt32,
    height!: UInt32
)
```

**功能：** Size构造函数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|UInt32|是|-| **命名参数。** 窗口宽度。|
|height|UInt32|是|-| **命名参数。** 窗口高度。|