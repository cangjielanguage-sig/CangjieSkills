### func menuAlign(MenuAlignType, MenuOffset)

```cangjie
public func menuAlign(alignType: MenuAlignType, offset!: MenuOffset): This
```

**功能：** 设置下拉按钮与下拉菜单间的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alignType|[MenuAlignType](#enum-menualigntype)|是|-|对齐方式类型。<br/>初始值：MenuAlignType.START。|
|offset|[MenuOffset](./cj-common-types.md#class-menuoffset)|是|-| **命名参数。** 按照对齐类型对齐后，下拉菜单相对下拉按钮的偏移量。<br>初始值：MenuOffset(0, 0)。|

### func menuBackgroundBlurStyle(BlurStyle)

```cangjie
public func menuBackgroundBlurStyle(value: BlurStyle): This
```

**功能：** 设置下拉菜单的背景模糊材质。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)|是|-|下拉菜单的背景模糊材质。<br/>初始值：BlurStyle.COMPONENT_ULTRA_THICK。|

### func menuBackgroundColor(ResourceColor)

```cangjie
public func menuBackgroundColor(value: ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉菜单的背景色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉菜单的背景色。<br>初始值：Color.TRANSPARENT。|

### func optionBgColor(ResourceColor)

```cangjie
public func optionBgColor(value: ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉菜单项的背景色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉菜单项的背景色。<br>初始值：Color.TRANSPARENT。|

### func optionFont(FontStyle, FontWeight, Length, String)

```cangjie
public func optionFont(
    style!: FontStyle = FontStyle.Normal,
    weight!: FontWeight = FontWeight.Medium,
    size!: Length = 16.vp,
    family!: String = "sans-serif"
): This
```

**功能：** 设置下拉菜单项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照初始值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 用于指定字体样式。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Medium| **命名参数。** 用于指定字体的粗细。|
|size|[Length](./cj-common-types.md#enum-lengthtype)|否|16.vp| **命名参数。** 指定字号和行高，不支持百分比设置。|
|family|String|否|"sans-serif"| **命名参数。** 指定字体系列。|

### func optionFontColor(ResourceColor)

```cangjie
public func optionFontColor(value: ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉菜单项的文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉菜单项的文本颜色。<br>初始值：@r(sys.color.ohos_id_color_text_primary)。|