### func getMimeTypes()

```cangjie
public func getMimeTypes(): Array<String>
```

**功能：** 获取剪贴板中PasteDataProperty的mimeTypes列表，当剪贴板内容为空时，返回列表为空。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|剪贴板内容条目的数据类型。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
let resMimeTypes = pasteData.getMimeTypes()
```

### func getPrimaryHtml()

```cangjie
public func getPrimaryHtml(): String
```

**功能：** 获取首个条目的HTML内容。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|HTML内容。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" +
    "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "<h1>HEAD</h1>\n" + "<p></p>\n" + "</body>\n" +
    "</html>"
let pasteData = createData(MIMETYPE_TEXT_HTML, dataText)
let res = pasteData.getPrimaryHtml()
```

### func getPrimaryMimeType()

```cangjie
public func getPrimaryMimeType(): String
```

**功能：** 获取剪贴板内容中首个条目的数据类型。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|首个条目的数据类型。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
let res = pasteData.getPrimaryMimeType()
```

### func getPrimaryPixelMap()

```cangjie
public func getPrimaryPixelMap(): PixelMap
```

**功能：** 获取首个条目的PixelMap内容。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../../apis/ImageKit/cj-apis-image.md#class-pixelmap)|PixelMap内容。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

var globalPixelMap: PixelMap
var color: Array<UInt8> = Array<UInt8>(96) {index: Int64 => UInt8(index + 1)}
var opts = InitializationOptions(editable: true, pixelFormat: PixelMapFormat.RGBA_8888, size: Size(height: 6, width: 8))
globalPixelMap = createPixelMap(color, opts)
let pasteData = createData(MIMETYPE_PIXELMAP, globalPixelMap)
let res = pasteData.getPrimaryPixelMap()
```

### func getPrimaryText()

```cangjie
public func getPrimaryText(): String
```

**功能：** 获取首个条目的纯文本内容。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|纯文本内容。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
let res = pasteData.getPrimaryText()
```

### func getPrimaryUri()

```cangjie
public func getPrimaryUri(): String
```

**功能：** 获取首个条目的URI内容。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|URI内容。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let uri = "dataability:///com.example.myapplication1/user.txt"
let pasteData = createData(MIMETYPE_TEXT_URI, uri)
let res = pasteData.getPrimaryUri()
```