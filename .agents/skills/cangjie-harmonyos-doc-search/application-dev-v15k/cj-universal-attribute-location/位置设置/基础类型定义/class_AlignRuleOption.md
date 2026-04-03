### class AlignRuleOption

```cangjie
public class AlignRuleOption {
    public AlignRuleOption (
        public var left!: ?HorizontalAnchor = None,
        public var right!: ?HorizontalAnchor = None,
        public var middle!: ?HorizontalAnchor = None,
        public var top!: ?VerticalAnchor = None,
        public var bottom!: ?VerticalAnchor = None,
        public var center!: ?VerticalAnchor = None,
        public var bias!: ?Bias = None
    )
}
```

**功能：** 指定设置在相对容器中子组件的对齐规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var bias

```cangjie
public var bias: ?Bias = None
```

**功能：** 设置组件在锚点约束下的偏移参数，其值为到左/上侧锚点的距离与锚点间总距离的比值。

**类型：** ?[Bias](#class-bias)

**读写能力：** 可读写

**起始版本：** 12

#### var bottom

```cangjie
public var bottom: ?VerticalAnchor = None
```

**功能：** 设置底部对齐的参数。

**类型：** ?[VerticalAnchor](#class-verticalanchor)

**读写能力：** 可读写

**起始版本：** 12

#### var center

```cangjie
public var center: ?VerticalAnchor = None
```

**功能：** 设置纵向居中对齐方式的参数。

**类型：** ?[VerticalAnchor](#class-verticalanchor)

**读写能力：** 可读写

**起始版本：** 12

#### var left

```cangjie
public var left: ?HorizontalAnchor = None
```

**功能：** 设置左对齐参数。

**类型：** ?[HorizontalAnchor](#class-horizontalanchor)

**读写能力：** 可读写

**起始版本：** 12

#### var middle

```cangjie
public var middle: ?HorizontalAnchor = None
```

**功能：** 设置横向居中对齐方式的参数。

**类型：** ?[HorizontalAnchor](#class-horizontalanchor)

**读写能力：** 可读写

**起始版本：** 12

#### var right

```cangjie
public var right: ?HorizontalAnchor = None
```

**功能：** 设置右对齐参数。

**类型：** ?[HorizontalAnchor](#class-horizontalanchor)

**读写能力：** 可读写

**起始版本：** 12

#### var top

```cangjie
public var top: ?VerticalAnchor = None
```

**功能：** 设置顶部对齐的参数。

**类型：** ?[VerticalAnchor](#class-verticalanchor)

**读写能力：** 可读写

**起始版本：** 12

#### AlignRuleOption(?HorizontalAnchor, ?HorizontalAnchor, ?HorizontalAnchor, ?VerticalAnchor, ?VerticalAnchor, ?VerticalAnchor, ?Bias)

```cangjie
public AlignRuleOption (
    public var left!: ?HorizontalAnchor = None,
    public var right!: ?HorizontalAnchor = None,
    public var middle!: ?HorizontalAnchor = None,
    public var top!: ?VerticalAnchor = None,
    public var bottom!: ?VerticalAnchor = None,
    public var center!: ?VerticalAnchor = None,
    public var bias!: ?Bias = None
)
```

**功能：** 创建一个 AlignRuleOption 类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|?[HorizontalAnchor](#class-horizontalanchor)|否|None| **命名参数。** 设置左对齐参数。|
|right|?[HorizontalAnchor](#class-horizontalanchor)|否|None| **命名参数。** 设置右对齐参数。|
|middle|?[HorizontalAnchor](#class-horizontalanchor)|否|None| **命名参数。** 设置横向居中对齐方式的参数。|
|top|?[VerticalAnchor](#class-verticalanchor)|否|None| **命名参数。** 设置顶部对齐的参数。|
|bottom|?[VerticalAnchor](#class-verticalanchor)|否|None| **命名参数。** 设置底部对齐的参数。|
|center|?[VerticalAnchor](#class-verticalanchor)|否|None| **命名参数。** 设置纵向居中对齐方式的参数。|
|bias|?[Bias](#class-bias)|否|None| **命名参数。** 设置组件在锚点约束下的偏移参数，其值为到左/上侧锚点的距离与锚点间总距离的比值。|