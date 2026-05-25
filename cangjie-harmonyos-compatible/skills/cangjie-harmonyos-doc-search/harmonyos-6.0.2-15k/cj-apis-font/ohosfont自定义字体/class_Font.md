## class Font

```cangjie
public class Font {}
```

**功能：** 该类提供了一些注册和获取自定义字体的全局方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func registerFont(String, String)

```cangjie
public static func registerFont(familyName!: String, familySrc!: String): Unit
```

**功能：** 在字体管理中注册自定义字体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|familyName|String|是|-| **命名参数。** 设置注册字体的名称。|
|familySrc|String|是|-| **命名参数。** 设置注册字体文件的路径。|

### static func registerFont(AppResource, AppResource)

```cangjie
public static func registerFont(familyName!: AppResource, familySrc!: AppResource): Unit
```

**功能：** 在字体管理中注册自定义字体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|familyName|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置注册字体的名称。|
|familySrc|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置注册字体文件的路径。|

### static func getSystemFontList()

```cangjie
public static func getSystemFontList(): Array<String>
```

**功能：** 获取系统字体列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|系统字体列表。|

### static func getFontByName(String)

```cangjie
public static func getFontByName(fontName: String): ?FontInfo
```

**功能：** 根据传入的系统字体名称获取系统字体的相关信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fontName|String|是|-|系统的字体名。|

**返回值：**

|类型|说明|
|:----|:----|
|?[FontInfo](#class-fontinfo)|字体的详细信息。|

### static func getUIFontConfig()

```cangjie
public static func getUIFontConfig(): UIFontConfig
```

**功能：** 获取系统的UI字体配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[UIFontConfig](#class-uifontconfig)|系统的UI字体配置信息。|