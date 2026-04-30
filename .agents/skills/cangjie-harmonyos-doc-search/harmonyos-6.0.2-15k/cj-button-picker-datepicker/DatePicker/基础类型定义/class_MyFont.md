### class MyFont

```cangjie
public class MyFont {
    public var size: Length
    public var weight: FontWeight
    public var family: String
    public var style: FontStyle
    public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: String = "HarmonyOS Sans", style!: FontStyle = FontStyle.Normal)
    public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: AppResource, style!: FontStyle = FontStyle.Normal)
}
```

**功能：** 设置字体初始化格式样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var family

```cangjie
public var family: String
```

**功能：** 字体系列。初始值：HarmonyOS Sans。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var size

```cangjie
public var size: Length
```

**功能：** 字体尺寸。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var style

```cangjie
public var style: FontStyle
```

**功能：** 字体风格。

**类型：** [FontStyle](./cj-common-types.md#enum-fontstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var weight

```cangjie
public var weight: FontWeight
```

**功能：** 字体粗细。

**类型：** [FontWeight](./cj-common-types.md#enum-fontweight)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Length, FontWeight, String, FontStyle)

```cangjie
public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: String = "HarmonyOS Sans", style!: FontStyle = FontStyle.Normal)
```

**功能：** myfont的构造函数，此时字体系列为[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|16.fp| **命名参数。** 字体尺寸。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 字体列表。<br/>初始值：HarmonyOS Sans。|
|style|[FontStyle](./cj-common-types.md#enum-fontweight)|否|FontStyle.Normal| **命名参数。** 字体样式。|

#### init(Length, FontWeight, AppResource, FontStyle)

```cangjie
public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: AppResource, style!: FontStyle = FontStyle.Normal)
```

**功能：** myfont的构造函数，此时字体系列为[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|16.fp| **命名参数。** 字体尺寸。不支持百分比设置。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 字体粗细。|
|family|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 字体列表。<br/>初始值：HarmonyOS Sans。|
|style|[FontStyle](./cj-common-types.md#enum-fontweight)|否|FontStyle.Normal| **命名参数。** 字体样式。|