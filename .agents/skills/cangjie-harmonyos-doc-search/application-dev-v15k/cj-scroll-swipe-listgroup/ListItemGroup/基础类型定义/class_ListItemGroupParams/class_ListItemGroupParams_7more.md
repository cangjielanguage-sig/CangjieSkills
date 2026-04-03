### class ListItemGroupParams

```cangjie
public class ListItemGroupParams {
    public let header:() -> Unit
    public let footer:() -> Unit
    public let space: Length
    public var style: ListItemGroupStyle
    public init(
        header!: () -> Unit = { => }, footer!: () -> Unit = { => }, space!: Length
    )
    public init(
        header!: () -> Unit = { => },
        footer!: () -> Unit = { => }
    )
    public init(header!: () -> Unit = { => }, footer!: () -> Unit = { => }, space!: Length, style!: ListItemGroupStyle)
}
```

**功能：** 列表item分组组件参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var style

```cangjie
public var style: ListItemGroupStyle
```

**功能：** 设置List组件卡片样式。

**类型：** [ListItemGroupStyle](#enum-listitemgroupstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let footer

```cangjie
public let footer:() -> Unit
```

**功能：** 设置ListItemGroup尾部组件。

**类型：** ()->Unit

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let header

```cangjie
public let header:() -> Unit
```

**功能：** 设置ListItemGroup头部组件，函数需要用@Builder装饰器修饰，函数中组件代码会显示在ListItemGroup的头部。

**类型：** ()->Unit

**读写能力：** 只读

**起始版本：** 12

#### let space

```cangjie
public let space: Length
```

**功能：** 列表项间距。列表项之间会有一定的初始高度，当设置了space后，列表项间距为初始高度加上space设置的高度。

**类型：** [Length](cj-common-types.md#interface-Length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(() -> Unit, () -> Unit, Length)

```cangjie
public init(
    header!: () -> Unit = { => }, footer!: () -> Unit = { => }, space!: Length
)
```

**功能：** 创建ListItemGroupParams对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|header|()->Unit|否|{ => }| **命名参数。** 设置ListItemGroup头部组件。<br/>**说明：**<br/>可以放单个子组件或不放子组件。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|
|footer|()->Unit|否|{ => }| **命名参数。** 设置ListItemGroup尾部组件。<br/>**说明：**<br/>可以放单个子组件或不放子组件。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|
|space|[Length](cj-common-types.md#interface-Length)|是|-| **命名参数。** 列表项间距。只作用于ListItem与ListItem之间，不作用于header与ListItem、footer与ListItem之间。<br/>初始值：0。<br/>单位：vp。<br/>**说明：**<br/>设置为负数或者大于等于List内容区长度时，按初始值显示。|

#### init(() -> Unit, () -> Unit)

```cangjie
public init(
    header!: () -> Unit = { => },
    footer!: () -> Unit = { => }
)
```

**功能：** 创建ListItemGroupParams对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|header|()->Unit|否|{ => }| **命名参数。** 设置ListItemGroup头部组件。<br/>可以放单个子组件或不放子组件。|
|footer|()->Unit|否|{ => }| **命名参数。** 设置ListItemGroup尾部组件。<br/>可以放单个子组件或不放子组件。|