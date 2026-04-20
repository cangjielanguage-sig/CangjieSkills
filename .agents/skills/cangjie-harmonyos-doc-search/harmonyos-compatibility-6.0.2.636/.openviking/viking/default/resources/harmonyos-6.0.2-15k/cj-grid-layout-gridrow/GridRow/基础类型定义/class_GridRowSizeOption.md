### class GridRowSizeOption

```cangjie
public class GridRowSizeOption {
    public var xs: Length
    public var sm: Length
    public var md: Length
    public var lg: Length
    public var xl: Length
    public var xxl: Length
    public GridRowSizeOption(
        xs!: Length = 0.vp,
        sm!: Length = 0.vp,
        md!: Length = 0.vp,
        lg!: Length = 0.vp,
        xl!: Length = 0.vp,
        xxl!: Length = 0.vp
    )
}
```

**功能：** 栅格在不同宽度设备类型下，gutter的大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var lg

```cangjie
public var lg: Length
```

**功能：** 大宽度类型设备。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var md

```cangjie
public var md: Length
```

**功能：** 中等宽度类型设备。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var sm

```cangjie
public var sm: Length
```

**功能：** 小宽度类型设备。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var xl

```cangjie
public var xl: Length
```

**功能：** 特大宽度类型设备。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var xs

```cangjie
public var xs: Length
```

**功能：** 最小宽度类型设备。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var xxl

```cangjie
public var xxl: Length
```

**功能：** 超大宽度类型设备。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### GridRowSizeOption(Length, Length, Length, Length, Length, Length)

```cangjie
public GridRowSizeOption(
    xs!: Length = 0.vp,
    sm!: Length = 0.vp,
    md!: Length = 0.vp,
    lg!: Length = 0.vp,
    xl!: Length = 0.vp,
    xxl!: Length = 0.vp
)
```

**功能：** 构造一个GridRowSizeOption对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|类型名|参数类型|必填|默认值|描述|
|:---|:---|:---|:---|:---|
|xs|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 在最小宽度类型设备上，栅格子组件的间距。|
|sm|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 在小宽度类型设备上，栅格子组件的间距。|
|md|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 在中等宽度类型设备上，栅格子组件的间距。|
|lg|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 在大宽度类型设备上，栅格子组件的间距。|
|xl|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 在特大宽度类型设备上，栅格子组件的间距。|
|xxl|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 在超大宽度类型设备上，栅格子组件的间距。|