### func placeholderFont(Length, FontWeight, FontStyle, String)

```cangjie
public func placeholderFont(
    size!: Length = DEFAULT_SIZE.fp,
    weight!: FontWeight = FontWeight.W400,
    style!: FontStyle = FontStyle.Normal,
    family!: String = ""
): This
```

**功能：** 设置placeHolder的样式，包括字体大小，字体粗细，字体族，字体风格。当前支持'HarmonyOS Sans'字体和[注册自定义字体](./cj-apis-font.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|DEFAULT_SIZE.fp| **命名参数。** placeholder的文本尺寸。Length为Int64、Float64类型时，使用fp单位。支持设置百分比字符串。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.W400| **命名参数。** placeholder字体的目标粗细。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** placeholder字体的目标样式。|
|family|String|否|""| **命名参数。** placeholder字体的样式族。|

### func searchButton(String)

```cangjie
public func searchButton(text: String): This
```

**功能：** 设置搜索框末尾搜索按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|搜索框末尾搜索按钮文本内容。|

### func searchIcon(Length, ResourceColor, String)

```cangjie
public func searchIcon(size!: Length, color!: ResourceColor, src!: String): This
```

**功能：** 设置左侧搜索图标样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 图标尺寸，不支持百分比。<br>浅色模式初始值: 16.vp，深色模式初始值：16.vp。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 图标颜色。<br>浅色模式初始值：0x99000000，深色模式初始值：0x99ffffff。|
|src|String|是|-| **命名参数。** 图标/图片源。<br>初始值：''。|

### func searchIcon(Length, ResourceColor, AppResource)

```cangjie
public func searchIcon(size!: Length, color!: ResourceColor, src!: AppResource): This
```

**功能：** 设置左侧搜索图标样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 图标尺寸，不支持百分比。<br>浅色模式初始值: 16.vp，深色模式初始值：16.vp。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 图标颜色。<br>浅色模式初始值：0x99000000，深色模式初始值：0x99ffffff。|
|src|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 图标/图片源。<br>初始值：''。|

### func selectedBackgroundColor(ResourceColor)

```cangjie
public func selectedBackgroundColor(value: ResourceColor): This
```

**功能：** 设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|文本选中底板颜色。<br>初始值：20%不透明度。|