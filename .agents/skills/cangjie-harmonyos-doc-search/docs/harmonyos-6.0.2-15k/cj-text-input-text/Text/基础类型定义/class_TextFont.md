### class TextFont

```cangjie
public class TextFont {
    public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: String = "", style!: FontStyle = FontStyle.Normal)
    public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: AppResource, style!: FontStyle = FontStyle.Normal)
}
```

**功能：** 文本样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Length, FontWeight, AppResource, FontStyle)

```cangjie
public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: AppResource, style!: FontStyle = FontStyle.Normal)
```

**功能：** 创建TextFont对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](cj-common-types.md#interface-length)|否|16.fp| **命名参数。** 字体大小。|
|weight|[FontWeight](cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 字体粗细。|
|family|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 字体列表。|
|style|[FontStyle](cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 字体样式。|

#### init(Length, FontWeight, String, FontStyle)

```cangjie
public init(size!: Length = 16.fp, weight!: FontWeight = FontWeight.Normal, family!: String = "", style!: FontStyle = FontStyle.Normal)
```

**功能：** 创建TextFont对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](cj-common-types.md#interface-length)|否|16.fp| **命名参数。** 字体大小。|
|weight|[FontWeight](cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 字体粗细。|
|family|String|否|""| **命名参数。** 字体列表。|
|style|[FontStyle](cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 字体样式。|