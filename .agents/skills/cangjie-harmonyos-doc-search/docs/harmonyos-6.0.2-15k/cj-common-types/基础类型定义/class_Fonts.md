## class Fonts

```cangjie
public class Fonts {
    public var size: Length
    public var weight: FontWeight
    public var family: String
    public var style: FontStyle
    public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: String = "HarmonyOS Sans",
        style!: FontStyle = FontStyle.Normal)
    public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: AppResource,
        style!: FontStyle = FontStyle.Normal)
}
```

**功能：** 文本样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var family

```cangjie
public var family: String
```

**功能：** 设置文本的字体列表。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var size

```cangjie
public var size: Length
```

**功能：** 设置文本尺寸，使用fp单位。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var style

```cangjie
public var style: FontStyle
```

**功能：** 设置文本的字体样式。

**类型：** [FontStyle](./cj-common-types.md#enum-fontstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var weight

```cangjie
public var weight: FontWeight
```

**功能：** 设置文本的字体粗细。

**类型：** [FontWeight](./cj-common-types.md#enum-fontweight)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Length, FontWeight, String, FontStyle)

```cangjie
public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: String = "HarmonyOS Sans",
    style!: FontStyle = FontStyle.Normal)
```

**功能：** 构造一个Fonts对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|16.fp| **命名参数。** 设置文本尺寸，Length为Int64、Float64类型时，使用fp单位。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 设置文本的字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 设置文本的字体列表。使用多个字体，使用','进行分割，优先级按顺序生效。例如：'Arial, HarmonyOS Sans'。当前支持'HarmonyOS Sans'字体。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 设置文本的字体样式。|

### init(Length, FontWeight, AppResource, FontStyle)

```cangjie
public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: AppResource,
    style!: FontStyle = FontStyle.Normal)
```

**功能：** 构造一个Fonts对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|16.fp| **命名参数。** 设置文本尺寸，Length为Int64、Float64类型时，使用fp单位。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 设置文本的字体粗细。|
|family|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置文本的字体列表。使用多个字体，使用','进行分割，优先级按顺序生效。例如：'Arial, HarmonyOS Sans'。当前支持'HarmonyOS Sans'字体。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 设置文本的字体样式。|