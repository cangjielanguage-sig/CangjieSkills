### func labelFont(Length, FontWeight, String, FontStyle)

```cangjie
public func labelFont(
    size!: Length = 16.vp,
    weight!: FontWeight = FontWeight.Normal,
    family!: String = "HarmonyOS Sans",
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置菜单项中标签信息的字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|16.vp| **命名参数。** 设置文本尺寸，Length为Int64、Float64类型时，使用fp单位。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 设置文本的字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 设置文本的字体列表。使用多个字体，使用','进行分割，优先级按顺序生效。例如：'Arial, HarmonyOS Sans'。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。**  设置文本的字体样式。|

### func labelFont(Length, FontWeight, AppResource, FontStyle)

```cangjie
public func labelFont(
    size!: Length = 16.vp,
    weight!: FontWeight = FontWeight.Normal,
    family!: AppResource,
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置菜单项中标签信息的字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|16.vp| **命名参数。** 设置文本尺寸，Length为Int64、Float64类型时，使用fp单位。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 设置文本的字体粗细。|
|family|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置文本的字体列表。使用多个字体，使用','进行分割，优先级按顺序生效。例如：'Arial, HarmonyOS Sans'。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。**  设置文本的字体样式。|

### func labelFontColor(AppResource)

```cangjie
public func labelFontColor(value: AppResource): This
```

**功能：** 设置菜单项中标签信息的字体颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|菜单项中标签信息的字体颜色。<br/>初始值：'0x99000000'|

### func selectIcon(Bool)

```cangjie
public func selectIcon(value: Bool): This
```

**功能：** 设置当菜单项被选中时，是否显示被选中的图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|菜单项被选中时，是否显示被选中的图标。<br/>初始值：false<br/>true：菜单项被选中时，显示默认的对勾图标。<br/>false：即使菜单项被选中也不显示图标。|

### func selectIcon(AppResource)

```cangjie
public func selectIcon(value: AppResource): This
```

**功能：** 设置当菜单项被选中时，是否显示被选中的图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|菜单项被选中时，显示指定的图标。|