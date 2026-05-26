### func selectedOptionFont(FontStyle, FontWeight, Length, String)

```cangjie
public func selectedOptionFont(
    style!: FontStyle = FontStyle.Normal,
    weight!: FontWeight = FontWeight.Medium,
    size!: Length = 16.vp,
    family!: String = "sans-serif"
): This
```

**功能：** 设置下拉菜单选中项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照初始值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 用于指定字体样式。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Medium| **命名参数。** 用于指定字体的粗细。|
|size|[Length](./cj-common-types.md#interface-length)|否|16.vp| **命名参数。** 文本尺寸。不支持百分比设置。|
|family|String|否|"sans-serif"| **命名参数。** 指定字体列表。|

### func selectedOptionFontColor(ResourceColor)

```cangjie
public func selectedOptionFontColor(value: ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉菜单选中项的文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉菜单选中项的文本颜色。<br>初始值：@r(sys.color.ohos_id_color_text_primary_activated)|

### func space(Length)

```cangjie
public func space(value: Length): This
```

**功能：** 根据指定的Length类型值，设置下拉菜单项的文本与箭头之间的间距。不支持设置百分比。设置为小于等于8的值，取初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|下拉菜单项的文本与箭头之间的间距。<br>初始值：8|

### func value(String)

```cangjie
public func value(content: String): This
```

**功能：** 设置下拉按钮本身的文本内容。当菜单选中时默认会替换为菜单项文本内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|是|-|下拉按钮本身的文本内容。文本长度大于列宽时，文本被截断。|

### func value(AppResource)

```cangjie
public func value(content: AppResource): This
```

**功能：** 设置下拉按钮本身的文本内容。当菜单选中时默认会替换为菜单项文本内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|下拉按钮本身的文本内容。文本长度大于列宽时，文本被截断。|