### func contentFont(?Length, ?FontWeight, ?ResourceStr, ?FontStyle)

```cangjie
public func contentFont(
    size!: ?Length = None,
    weight!: ?FontWeight = None,
    family!: ?ResourceStr = None,
    style!: ?FontStyle = None
): This
```

**功能：**设置菜单项中内容信息的字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 设置文本尺寸，Length为Int64、Float64类型时，使用fp单位。不支持百分比设置。初始值：16.vp。|
|weight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 设置文本的字体粗细。初始值：FontWeight.Normal。|
|family|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 设置文本的字体列表。使用多个字体，使用','进行分割，优先级按顺序生效。例如：'Arial, HarmonyOS Sans'。当前支持'HarmonyOS Sans'字体和[注册自定义字体](./cj-apis-uicontext-font.md)。初始值："HarmonyOS Sans"。|
|style|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None|**命名参数。** 设置文本的字体样式。初始值：FontStyle.Normal。|

### func contentFontColor(?ResourceColor)

```cangjie
public func contentFontColor(value: ?ResourceColor): This
```

**功能：** 设置菜单项中内容信息的字体颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|菜单项中内容信息的字体颜色。初始值：0xE5000000。|

### func labelFont(?Length, ?FontWeight, ?ResourceStr, ?FontStyle)

```cangjie
public func labelFont(
    size!: ?Length = None,
    weight!: ?FontWeight = None,
    family!: ?ResourceStr = None,
    style!: ?FontStyle = None
): This
```

**功能：**设置菜单项中标签信息的字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 设置文本尺寸，Length为Int64、Float64类型时，使用fp单位。不支持百分比设置。初始值：16.vp。|
|weight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 设置文本的字体粗细。初始值：FontWeight.Normal。|
|family|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 设置文本的字体列表。使用多个字体，使用','进行分割，优先级按顺序生效。例如：'Arial, HarmonyOS Sans'。初始值："HarmonyOS Sans"。|
|style|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None|**命名参数。**  设置文本的字体样式。初始值：FontStyle.Normal。|

### func labelFontColor(?ResourceColor)

```cangjie
public func labelFontColor(value: ?ResourceColor): This
```

**功能：** 设置菜单项中标签信息的字体颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|菜单项中标签信息的字体颜色。初始值：0x99000000。|

### func selected(?Bool)

```cangjie
public func selected(value: ?Bool): This
```

**功能：** 设置菜单项是否选中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|菜单项是否选中。初始值：false。|