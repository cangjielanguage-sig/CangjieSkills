### func selectedOptionFont(?FontStyle, ?FontWeight, ?Length, ?String)

```cangjie
public func selectedOptionFont(
    style!: ?FontStyle = None,
    weight!: ?FontWeight = None,
    size!: ?Length = None,
    family!: ?String = None
): This
```

**功能：** 设置下拉菜单选中项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照初始值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None|**命名参数。** 用于指定字体样式。<br>初始值：FontStyle.Normal。|
|weight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 用于指定字体的粗细。<br>初始值：FontWeight.Medium。|
|size|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 文本尺寸。不支持百分比设置。<br>初始值：16.vp。|
|family|?String|否|None|**命名参数。** 指定字体列表。<br>初始值："sans-serif"。|

### func selectedOptionFontColor(?ResourceColor)

```cangjie
public func selectedOptionFontColor(value: ?ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉菜单选中项的文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉菜单选中项的文本颜色。<br>初始值：@r(sys.color.ohos_id_color_text_primary_activated)|

### func optionBgColor(?ResourceColor)

```cangjie
public func optionBgColor(value: ?ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉菜单项的背景色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉菜单项的背景色。<br>初始值：Color.Transparent。|

### func optionFont(?FontStyle, ?FontWeight, ?Length, ?ResourceStr)

```cangjie
public func optionFont(
    style!: ?FontStyle = None,
    weight!: ?FontWeight = None,
    size!: ?Length = None,
    family!: ?ResourceStr = None
): This
```

**功能：** 设置下拉菜单项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照初始值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None|**命名参数。** 用于指定字体样式。<br>初始值：FontStyle.Normal。|
|weight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 用于指定字体的粗细。<br>初始值：FontWeight.Medium。|
|size|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 指定字号和行高，不支持百分比设置。<br>初始值：16.vp。|
|family|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 指定字体系列。<br>初始值："sans-serif"。|

### func optionFontColor(?ResourceColor)

```cangjie
public func optionFontColor(value: ?ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉菜单项的文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉菜单项的文本颜色。<br>初始值：@r(sys.color.ohos_id_color_text_primary)。|