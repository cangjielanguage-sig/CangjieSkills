### func selected(?Int32)

```cangjie
public func selected(value: ?Int32): This
```

**功能：** 设置下拉菜单初始选项的索引，第一项的索引为0。当不设置selected属性或设置异常值时，初始选择值为-1，菜单项不选中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|下拉菜单初始选项的索引。<br>初始值：0。|

### func value(?ResourceStr)

```cangjie
public func value(value: ?ResourceStr): This
```

**功能：** 设置下拉按钮本身的文本内容。当菜单选中时默认会替换为菜单项文本内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|下拉按钮本身的文本内容。文本长度大于列宽时，文本被截断。<br>初始值：""。|

### func font(?FontStyle, ?FontWeight, ?Length, ?ResourceStr)

```cangjie
public func font(
    style!: ?FontStyle = None,
    weight!: ?FontWeight = None,
    size!: ?Length = None,
    family!: ?ResourceStr = None
): This
```

**功能：** 设置下拉按钮本身的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照初始值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None|**命名参数。** 用于指定字体样式。<br>初始值：FontStyle.Normal。|
|weight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 用于指定字体的粗细。<br>初始值：FontWeight.Medium。|
|size|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 指定字号和行高，不支持百分比设置。<br>初始值：16.vp。|
|family|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 指定字体系列。<br>初始值："sans-serif"。|

### func fontColor(?ResourceColor)

```cangjie
public func fontColor(value: ?ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉按钮本身的文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉按钮本身的文本颜色。<br>初始值：@r(sys.color.ohos_id_color_text_primary)混合@r(sys.color.ohos_id_alpha_content_primary)的透明度。|

### func selectedOptionBgColor(?ResourceColor)

```cangjie
public func selectedOptionBgColor(value: ?ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉菜单选中项的背景色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉菜单选中项的背景色。<br>初始值：@r(sys.color.ohos_id_color_component_activated)混合@r(sys.color.ohos_id_alpha_highlight_bg)的透明度。|