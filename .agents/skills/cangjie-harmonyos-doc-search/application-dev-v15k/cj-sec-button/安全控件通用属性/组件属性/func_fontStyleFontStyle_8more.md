### func fontStyle(FontStyle)

```cangjie
public open func fontStyle(style: FontStyle): This
```

**功能：** 设置安全控件上文字的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|是|-|安全控件上文字的样式。<br/>初始值：FontStyle.Normal。|

### func fontWeight(FontWeight)

```cangjie
public open func fontWeight(value: FontWeight): This
```

**功能：** 设置安全控件上文字粗细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontWeight](./cj-common-types.md#enum-fontweight)|是|-|安全控件上文字粗细。<br/>初始值：FontWeight.Medium。|

### func fontFamily(String)

```cangjie
public open func fontFamily(content: String): This
```

**功能：** 设置安全控件上文字的字体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|是|-|安全控件上文字的字体。<br/>默认字体：'HarmonyOS Sans'。|

### func fontFamily(AppResource)

```cangjie
public open func fontFamily(content: AppResource): This
```

**功能：** 设置安全控件上文字的字体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|安全控件上文字的字体。<br/>默认字体：'HarmonyOS Sans'。|

### func fontColor(ResourceColor)

```cangjie
public open func fontColor(color: ResourceColor): This
```

**功能：** 设置安全控件上文字的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|安全控件上文字的颜色。<br/>初始值：@r(sys.color.font_on_primary)。|

### func iconColor(ResourceColor)

```cangjie
public open func iconColor(color: ResourceColor): This
```

**功能：** 设置安全控件上图标的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|安全控件上图标的颜色。<br/>初始值：Color.WHITE。|

### func backgroundColor(ResourceColor)

```cangjie
public open func backgroundColor(value: ResourceColor): This
```

**功能：** 设置安全控件的背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|安全控件的背景颜色。<br/>初始值：Color.BLUE。|

### func borderStyle(BorderStyle)

```cangjie
public open func borderStyle(style: BorderStyle): This
```

**功能：** 设置安全控件的边框的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[BorderStyle](./cj-common-types.md#enum-borderstyle)|是|-|安全控件的边框的样式。<br/>默认不设置边框样式。|