### func fontColor(ResourceColor)

```cangjie
public func fontColor(value: ResourceColor): This
```

**功能：** 设置字体颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|字体颜色。|

### func fontFamily(String)

```cangjie
public func fontFamily(value: String): This
```

**功能：** 设置字体列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|字体列表。<br/>初始字体：'HarmonyOS Sans'。<br/>应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](cj-apis-font.md)。|

### func fontFamily(AppResource)

```cangjie
public func fontFamily(content: AppResource): This
```

**功能：** 设置字体列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|字体列表。<br/>初始字体：'HarmonyOS Sans'。<br/>应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](cj-apis-font.md)。|

### func fontSize(Length)

```cangjie
public func fontSize(value: Length): This
```

**功能：** 设置字体大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|字体大小。fontSize为Int64、Float64类型时，使用fp单位。字体初始大小16.fp。不支持设置百分比。|

### func fontStyle(FontStyle)

```cangjie
public func fontStyle(value: FontStyle): This
```

**功能：** 设置字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontStyle](./cj-common-types.md#enum-fontstyle)|是|-|字体样式。<br/>初始值：FontStyle.Normal|

### func fontWeight(FontWeight)

```cangjie
public func fontWeight(value: FontWeight): This
```

**功能：** 设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontWeight](./cj-common-types.md#enum-fontweight)|是|-|文本的字体粗细。<br/>初始值：FontWeight.Normal|

### func format(String)

```cangjie
public func format(value: String): This
```

**功能：** 设置自定义格式，需至少包含一个HH、mm、ss、SS中的关键字。如使用yy、MM、dd等日期格式，则使用默认值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|自定义格式。<br/>初始值：'HH:mm:ss.SS'|

### func textShadow(Array\<ShadowOptions>)

```cangjie
public func textShadow(values: Array<ShadowOptions>): This
```

**功能：** 设置文字阴影效果。该接口支持以数组形式入参，实现多重文字阴影。不支持fill字段, 不支持智能取色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|values|Array\<[ShadowOptions](./cj-text-input-text.md#class-shadowoptions)>|是|-|文字阴影效果。|