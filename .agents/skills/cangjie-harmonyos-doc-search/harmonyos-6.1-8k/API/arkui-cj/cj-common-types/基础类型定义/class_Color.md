## class Color

```cangjie
public class Color <: ResourceColor {
    public static let Black: Color = Color(0xff000000)
    public static let Blue: Color = Color(0xff0000ff)
    public static let Gray: Color = Color(0xff808080)
    public static let Green: Color = Color(0xff008000)
    public static let Red: Color = Color(0xffff0000)
    public static let White: Color = Color(0xffffffff)
    public static let Transparent: Color = Color(0, 0, 0, alpha: 0.0)
    public init(red: UInt8, green: UInt8, blue: UInt8, alpha!: ?Float32 = None)
    public init(value: UInt32)
}
```

**功能：** 颜色类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [ResourceColor](#interface-resourcecolor)

### static let Black

```cangjie
public static let Black: Color = Color(0xff000000)
```

**功能：** 黑色。

**类型：** [Color](#class-color)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static let Blue

```cangjie
public static let Blue: Color = Color(0xff0000ff)
```

**功能：** 蓝色。

**类型：** [Color](#class-color)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static let Gray

```cangjie
public static let Gray: Color = Color(0xff808080)
```

**功能：** 灰色。

**类型：** [Color](#class-color)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static let Green

```cangjie
public static let Green: Color = Color(0xff008000)
```

**功能：** 绿色。

**类型：** [Color](#class-color)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static let Red

```cangjie
public static let Red: Color = Color(0xffff0000)
```

**功能：** 红色。

**类型：** [Color](#class-color)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static let White

```cangjie
public static let White: Color = Color(0xffffffff)
```

**功能：** 白色。

**类型：** [Color](#class-color)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static let Transparent

```cangjie
public static let Transparent: Color = Color(0, 0, 0, alpha: 0.0)
```

**功能：** 透明色。

**类型：** [Color](#class-color)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(UInt8, UInt8, UInt8, ?Float32)

```cangjie
public init(red: UInt8, green: UInt8, blue: UInt8, alpha!: ?Float32 = None)
```

**功能：** 使用红、绿、蓝和透明度值创建颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|red|UInt8|是|-|RGB中红色通道取值。|
|green|UInt8|是|-|RGB中绿色通道取值。|
|blue|UInt8|是|-|RGB中蓝色通道取值。|
|alpha|?Float32|否|None|**命名参数。** 透明通道取值，取值范围 [0.0-1.0]。|

### init(UInt32)

```cangjie
public init(value: UInt32)
```

**功能：** 使用32位无符号整数值创建颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|UInt32|是|-|Uint32颜色取值。alpha，R，G，B通道按顺序各占输入的8位，若只输入R,G,B三个通道，则alpha通道默认取0xff。|

### func toUInt32()

```cangjie
public func toUInt32(): UInt32
```

**功能：** 转为UInt32颜色取值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|UInt32颜色取值。|