### func passwordIcon(?AppResource, ?AppResource)

```cangjie
public func passwordIcon(onIconSrc!: ?AppResource = None, offIconSrc!: ?AppResource = None): This
```

**功能：** 设置当密码输入模式时，输入框末尾的图标。

> **说明：**
>
> - 支持jpg、png、bmp、heic和webp类型的图片格式。
> - 该图标的固定尺寸为24vp，若引用的图标过大或过小，均显示为固定尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onIconSrc|?[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|否|None| **命名参数。** 密码输入模式时，能够切换密码隐藏的显示状态的图标。默认为系统提供的密码图标。|
|offIconSrc|?[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|否|None| **命名参数。** 密码输入模式时，能够切换密码显示的隐藏状态的图标。默认为系统提供的密码图标。|

### func passwordRules(String)

```cangjie
public func passwordRules(value: String): This
```

**功能：** 定义生成密码的规则。

> **说明：**
>
> 在触发自动填充时，所设置的密码规则会透传给密码保险箱，用于新密码的生成。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|定义生成密码的规则。|

### func placeholderColor(ResourceColor)

```cangjie
public func placeholderColor(value: ResourceColor): This
```

**功能：** 设置placeholder文本颜色。InputType设置为Password后，设置placeholderColor不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|placeholder文本颜色。<br>初始值：跟随主题。|

### func placeholderFont(Length, FontWeight, String, FontStyle)

```cangjie
public func placeholderFont(size!: Length, weight!: FontWeight = FontWeight.W400, family!: String = "", style!: FontStyle = FontStyle.Normal): This
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

### func selectAll(Bool)

```cangjie
public func selectAll(value: Bool): This
```

**功能：** 设置当初始状态，是否全选文本。不支持内联模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否全选文本。<br>初始值：false。|

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