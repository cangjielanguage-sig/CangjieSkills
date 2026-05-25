## class TitleButtonRect

```cangjie
public class TitleButtonRect {
    public var right: Int32
    public var top: Int32
    public var width: UInt32
    public var height: UInt32
    public init(
      right!: Int32,
      top!: Int32,
      width!: UInt32,
      height!: UInt32
    )
}
```

**功能：** 标题栏上的最小化、最大化、关闭按钮矩形区域，该区域位置坐标相对窗口右上角。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### var height

```cangjie
public var height: UInt32
```

**功能：** 矩形区域的高度。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### var right

```cangjie
public var right: Int32
```

**功能：** 矩形区域的右边界。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### var top

```cangjie
public var top: Int32
```

**功能：** 矩形区域的上边界。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### var width

```cangjie
public var width: UInt32
```

**功能：** 矩形区域的宽度。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### init(Int32, Int32, UInt32, UInt32)

```cangjie
public init(
    right!: Int32,
    top!: Int32,
    width!: UInt32,
    height!: UInt32
)
```

**功能：** TitleButtonRect构造函数。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|right|Int32|是|-| **命名参数。** 矩形区域的右边界，单位为vp。|
|top|Int32|是|-| **命名参数。** 矩形区域的上边界，单位为vp。|
|width|UInt32|是|-| **命名参数。** 矩形区域的宽度，单位为vp。|
|height|UInt32|是|-| **命名参数。** 矩形区域的高度，单位为vp。|