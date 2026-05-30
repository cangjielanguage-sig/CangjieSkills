## class PasteData

```cangjie
public class PasteData {}
```

**功能：** 剪贴板内容对象。剪贴板内容包含一个或者多个内容条目（PasteDataRecord）以及属性描述对象（PasteDataProperty）。

在调用PasteData的方法前，需要先通过createData()获取一个PasteData对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

### func addRecord(PasteDataRecord)

```cangjie
public func addRecord(record: PasteDataRecord): Unit
```

**功能：** 向当前剪贴板内容中添加一条数据内容条目，同时也会将条目类型添加到PasteDataProperty的mimeTypes中。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|record|[PasteDataRecord](#class-pastedatarecord)|是|-|待添加的条目。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let uri = "dataability:///com.example.myapplication1/user.txt"
pasteDataRecord = createRecord("Custom", uri.toArray())
pasteData.addRecord(pasteDataRecord)
```

### func addRecord(String, String)

```cangjie
public func addRecord(mimeType: String, value: String): Unit
```

**功能：** 向当前剪贴板内容中添加一条数据内容条目, 同时也会将条目类型添加到PasteDataProperty的mimeTypes中。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|剪贴板数据对应的MIME类型，为自定义String。|
|value|String|是|-|数据内容。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
var data = Array<UInt8>(96, repeat: 0)
pasteData.addRecord("app/xml", " ")
```

### func addRecord(String, PixelMap)

```cangjie
public func addRecord(mimeType: String, value: PixelMap): Unit
```

**功能：** 向当前剪贴板内容中添加一条数据内容条目, 同时也会将条目类型添加到PasteDataProperty的mimeTypes中。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|剪贴板数据对应的MIME类型，为自定义String。|
|value|[PixelMap](../../apis/ImageKit/cj-apis-image.md#class-pixelmap)|是|-|数据内容。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.image.*

let color: Array<UInt8> = Array<UInt8>(96) {index: Int64 => UInt8(index + 1)}
let opts = InitializationOptions(editable: true, pixelFormat: PixelMapFormat.RGBA_8888, size: Size(height: 6, width: 4))
let pixelMap1 = createPixelMap(color, opts)
let pasteData = createData(MIMETYPE_TEXT_PLAIN, pixelMap1)
pasteData.addRecord("app/xml", pixelMap1)
```

### func addRecord(String, Array\<UInt8>)

```cangjie
public func addRecord(mimeType: String, value: Array<UInt8>): Unit
```

**功能：** 向当前剪贴板内容中添加一条数据内容条目, 同时也会将条目类型添加到PasteDataProperty的mimeTypes中。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|剪贴板数据对应的MIME类型，为自定义String。|
|value|Array\<UInt8>|是|-|数据内容。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
var data = Array<UInt8>(96, repeat: 0)
pasteData.addRecord("app/xml", data)
```