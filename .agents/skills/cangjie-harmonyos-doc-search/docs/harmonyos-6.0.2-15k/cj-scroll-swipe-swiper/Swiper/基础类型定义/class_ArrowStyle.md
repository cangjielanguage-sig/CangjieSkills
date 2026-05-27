### class ArrowStyle

```cangjie
public class ArrowStyle {
    public var showBackground: Bool
    public var isSidebarMiddle: Bool
    public var backgroundSize: Length
    public var backgroundColor: UInt32
    public var arrowSize: Length
    public var arrowColor: UInt32
    public init(showBackground!: Bool = false, isSidebarMiddle!: Bool = false, backgroundSize!: Length = 24.vp,
        backgroundColor!: ResourceColor = Color(0x00000000), arrowSize!: Length = 18.vp, arrowColor!: ResourceColor = Color(0x182431))
}
```

**功能：** 左右箭头属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var arrowColor

```cangjie
public var arrowColor: UInt32
```

**功能：** 设置箭头颜色。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var arrowSize

```cangjie
public var arrowSize: Length
```

**功能：** 设置箭头大小。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var backgroundColor

```cangjie
public var backgroundColor: UInt32
```

**功能：** 设置底板颜色。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var backgroundSize

```cangjie
public var backgroundSize: Length
```

**功能：** 设置底板大小。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var isSidebarMiddle

```cangjie
public var isSidebarMiddle: Bool
```

**功能：** 设置箭头显示位置。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var showBackground

```cangjie
public var showBackground: Bool
```

**功能：** 设置箭头底板是否显示。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Bool, Bool, Length, ResourceColor, Length, ResourceColor)

```cangjie
public init(showBackground!: Bool = false, isSidebarMiddle!: Bool = false, backgroundSize!: Length = 24.vp,
    backgroundColor!: ResourceColor = Color(0x00000000), arrowSize!: Length = 18.vp, arrowColor!: ResourceColor = Color(0x182431))
```

**功能：** ArrowStyle的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|showBackground|Bool|否|false| **命名参数。** 设置箭头底板是否显示。为true时箭头底板显示，为false时箭头底板不显示。|
|isSidebarMiddle|Bool|否|false| **命名参数。** 设置箭头显示位置。为true时箭头居中显示在swiper组件两侧，为false时显示在导航点指示器两侧。|
|backgroundSize|[Length](./cj-common-types.md#interface-length)|否|24.vp| **命名参数。** 设置底板大小。不支持设置百分比。|
|backgroundColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0x00000000)| **命名参数。** 设置底板颜色。|
|arrowSize|[Length](./cj-common-types.md#interface-length)|否|18.vp| **命名参数。** 设置箭头大小。不支持设置百分比。<br> **说明：**<br>showBackground为true时，arrowSize为backgroundSize的3/4。|
|arrowColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0x182431)| **命名参数。** 设置箭头颜色。|