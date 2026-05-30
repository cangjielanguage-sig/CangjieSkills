### func selectedBackgroundColor(ResourceColor)

```cangjie
public func selectedBackgroundColor(value: ResourceColor): This
```

**功能：** 设置选中项背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|选中项背景颜色。<br>初始值：0x1A007DFF。|

### func selectedColor(ResourceColor)

```cangjie
public func selectedColor(value: ResourceColor): This
```

**功能：** 设置选中项文字颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|选中项文字颜色。<br>初始值：0xFF007DFF。|

### func selectedFont(Length, FontWeight, String, FontStyle)

```cangjie
public func selectedFont(
    size!: Length = 10.vp,
    weight!: FontWeight = FontWeight.Normal,
    family!: String = "HarmonyOS Sans",
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置选中项文字样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|10.vp| **命名参数。** 选中项文字大小。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 选中项文字字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 选中项文字字体家族。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 选中项文字样式。|

### func selectedFont(Length, FontWeight, AppResource, FontStyle)

```cangjie
public func selectedFont(
    size!: Length = 10.vp,
    weight!: FontWeight = FontWeight.Normal,
    family!: AppResource,
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置选中项文字样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|10.vp| **命名参数。** 选中项文字大小。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 选中项文字字体粗细。|
|family|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 选中项文字字体家族。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 选中项文字样式。|

### func usingPopup(Bool)

```cangjie
public func usingPopup(usingPopup: Bool): This
```

**功能：** 设置是否使用提示弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|usingPopup|Bool|是|-|是否使用提示弹窗。<br>初始值：false。|