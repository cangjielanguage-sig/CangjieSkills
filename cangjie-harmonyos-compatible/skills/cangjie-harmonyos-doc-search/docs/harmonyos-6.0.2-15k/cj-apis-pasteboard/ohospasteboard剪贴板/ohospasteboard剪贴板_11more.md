# ohos.pasteboard（剪贴板）

本模块主要提供管理系统剪贴板的能力，为系统复制、粘贴功能提供支持。系统剪贴板支持对文本、HTML、URI、PixelMap等内容的操作。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 权限列表

ohos.permission.READ_PASTEBOARD

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## const MIMETYPE_PIXELMAP

```cangjie
public const MIMETYPE_PIXELMAP = "pixelMap"
```

**功能：** PixelMap内容的MIME类型定义。

**类型：** String

**起始版本：** 12

## const MIMETYPE_TEXT_HTML

```cangjie
public const MIMETYPE_TEXT_HTML = "text/html"
```

**功能：** HTML内容的MIME类型定义。

**类型：** String

**起始版本：** 12

## const MIMETYPE_TEXT_PLAIN

```cangjie
public const MIMETYPE_TEXT_PLAIN = "text/plain"
```

**功能：** 纯文本内容的MIME类型定义。

**类型：** String

**起始版本：** 12

## const MIMETYPE_TEXT_URI

```cangjie
public const MIMETYPE_TEXT_URI = "text/uri"
```

**功能：** URI内容的MIME类型定义。

**类型：** String

**起始版本：** 12

## const MIMETYPE_TEXT_WANT

```cangjie
public const MIMETYPE_TEXT_WANT = "text/want"
```

**功能：** Want内容的MIME类型定义。

**类型：** String

**起始版本：** 12

## func createData(String, String)

```cangjie
public func createData(mimeType: String, value: String): PasteData
```

**功能：** 构建一个剪贴板内容对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|剪贴板数据对应的MIME类型，可以是常量中已定义的类型，也可以自定义。mimeType取值可以为[MIMETYPE_TEXT_HTML](#const-mimetype_text_html)、[MIMETYPE_TEXT_PLAIN](#const-mimetype_text_plain)、[MIMETYPE_TEXT_URI](#const-mimetype_text_uri)。|
|value|String|是|-|字符串数据内容。|

**返回值：**

| 类型                     | 说明                     |
| :---------------------    | :------------------------ |
| [PasteData](#class-pastedata)  | 返回剪贴板内容对象。       |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
```

## func createData(String, PixelMap)

```cangjie
public func createData(mimeType: String, value: PixelMap): PasteData
```

**功能：** 构建一个剪贴板内容对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|剪贴板数据对应的MIME类型，可以是常量中已定义的类型，也可以自定义。取值为[MIMETYPE_PIXELMAP](#const-mimetype_pixelmap)。|
|value|[PixelMap](../../apis/ImageKit/cj-apis-image.md#class-pixelmap)|是|-|PixelMap类型的数据内容。|

**返回值：**

|类型|说明|
|:----|:----|
|[PasteData](#class-pastedata)|返回剪贴板内容对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.image.*

var globalPixelMap: PixelMap
var color: Array<UInt8> = Array<UInt8>(96) {index: Int64 => UInt8(index + 1)}
var opts = InitializationOptions(editable: true, pixelFormat: PixelMapFormat.RGBA_8888, size: Size(height: 6, width: 8))
globalPixelMap = createPixelMap(color, opts)
let pasteData = createData(MIMETYPE_TEXT_PLAIN, globalPixelMap)
```