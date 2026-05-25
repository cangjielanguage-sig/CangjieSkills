### class LocalizedAlignRuleOptions

```cangjie
public class LocalizedAlignRuleOptions {
    public LocalizedAlignRuleOptions (
        public var start!: ?LocalizedHorizontalAlignParam = None,
        public var end!: ?LocalizedHorizontalAlignParam = None,
        public var middle!: ?LocalizedHorizontalAlignParam = None,
        public var top!: ?LocalizedVerticalAlignParam = None,
        public var bottom!: ?LocalizedVerticalAlignParam = None,
        public var center!: ?LocalizedVerticalAlignParam = None,
        public var bias!: ?Bias = None
    )
}
```

**功能：** 指定设置在相对容器中子组件的对齐规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var bias

```cangjie
public var bias: ?Bias = None
```

**功能：** 设置组件在锚点约束下的偏移参数，其值为到左/上侧锚点的距离与锚点间总距离的比值。

**类型：** ?[Bias](#class-bias)

**读写能力：** 可读写

**起始版本：** 19

#### var bottom

```cangjie
public var bottom: ?LocalizedVerticalAlignParam = None
```

**功能：** 设置纵向底部对齐的参数。

**类型：** ?[LocalizedVerticalAlignParam](#class-localizedverticalalignparam)

**读写能力：** 可读写

**起始版本：** 19

#### var center

```cangjie
public var center: ?LocalizedVerticalAlignParam = None
```

**功能：** 设置纵向居中对齐方式的参数。

**类型：** ?[LocalizedVerticalAlignParam](#class-localizedverticalalignparam)

**读写能力：** 可读写

**起始版本：** 19

#### var end

```cangjie
public var end: ?LocalizedHorizontalAlignParam = None
```

**功能：** 设置横向对齐方式的参数，LTR模式时为右对齐，RTL模式时为左对齐。

**类型：** ?[LocalizedHorizontalAlignParam](#class-localizedhorizontalalignparam)

**读写能力：** 可读写

**起始版本：** 19

#### var middle

```cangjie
public var middle: ?LocalizedHorizontalAlignParam = None
```

**功能：** 设置横向居中对齐方式的参数。

**类型：** ?[LocalizedHorizontalAlignParam](#class-localizedhorizontalalignparam)

**读写能力：** 可读写

**起始版本：** 19

#### var start

```cangjie
public var start: ?LocalizedHorizontalAlignParam = None
```

**功能：** 设置横向对齐方式的参数，LTR模式时为左对齐，RTL模式时为右对齐。

**类型：** ?[LocalizedHorizontalAlignParam](#class-localizedhorizontalalignparam)

**读写能力：** 可读写

**起始版本：** 19

#### var top

```cangjie
public var top: ?LocalizedVerticalAlignParam = None
```

**功能：** 设置纵向顶部对齐的参数。

**类型：** ?[LocalizedVerticalAlignParam](#class-localizedverticalalignparam)

**读写能力：** 可读写

**起始版本：** 19