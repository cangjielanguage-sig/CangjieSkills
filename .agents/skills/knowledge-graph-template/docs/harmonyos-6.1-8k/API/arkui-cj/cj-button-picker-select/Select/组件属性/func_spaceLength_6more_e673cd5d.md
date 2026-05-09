### func space(?Length)

```cangjie
public func space(value: ?Length): This
```

**功能：** 根据指定的Length类型值，设置下拉菜单项的文本与箭头之间的间距。不支持设置百分比。设置为小于等于8的值，取初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|下拉菜单项的文本与箭头之间的间距。<br>初始值：8.0.vp。|

### func arrowPosition(?ArrowPosition)

```cangjie
public func arrowPosition(value: ?ArrowPosition): This
```

**功能：** 设置下拉菜单项的文本与箭头之间的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ArrowPosition](./cj-common-types.md#enum-arrowposition)|是|-|下拉菜单项的文本与箭头之间的对齐方式。<br>初始值：ArrowPosition.End。|

### func menuAlign(?MenuAlignType, ?Offset)

```cangjie
public func menuAlign(alignType!: ?MenuAlignType, offset!: ?Offset): This
```

**功能：** 设置下拉按钮与下拉菜单间的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alignType|?[MenuAlignType](./cj-common-types.md#enum-menualigntype)|是|-|**命名参数。** 对齐方式类型。<br>初始值：MenuAlignType.Start。|
|offset|?[Offset](./cj-common-types.md#class-offset)|是|-|**命名参数。** 按照对齐类型对齐后，下拉菜单相对下拉按钮的偏移量。<br>初始值：Offset(0.0.vp, 0.0.vp)。|

### func optionWidth(?OptionWidthMode)

```cangjie
public func optionWidth(value: ?OptionWidthMode): This
```

**功能：** 设置下拉菜单项的宽度。OptionWidthMode类型为枚举类型，OptionWidthMode决定下拉菜单是否继承下拉按钮宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[OptionWidthMode](./cj-common-types.md#enum-optionwidthmode)|是|-|下拉菜单项的宽度。|

### func optionWidth(?Length)

```cangjie
public func optionWidth(value: ?Length): This
```

**功能：** 根据指定的Length类型值，设置下拉菜单项的宽度，不支持设置百分比。

当设置为异常值或小于最小宽度56.vp时，属性不生效，菜单项宽度设为初始值，即菜单初始宽度为2栅格。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|下拉菜单项的宽度。|

### func optionHeight(?Length)

```cangjie
public func optionHeight(value: ?Length): This
```

**功能：** 根据指定的Length类型值，设置下拉菜单显示的最大高度。下拉菜单的初始最大高度是屏幕可用高度的80%，设置的菜单最大高度不能超过初始最大高度。

当设置为负数与零时，属性不生效，下拉菜单最大高度设为初始值，即下拉菜单最大高度默认值为屏幕可用高度的80%。

正常值范围大于0。如果下拉菜单所有选项的实际高度没有设定的高度大，下拉菜单的高度按实际高度显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|下拉菜单显示的最大高度。|