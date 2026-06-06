### class FlexOptions

```cangjie
public class FlexOptions {
    public FlexOptions(
        public var direction!: FlexDirection = FlexDirection.Row,
        public var wrap!: FlexWrap = FlexWrap.NoWrap,
        public var justifyContent!: FlexAlign = FlexAlign.Start,
        public var alignItems!: ItemAlign = ItemAlign.Start,
        public var alignContent!: FlexAlign = FlexAlign.Start,
        public var space!: FlexSpaceOptions = FlexSpaceOptions()
    )
}
```

**功能：** 表示Flex子组件的排列对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var alignContent

```cangjie
public var alignContent: FlexAlign = FlexAlign.Start
```

**功能：** 交叉轴中有额外的空间时，多行内容的对齐方式。仅在wrap为Wrap或WrapReverse下生效。

**类型：** [FlexAlign](cj-common-types.md#enum-flexalign)

**读写能力：** 可读写

**起始版本：** 12

#### var alignItems

```cangjie
public var alignItems: ItemAlign = ItemAlign.Start
```

**功能：** 所有子组件在Flex容器交叉轴上的对齐格式。

**类型：** [ItemAlign](cj-common-types.md#enum-flexalign)

**读写能力：** 可读写

**起始版本：** 12

#### var direction

```cangjie
public var direction: FlexDirection = FlexDirection.Row
```

**功能：** 子组件在Flex容器上排列的方向，即主轴的方向。

**类型：** [FlexDirection](cj-common-types.md#enum-flexdirection)

**读写能力：** 可读写

**起始版本：** 12

#### var justifyContent

```cangjie
public var justifyContent: FlexAlign = FlexAlign.Start
```

**功能：** 所有子组件在Flex容器主轴上的对齐格式。

**类型：** [FlexAlign](cj-common-types.md#enum-flexalign)

**读写能力：** 可读写

**起始版本：** 12

#### var space

```cangjie
public var space: FlexSpaceOptions = FlexSpaceOptions()
```

**功能：** 所有子组件在Flex容器主轴或交叉轴的间距。space为负数、百分比或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。

**类型：** [FlexSpaceOptions](#class-flexspaceoptions)

**读写能力：** 可读写

**起始版本：** 12

#### var wrap

```cangjie
public var wrap: FlexWrap = FlexWrap.NoWrap
```

**功能：** Flex容器是单行/列还是多行/列排列。

**类型：** [FlexWrap](cj-common-types.md#enum-flexwrap)

**读写能力：** 可读写

**起始版本：** 12