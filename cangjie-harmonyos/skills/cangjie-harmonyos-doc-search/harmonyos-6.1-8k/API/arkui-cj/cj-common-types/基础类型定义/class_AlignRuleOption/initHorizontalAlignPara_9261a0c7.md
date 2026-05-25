### init(?HorizontalAlignParam, ?HorizontalAlignParam, ?HorizontalAlignParam, ?VerticalAlignParam, ?VerticalAlignParam, ?VerticalAlignParam, ?Bias)

```cangjie
public init(left!: ?HorizontalAlignParam = None, right!: ?HorizontalAlignParam = None, middle!: ?HorizontalAlignParam = None, top!: ?VerticalAlignParam = None, bottom!: ?VerticalAlignParam = None, center!: ?VerticalAlignParam = None, bias!: ?Bias = None)
```

**功能：** 构造一个AlignRuleOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|?[HorizontalAlignParam](#class-horizontalalignparam)|否|None|**命名参数。** 设置组件左侧对齐方式。|
|right|?[HorizontalAlignParam](#class-horizontalalignparam)|否|None|**命名参数。** 设置组件右侧对齐方式。|
|middle|?[HorizontalAlignParam](#class-horizontalalignparam)|否|None|**命名参数。** 设置组件水平居中对齐方式。|
|top|?[VerticalAlignParam](#class-verticalalignparam)|否|None|**命名参数。** 设置组件顶部对齐方式。|
|bottom|?[VerticalAlignParam](#class-verticalalignparam)|否|None|**命名参数。** 设置组件顶部对齐方式。|
|center|?[VerticalAlignParam](#class-verticalalignparam)|否|None|**命名参数。** 设置组件垂直居中对齐方式。|
|bias|?[Bias](#class-bias)|否|None|**命名参数。** 设置组件对齐的偏移量。初始值为Bias()。|