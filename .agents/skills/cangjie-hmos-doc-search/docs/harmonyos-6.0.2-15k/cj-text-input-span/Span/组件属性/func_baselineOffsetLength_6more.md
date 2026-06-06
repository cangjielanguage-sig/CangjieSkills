### func baselineOffset(Length)

```cangjie
public func baselineOffset(value: Length): This
```

**功能：** 设置Span基线的偏移量。此属性与父组件的baselineOffset是共存的。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|Span基线的偏移量，正数内容向上偏移，负数向下偏移。设置该值为百分比时，按初始值显示。在ImageSpan中，设置为非0时会导致设置verticalAlign失效。<br>初始值：0。<br>在ImageSpan中，设置为非0时会导致设置verticalAlign失效。|

### func decoration(TextDecorationType, ResourceColor)

```cangjie
public func decoration(decorationType!: TextDecorationType, color!: ResourceColor = Color.BLACK): This
```

**功能：** 设置文本装饰线样式及其颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|decorationType|[TextDecorationType](./cj-common-types.md#enum-textdecorationtype)|是|-| **命名参数。** 文本装饰线样式。<br>初始值：TextDecorationType.None。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.BLACK| **命名参数。** 文本装饰线颜色。|

### func font(Length, FontWeight, String, FontStyle)

```cangjie
public func font(size!: Length, weight!: FontWeight,
 family!: String, style!: FontStyle): This
```

**功能：** 设置文本样式。包括字体大小、字体粗细、字体族和字体风格。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 文本尺寸，Length为Int64、Float64类型时，使用fp单位。不支持设置百分比字符串。<br>初始值：16.fp|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|是|-| **命名参数。** 文本的字体粗细。|
|family|String|是|-| **命名参数。** 文本的字体列表。使用多个字体，使用','进行分割，优先级按顺序生效。例如：'Arial, HarmonyOS Sans'。当前支持'HarmonyOS Sans'字体和[注册自定义字体](./cj-apis-font.md)。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|是|-| **命名参数。** 文本的字体样式。<br>初始值：FontStyle.Normal。|

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
|value|String|是|-|字体列表。|

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
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|字体列表。|