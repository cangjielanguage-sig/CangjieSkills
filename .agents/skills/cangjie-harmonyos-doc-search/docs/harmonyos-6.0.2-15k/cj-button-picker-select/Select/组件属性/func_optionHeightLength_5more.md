### func optionHeight(Length)

```cangjie
public func optionHeight(value: Length): This
```

**功能：** 根据指定的Length类型值，设置下拉菜单显示的最大高度。下拉菜单的初始最大高度是屏幕可用高度的80%，设置的菜单最大高度不能超过初始最大高度。

当设置为负数与零时，属性不生效，下拉菜单最大高度设为初始值，即下拉菜单最大高度默认值为屏幕可用高度的80%。

正常值范围大于0。如果下拉菜单所有选项的实际高度没有设定的高度大，下拉菜单的高度按实际高度显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|下拉菜单显示的最大高度。|

### func optionWidth(OptionWidthMode)

```cangjie
public func optionWidth(value: OptionWidthMode ): This
```

**功能：** 设置下拉菜单项的宽度。OptionWidthMode类型为枚举类型，OptionWidthMode决定下拉菜单是否继承下拉按钮宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[OptionWidthMode](./cj-common-types.md#enum-optionwidthmode)|是|-|下拉菜单项的宽度。|

### func optionWidth(Length)

```cangjie
public func optionWidth(value: Length): This
```

**功能：** 根据指定的Length类型值，设置下拉菜单项的宽度，不支持设置百分比。

当设置为异常值或小于最小宽度56.vp时，属性不生效，菜单项宽度设为初始值，即菜单初始宽度为2栅格。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md)|是|-|下拉菜单项的宽度。|

### func selected(Int32)

```cangjie
public func selected(value: Int32): This
```

**功能：** 设置下拉菜单初始选项的索引，第一项的索引为0。当不设置selected属性或设置异常值时，初始选择值为-1，菜单项不选中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|下拉菜单初始选项的索引。|

### func selectedOptionBgColor(ResourceColor)

```cangjie
public func selectedOptionBgColor(value: ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉菜单选中项的背景色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉菜单选中项的背景色。<br> 初始值：@r(sys.color.ohos_id_color_component_activated)混合@r(sys.color.ohos_id_alpha_highlight_bg)的透明度。|