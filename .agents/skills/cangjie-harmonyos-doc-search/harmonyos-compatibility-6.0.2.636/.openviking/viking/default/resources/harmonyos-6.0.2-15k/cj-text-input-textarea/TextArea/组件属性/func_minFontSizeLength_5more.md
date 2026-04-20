### func minFontSize(Length)

```cangjie
public func minFontSize(value: Length): This
```

**功能：** 设置文本最小显示字号。

> **说明：**
>
> - 需配合[maxFontSize](#func-maxfontsizelength)以及[maxLines](#func-maxlinesint32)或布局大小限制使用，单独设置不生效。
> - 自适应字号生效时，fontSize设置不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|文本最小显示字号。单位：fp。|

### func placeholderColor(ResourceColor)

```cangjie
public func placeholderColor(value: ResourceColor): This
```

**功能：** 设置placeholder文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|placeholder文本颜色。<br>初始值：跟随主题。|

### func placeholderFont(Length, FontWeight, String, FontStyle)

```cangjie
public func placeholderFont(size!: Length, weight!: FontWeight = FontWeight.W400, family!: String = "",
    style!: FontStyle = FontStyle.Normal): This
```

**功能：** 设置placeholder文本样式，包括字体大小，字体粗细，字体族，字体风格。当前支持'HarmonyOS Sans'字体和[注册自定义字体](./cj-apis-font.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 文本尺寸。 单位：fp。<br>初始值：16.fp。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.W400| **命名参数。** 文本的字体粗细。|
|family|String|否|""| **命名参数。** 文本的字体列表。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 文本的字体样式。|

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

### func selectionMenuHidden(Bool)

```cangjie
public func selectionMenuHidden(value: Bool): This
```

**功能：** 设置是否不弹出系统文本选择菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否不弹出系统文本选择菜单。<br/>设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，不弹出系统文本选择菜单。<br/>设置为false时，弹出系统文本选择菜单。<br>初始值：false。|