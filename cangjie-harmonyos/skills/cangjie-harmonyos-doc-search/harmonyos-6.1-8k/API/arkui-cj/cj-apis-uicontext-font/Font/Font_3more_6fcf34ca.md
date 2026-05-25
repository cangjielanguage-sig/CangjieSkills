# Font

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

注册自定义字体的信息。

> **说明：**
>
> 以下API需先使用[UIContext](./cj-apis-uicontext-uicontext.md#class-uicontext)中的[getFont()](./cj-apis-uicontext-uicontext.md#func-getfont)方法获取Font实例，再通过此实例调用对应方法。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## class Font

```cangjie
public class Font {}
```

**功能：** 字体类，提供字体注册、获取系统字体列表和根据字体名称获取字体信息等功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func getFontByName(String)

```cangjie
public func getFontByName(fontName: String): ?FontInfo
```

**功能：** 根据字体名称获取字体详细信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fontName|String|是|-|字体名称。|

**返回值：**

|类型|说明|
|:----|:----|
|?[FontInfo](#class-fontinfo)|返回字体信息，如果找不到对应字体则返回None。|

### func getSystemFontList()

```cangjie
public func getSystemFontList(): Array<String>
```

**功能：** 获取系统支持的字体列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|系统字体名称列表。|

### func registerFont(ResourceStr, ResourceStr)

```cangjie
public func registerFont(familyName!: ResourceStr, familySrc!: ResourceStr): Unit
```

**功能：** 在字体管理中注册自定义字体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|familyName|[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-| **命名参数。** 字体名称。|
|familySrc|[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-| **命名参数。** 字体资源路径。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码|说明|
  |:----|:----|
  |401|Invalid input parameter|
  |100001|Internal error.|