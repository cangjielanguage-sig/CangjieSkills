### class FontOptions

```cangjie
public class FontOptions {
    public var size: Length
    public var weight: FontWeight
    public init(size!: Length = 14.vp, weight!: FontWeight = FontWeight.Normal)
}
```

**功能：** Swiper组件数字导航点的字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var size

```cangjie
public var size: Length
```

**功能：** 数字导航点指示器的字体大小，不支持设置百分比。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var weight

```cangjie
public var weight: FontWeight
```

**功能：** 数字导航点选中指示器的字体粗细。

**类型：** [FontWeight](./cj-common-types.md#enum-fontweight)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Length, FontWeight)

```cangjie
public init(size!: Length = 14.vp, weight!: FontWeight = FontWeight.Normal)
```

**功能：** FontOptions的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|14.vp| **命名参数。** 数字导航点指示器的字体大小，不支持设置百分比。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 数字导航点选中指示器的字体粗细。|