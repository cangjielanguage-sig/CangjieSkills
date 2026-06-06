## class Color

```cangjie
public class Color <: ResourceColor {
    public static let BLACK: Color = Color(0xff000000)
    public static let BLUE: Color = Color(0xff0000ff)
    public static let BROWN: Color = Color(0xffa52a2a)
    public static let GRAY: Color = Color(0xff808080)
    public static let GREY: Color = Color(0xff808080)
    public static let GREEN: Color = Color(0xff008000)
    public static let ORANGE: Color = Color(0xffffa500)
    public static let PINK: Color = Color(0xffffc0cb)
    public static let RED: Color = Color(0xffff0000)
    public static let WHITE: Color = Color(0xffffffff)
    public static let YELLOW: Color = Color(0xffffff00)
    public static let TRANSPARENT: Color = Color(0, 0, 0, alpha: 0.0)
    public static let FOREGROUND: Color = Color(0x00000001)
    public init(red: UInt8, green: UInt8, blue: UInt8, alpha!: Float32 = 1.0)
    public init(value: UInt32)
}
```

**功能：** 颜色类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [ResourceColor](#interface-resourcecolor)

### static let BLACK

```cangjie
public static let BLACK: Color = Color(0xff000000)
```

**功能：** 黑色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static let BLUE

```cangjie
public static let BLUE: Color = Color(0xff0000ff)
```

**功能：** 蓝色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static let BROWN

```cangjie
public static let BROWN: Color = Color(0xffa52a2a)
```

**功能：** 棕色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static let FOREGROUND

```cangjie
public static let FOREGROUND: Color = Color(0x00000001)
```

**功能：** 前景色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static let GRAY

```cangjie
public static let GRAY: Color = Color(0xff808080)
```

**功能：** 灰色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static let GREEN

```cangjie
public static let GREEN: Color = Color(0xff008000)
```

**功能：** 绿色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static let GREY

```cangjie
public static let GREY: Color = Color(0xff808080)
```

**功能：** 灰色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static let ORANGE

```cangjie
public static let ORANGE: Color = Color(0xffffa500)
```

**功能：** 橙色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static let PINK

```cangjie
public static let PINK: Color = Color(0xffffc0cb)
```

**功能：** 粉色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static let RED

```cangjie
public static let RED: Color = Color(0xffff0000)
```

**功能：** 红色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static let TRANSPARENT

```cangjie
public static let TRANSPARENT: Color = Color(0, 0, 0, alpha: 0.0)
```

**功能：** 透明色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static let WHITE

```cangjie
public static let WHITE: Color = Color(0xffffffff)
```

**功能：** 白色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static let YELLOW

```cangjie
public static let YELLOW: Color = Color(0xffffff00)
```

**功能：** 黄色。

**类型：** [Color](#class-color)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19