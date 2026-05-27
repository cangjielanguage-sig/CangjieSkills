# 位置设置

设置组件的对齐方式、布局方向和显示位置。

## func align(Alignment)

```cangjie
public func align(value: Alignment): This
```

**功能：** 设置容器元素绘制区域内的子元素的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Alignment](./cj-common-types.md#enum-alignment)|是|-|容器元素绘制区域内的子元素的对齐方式。<br> 只在Stack、Button、Marquee、StepperItem、Text、TextArea、TextInput、FolderStack、Scroll中生效，其中和文本相关的组件Text、TextArea、TextInput的align结果参考[TextAlign](./cj-common-types.md#enum-textalign)。不支持textAlign属性的组件则无法设置水平方向的文字对齐。<br> 初始值：Alignment.Center。 <br> **说明：**<br>该属性不支持镜像能力。在Stack中该属性与alignContent效果一致，只能设置子组件在容器内的对齐方式。|

## func alignRules(AlignRuleOption)

```cangjie
public func alignRules(value: AlignRuleOption): This
```

**功能：** 指定设置在相对容器中子组件的对齐规则，仅当父容器为[RelativeContainer](./cj-row-column-stack-relativecontainer.md#relativecontainer)时生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AlignRuleOption](#class-alignruleoption)|是|-|指定设置在相对容器中子组件的对齐规则。|

## func alignRules(LocalizedAlignRuleOptions)

```cangjie
public func alignRules(value: LocalizedAlignRuleOptions): This
```

**功能：** 指定设置在相对容器中子组件的对齐规则，仅当父容器为[RelativeContainer](./cj-row-column-stack-relativecontainer.md#relativecontainer)时生效。该方法水平方向上以start和end分别替代原方法的left和right，以便在RTL模式下能镜像显示，建议使用该方法指定设置在相对容器中子组件的对齐规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[LocalizedAlignRuleOptions](#class-localizedalignruleoptions)|是|-|指定设置在相对容器中子组件的对齐规则。|

## func chainMode(Axis, ChainStyle)

```cangjie
public func chainMode(direction: Axis, style: ChainStyle): This
```

**功能：** 指定以该组件为链头所构成的链的参数，仅当父容器为[RelativeContainer](./cj-row-column-stack-relativecontainer.md#relativecontainer)时生效。链头指满足成链规则时链的第一个组件（水平方向从左边起始，镜像语言下从右边起始；竖直方向从上边起始）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|direction|[Axis](./cj-common-types.md#enum-axis)|是|-|链的方向。|
|style|[ChainStyle](#enum-chainstyle)|是|-|链的样式。|

## func direction(Direction)

```cangjie
public open func direction(value: Direction): This
```

**功能：** 设置容器元素内主轴方向上的布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Direction](./cj-common-types.md#enum-direction)|是|-|容器元素内主轴方向上的布局。<br> 属性配置为auto的时候，按照系统语言方向进行布局。该属性在Column组件上不生效。<br> 初始值：Direction.Auto。|