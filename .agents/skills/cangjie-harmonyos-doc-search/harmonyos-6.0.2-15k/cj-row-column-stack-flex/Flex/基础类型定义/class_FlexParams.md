### class FlexParams

```cangjie
public class FlexParams {
    public FlexParams(
        public var direction!: FlexDirection = FlexDirection.Row,
        public var wrap!: FlexWrap = FlexWrap.NoWrap,
        public var justifyContent!: FlexAlign = FlexAlign.Start,
        public var alignItems!: ItemAlign = ItemAlign.Start,
        public var alignContent!: FlexAlign = FlexAlign.Start
    )
}
```

**功能：** 表示Flex子组件的排列对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var alignContent

```cangjie
public var alignContent: FlexAlign = FlexAlign.Start
```

**功能：** 交叉轴中有额外的空间时，多行内容的对齐方式。仅在wrap为Wrap或WrapReverse下生效。

**类型：** [FlexAlign](cj-common-types.md#enum-flexalign)

**读写能力：** 可读写

**起始版本：** 19

#### var alignItems

```cangjie
public var alignItems: ItemAlign = ItemAlign.Start
```

**功能：** 子组件在Flex容器交叉轴上的对齐格式。

**类型：** [ItemAlign](cj-common-types.md#enum-itemalign)

**读写能力：** 可读写

**起始版本：** 19

#### var direction

```cangjie
public var direction: FlexDirection = FlexDirection.Row
```

**功能：** 子组件在Flex容器上排列的方向，即主轴的方向。

**类型：** [FlexDirection](cj-common-types.md#enum-flexdirection)

**读写能力：** 可读写

**起始版本：** 19

#### var justifyContent

```cangjie
public var justifyContent: FlexAlign = FlexAlign.Start
```

**功能：** 子组件在Flex容器主轴上的对齐格式。

**类型：** [FlexAlign](cj-common-types.md#enum-flexalign)

**读写能力：** 可读写

**起始版本：** 19

#### var wrap

```cangjie
public var wrap: FlexWrap = FlexWrap.NoWrap
```

**功能：** Flex容器是单行/列还是多行/列排列。

**类型：** [FlexWrap](cj-common-types.md#enum-flexwrap)

**读写能力：** 可读写

**起始版本：** 19

#### FlexParams(FlexDirection, FlexWrap, FlexAlign, ItemAlign, FlexAlign)

```cangjie
public FlexParams(
    public var direction!: FlexDirection = FlexDirection.Row,
    public var wrap!: FlexWrap = FlexWrap.NoWrap,
    public var justifyContent!: FlexAlign = FlexAlign.Start,
    public var alignItems!: ItemAlign = ItemAlign.Start,
    public var alignContent!: FlexAlign = FlexAlign.Start
)
```

**功能：** 创建一个FlexParams类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|direction|[FlexDirection](cj-common-types.md#enum-flexdirection)|否|FlexDirection.Row| **命名参数。** 子组件在Flex容器上排列的方向，即主轴的方向。|
|wrap|[FlexWrap](cj-common-types.md#enum-flexwrap)|否|FlexWrap.NoWrap| **命名参数。** Flex容器是单行/列还是多行/列排列。|
|justifyContent|[FlexAlign](cj-common-types.md#enum-flexalign)|否|FlexAlign.Start| **命名参数。** 子组件在Flex容器主轴上的对齐格式。|
|alignItems|[ItemAlign](cj-common-types.md#enum-itemalign)|否|ItemAlign.Start| **命名参数。** 子组件在Flex容器交叉轴上的对齐格式。|
|alignContent|[FlexAlign](cj-common-types.md#enum-flexalign)|否|FlexAlign.Start| **命名参数。** 交叉轴中有额外的空间时，多行内容的对齐方式。仅在wrap为Wrap或WrapReverse下生效。|