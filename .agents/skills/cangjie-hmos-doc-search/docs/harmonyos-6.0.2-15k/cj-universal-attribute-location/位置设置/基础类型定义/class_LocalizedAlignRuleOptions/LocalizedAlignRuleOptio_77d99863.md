#### LocalizedAlignRuleOptions(?LocalizedHorizontalAlignParam, ?LocalizedHorizontalAlignParam, ?LocalizedHorizontalAlignParam, ?LocalizedVerticalAlignParam, ?LocalizedVerticalAlignParam, ?LocalizedVerticalAlignParam, ?Bias)

```cangjie
public LocalizedAlignRuleOptions (
    public var start!: ?LocalizedHorizontalAlignParam = None,
    public var end!: ?LocalizedHorizontalAlignParam = None,
    public var middle!: ?LocalizedHorizontalAlignParam = None,
    public var top!: ?LocalizedVerticalAlignParam = None,
    public var bottom!: ?LocalizedVerticalAlignParam = None,
    public var center!: ?LocalizedVerticalAlignParam = None,
    public var bias!: ?Bias = None
)
```

**功能：** 创建一个LocalizedAlignRuleOptions对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|?[LocalizedHorizontalAlignParam](#class-localizedhorizontalalignparam)|否|None| **命名参数。** 横向对齐方式的参数，LTR模式时为左对齐，RTL模式时为右对齐。|
|end|?[LocalizedHorizontalAlignParam](#class-localizedhorizontalalignparam)|否|None| **命名参数。** 横向对齐方式的参数，LTR模式时为右对齐，RTL模式时为左对齐。|
|middle|?[LocalizedHorizontalAlignParam](#class-localizedhorizontalalignparam)|否|None| **命名参数。** 横向居中对齐方式的参数。|
|top|?[LocalizedVerticalAlignParam](#class-localizedverticalalignparam)|否|None| **命名参数。** 纵向顶部对齐的参数。|
|bottom|?[LocalizedVerticalAlignParam](#class-localizedverticalalignparam)|否|None| **命名参数。** 纵向底部对齐的参数。|
|center|?[LocalizedVerticalAlignParam](#class-localizedverticalalignparam)|否|None| **命名参数。** 纵向居中对齐方式的参数。|
|bias|?[Bias](#class-bias)|否|None| **命名参数。** 组件在锚点约束下的偏移参数，其值为到左/上侧锚点的距离与锚点间总距离的比值。|