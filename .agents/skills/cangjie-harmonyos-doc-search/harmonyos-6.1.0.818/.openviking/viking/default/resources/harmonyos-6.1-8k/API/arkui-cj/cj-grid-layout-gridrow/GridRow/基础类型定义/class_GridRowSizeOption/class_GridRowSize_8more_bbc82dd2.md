### class GridRowSizeOption

```cangjie
public class GridRowSizeOption {
    public var xs: ?Length
    public var sm: ?Length
    public var md: ?Length
    public var lg: ?Length
    public var xl: ?Length
    public var xxl: ?Length
    public init(
        xs!: ?Length = None,
        sm!: ?Length = None,
        md!: ?Length = None,
        lg!: ?Length = None,
        xl!: ?Length = None,
        xxl!: ?Length = None
    )
    public init(value: ?Length)
}
```

**功能：** 栅格在不同宽度设备类型下，gutter的大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var lg

```cangjie
public var lg: ?Length
```

**功能：** 大宽度类型设备。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var md

```cangjie
public var md: ?Length
```

**功能：** 中等宽度类型设备。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var sm

```cangjie
public var sm: ?Length
```

**功能：** 小宽度类型设备。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var xl

```cangjie
public var xl: ?Length
```

**功能：** 特大宽度类型设备。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var xs

```cangjie
public var xs: ?Length
```

**功能：** 最小宽度类型设备。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var xxl

```cangjie
public var xxl: ?Length
```

**功能：** 超大宽度类型设备。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Length, ?Length, ?Length, ?Length, ?Length, ?Length)

```cangjie
public init(
    xs!: ?Length = None,
    sm!: ?Length = None,
    md!: ?Length = None,
    lg!: ?Length = None,
    xl!: ?Length = None,
    xxl!: ?Length = None
)
```

**功能：** 构造一个GridRowSizeOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xs|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 在栅格大小为xs的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：0.vp|
|sm|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 在栅格大小为sm的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：0.vp|
|md|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 在栅格大小为md的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：0.vp|
|lg|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 在栅格大小为lg的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：0.vp|
|xl|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 在栅格大小为xl的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：0.vp|
|xxl|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 在栅格大小为xxl的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：0.vp|