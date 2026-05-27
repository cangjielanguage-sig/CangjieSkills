### func popupFont(Length, FontWeight, String, FontStyle)

```cangjie
public func popupFont(
    size!: Length = 24.vp,
    weight!: FontWeight = FontWeight.Normal,
    family!: String = "HarmonyOS Sans",
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置提示弹窗字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|24.vp| **命名参数。** 选中项文字大小。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 选中项文字字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 选中项文字字体家族。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 选中项文字样式。|

### func popupFont(Length, FontWeight, AppResource, FontStyle)

```cangjie
public func popupFont(
    size!: Length = 24.vp,
    weight!: FontWeight = FontWeight.Normal,
    family!: AppResource,
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置提示弹窗字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|24.vp| **命名参数。** 选中项文字大小。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 选中项文字字体粗细。|
|family|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 选中项文字字体家族。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 选中项文字样式。|

### func popupItemBackgroundColor(ResourceColor)

```cangjie
public func popupItemBackgroundColor(value: ResourceColor): This
```

**功能：** 设置提示弹窗二级索引项背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|提示弹窗二级索引项背景颜色。<br>初始值：0x00000000。|

### func popupItemBorderRadius(Float64)

```cangjie
public func popupItemBorderRadius(value: Float64): This
```

**功能：** 设置提示弹窗索引项背板圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|设置提示弹窗索引项背板圆角半径。<br>不支持设置为百分比，小于0时按照0设置。<br>提示弹窗背板圆角自适应变化（索引项圆角半径+4vp）。<br>初始值：24.0vp。|

### func popupItemFont(Length, FontWeight, String, FontStyle)

```cangjie
public func popupItemFont(
    size!: Length = 24.vp,
    weight!: FontWeight = FontWeight.Medium,
    family!: String = "HarmonyOS Sans",
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置提示弹窗二级索引项文本样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|24.vp| **命名参数。** 提示弹窗二级索引项字体大小。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Medium| **命名参数。** 提示弹窗二级索引项字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 提示弹窗二级索引项字体家族。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 提示弹窗二级索引项字体样式。|