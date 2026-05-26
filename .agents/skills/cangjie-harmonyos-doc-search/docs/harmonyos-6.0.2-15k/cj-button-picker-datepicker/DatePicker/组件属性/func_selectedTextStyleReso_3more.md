### func selectedTextStyle(ResourceColor, Length, FontWeight, AppResource, FontStyle)

```cangjie
public func selectedTextStyle(
    color!: ResourceColor = 0xff007dff,
    size!: Length,
    weight!: FontWeight = FontWeight.Medium,
    family!: AppResource,
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置选中项的文本样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|0xff007dff| **命名参数。** 文本颜色。|
|size|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 文本尺寸。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Medium| **命名参数。** 字体粗细。|
|family|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 字体列表。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 字体样式。|

### func textStyle(ResourceColor, Length, FontWeight, String, FontStyle)

```cangjie
public func textStyle(
    color!: ResourceColor = 0xff182431,
    size!: Length = 16.fp,
    weight!: FontWeight = FontWeight.Regular,
    family!: String = "HarmonyOS Sans",
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置选中项的文本样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|0xff182431| **命名参数。** 文本颜色。|
|size|[Length](./cj-common-types.md#interface-length)|否|16.fp| **命名参数。** 文本尺寸。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Regular| **命名参数。** 字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 字体列表。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 字体样式。|

### func textStyle(ResourceColor, Length, FontWeight, AppResource, FontStyle)

```cangjie
public func textStyle(
    color!: ResourceColor = 0xff182431,
    size!: Length,
    weight!: FontWeight = FontWeight.Regular,
    family!: AppResource,
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置选中项的文本样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|0xff182431| **命名参数。** 文本颜色。|
|size|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 文本尺寸。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Regular| **命名参数。** 字体粗细。|
|family|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 字体列表。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 字体样式。|