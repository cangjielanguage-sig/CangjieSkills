# 文本样式设置

针对包含文本元素的组件，设置文本样式。

## func fontColor(ResourceColor)

```cangjie
public func fontColor(value: ResourceColor): This
```

**功能：** 设置字体颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:--- |:---|:---|
| value  | [ResourceColor](./cj-common-types.md#interface-resourcecolor)| 是 | \-  | 字体颜色。 |

## func fontSize(Length)

```cangjie
public func fontSize(value: Length): This
```

**功能：** 设置字体大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:--- |:---|:---|
| value  | [Length](./cj-common-types.md#interface-length) | 是  | \-  | 字体大小。<br>单位：fp。<br>初始值：16.fp。<br>**说明：** 不支持设置百分比。|

## func fontStyle(FontStyle)

```cangjie
public func fontStyle(value: FontStyle): This
```

**功能：** 设置文本的字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:--- |:---|:---|
| value  | [FontStyle](./cj-common-types.md#enum-fontstyle) | 是  |-| 字体样式。</br>初始值：FontStyle.Normal。|

## func fontWeight(FontWeight)

```cangjie
public func fontWeight(value: FontWeight): This
```

**功能：** 设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:--- |:---|:---|
| value  | [FontWeight](./cj-common-types.md#enum-fontweight) | 是  |-| 文本的字体粗细。</br>初始值：FontStyle.Normal。 |

## func fontFamily(String)

```cangjie
public func fontFamily(value: String): This
```

**功能：** 设置字体列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:--- |:---|:---|
| value  | String | 是  | \-  | 文本的字体列表。默认字体'HarmonyOS Sans'。应用当前支持'HarmonyOS Sans'字体和注册自定义字体。<br>**说明：** 使用多个字体，使用','进行分割，优先级按顺序生效。例如："Arial, sans-serif"。 |

## func fontFamily(AppResource)

```cangjie
public func fontFamily(value: AppResource): This
```

**功能：** 根据指定的资源设置文本的字体列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:--- |:---|:---|
| value  | [AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource) | 是  | \- | 文本的字体列表。<br>**说明：** 使用多个字体，使用','进行分割，优先级按顺序生效。例如："Arial, sans-serif"。 |

## func lineHeight(value: Length)

```cangjie
public func lineHeight(value: Length): This
```

**功能：** 设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:--- |:---|:---|
| value  | [Length](./cj-common-types.md#interface-length) | 是  | \-  | 文本行高。<br>单位：fp。|

## func decoration(TextDecorationType,Color)

```cangjie
public func decoration(decorationType!: TextDecorationType, color!: Color): This
```

**功能：** 设置文本装饰线样式及其颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:--- |:---|:---|
| decorationType  | [TextDecorationType](./cj-common-types.md#enum-textdecorationtype) | 否  | TextDecorationType.None | **命名参数。**  文本装饰线类型。|
| color  | [Color](./cj-common-types.md#Color) | 否  | Color.BLACK | **命名参数。**  文本线颜色。|