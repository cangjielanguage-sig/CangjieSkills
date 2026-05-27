### func disappearTextStyle(ResourceColor, Length, FontWeight, String, FontStyle)

```cangjie
public func disappearTextStyle(
    color!: ResourceColor = 0xff182431,
    size!: Length = 14.fp,
    weight!: FontWeight = FontWeight.Regular,
    family!: String = "HarmonyOS Sans",
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置所有选项中最上和最下两个选项的文本样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|0xff182431| **命名参数。** 文本颜色。|
|size|[Length](./cj-common-types.md#interface-length)|否|14.fp| **命名参数。** 文本尺寸。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Regular| **命名参数。** 字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 字体列表。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 字体样式。|

### func disappearTextStyle(ResourceColor, Length, FontWeight, AppResource, FontStyle)

```cangjie
public func disappearTextStyle(
    color!: ResourceColor = 0xff182431,
    size!: Length,
    weight!: FontWeight = FontWeight.Regular,
    family!: AppResource,
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置所有选项中最上和最下两个选项的文本样式。

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

### func lunar(Bool)

```cangjie
public func lunar(isLunar: Bool): This
```

**功能：** 设置弹窗的日期是否显示农历。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isLunar|Bool|是|-|日期是否显示农历。<br/> - true：展示农历。<br/> - false：不展示农历。<br>初始值：false。|

### func selectedTextStyle(ResourceColor, Length, FontWeight, String, FontStyle)

```cangjie
public func selectedTextStyle(
    color!: ResourceColor = 0xff007dff,
    size!: Length = 20.vp,
    weight!: FontWeight = FontWeight.Medium,
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
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|0xff007dff| **命名参数。** 文本颜色。|
|size|[Length](./cj-common-types.md#interface-length)|否|20.vp| **命名参数。** 文本尺寸。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Medium| **命名参数。** 字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 字体列表。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 字体样式。|