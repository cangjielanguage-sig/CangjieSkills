## func createData(String, Array\<UInt8>)

```cangjie
public func createData(mimeType: String, value: Array<UInt8>): PasteData
```

**功能：** 构建一个剪贴板内容对象。定义的字符串。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|剪贴板数据对应的MIME类型，为自定义String。|
|value|Array\<UInt8>|是|-|数据内容。|

**返回值：**

|类型|说明|
|:----|:----|
|[PasteData](#class-pastedata)|返回剪贴板内容对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

var dataText = Array<UInt8>(96, repeat: 0)
let pasteData = createData("app/xml", dataText)
```

## func createRecord(String, String)

```cangjie
public func createRecord(mimeType: String, value: String): PasteDataRecord
```

**功能：** 创建一条数据内容条目。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|剪贴板数据对应的MIME类型，可以是常量中已定义的类型，也可以自定义。mimeType取值可以为[MIMETYPE_TEXT_HTML](#const-mimetype_text_html)、[MIMETYPE_TEXT_PLAIN](#const-mimetype_text_plain)、[MIMETYPE_TEXT_URI](#const-mimetype_text_uri)。|
|value|String|是|-|字符串数据内容。|

**返回值：**

| 类型 | 说明|
| :-------| :------- |
| [PasteDataRecord](#class-pastedatarecord)| 返回新建的数据内容条目。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "word"
let pasteDataRecord = createRecord(MIMETYPE_TEXT_PLAIN, dataText)
```

## func createRecord(String, PixelMap)

```cangjie
public func createRecord(mimeType: String, value: PixelMap): PasteDataRecord
```

**功能：** 创建一条数据内容条目。

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
|[PasteDataRecord](#class-pastedatarecord)|返回新建的数据内容条目。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.image.*
import kit.BasicServicesKit.*

var globalPixelMap: PixelMap
var color: Array<UInt8> = Array<UInt8>(96) {index: Int64 => UInt8(index + 1)}
var opts = InitializationOptions(editable: true, pixelFormat: PixelMapFormat.RGBA_8888, size: Size(height: 6, width: 8))
globalPixelMap = createPixelMap(color, opts)
let pasteDataRecord1 = createRecord(MIMETYPE_PIXELMAP, globalPixelMap)
```

## func createRecord(String, Array\<UInt8>)

```cangjie
public func createRecord(mimeType: String, value: Array<UInt8>): PasteDataRecord
```

**功能：** 创建一条数据内容条目。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|剪贴板数据对应的MIME类型，为自定义String。|
|value|Array\<UInt8>|是|-|数据内容。|

**返回值：**

|类型|说明|
|:----|:----|
|[PasteDataRecord](#class-pastedatarecord)|返回新建的数据内容条目。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

var dataText = Array<UInt8>(96, repeat: 0)
let pasteData = createData("app/xml", dataText)
```