#### FlexOptions(FlexDirection, FlexWrap, FlexAlign, ItemAlign, FlexAlign, FlexSpaceOptions)

```cangjie
public FlexOptions(
    public var direction!: FlexDirection = FlexDirection.Row,
    public var wrap!: FlexWrap = FlexWrap.NoWrap,
    public var justifyContent!: FlexAlign = FlexAlign.Start,
    public var alignItems!: ItemAlign = ItemAlign.Start,
    public var alignContent!: FlexAlign = FlexAlign.Start,
    public var space!: FlexSpaceOptions = FlexSpaceOptions()
)
```

**功能：** 创建一个FlexOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 16

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|direction|[FlexDirection](cj-common-types.md#enum-flexdirection)|否|FlexDirection.Row| **命名参数。** 子组件在Flex容器上排列的方向，即主轴的方向。|
|wrap|[FlexWrap](cj-common-types.md#enum-flexwrap)|否|FlexWrap.NoWrap| **命名参数。** Flex容器是单行/列还是多行/列排列。|
|justifyContent|[FlexAlign](cj-common-types.md#enum-flexalign)|否|FlexAlign.Start| **命名参数。** 所有子组件在Flex容器主轴上的对齐格式。|
|alignItems|[ItemAlign](cj-common-types.md#enum-itemalign)|否|ItemAlign.Start| **命名参数。** 所有子组件在Flex容器交叉轴上的对齐格式。|
|alignContent|[FlexAlign](cj-common-types.md#enum-flexalign)|否|FlexAlign.Start| **命名参数。** 交叉轴中有额外的空间时，多行内容的对齐方式。仅在wrap为Wrap或WrapReverse下生效。|
|space|[FlexSpaceOptions](#class-flexspaceoptions)|否|FlexSpaceOptions()| **命名参数。** 所有子组件在Flex容器主轴或交叉轴的间距。space为负数、百分比或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。|