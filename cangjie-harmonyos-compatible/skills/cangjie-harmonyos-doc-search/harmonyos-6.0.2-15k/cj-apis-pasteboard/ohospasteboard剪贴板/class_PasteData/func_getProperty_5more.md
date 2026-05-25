### func getProperty()

```cangjie
public func getProperty(): PasteDataProperty
```

**功能：** 获取剪贴板内容的属性描述对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[PasteDataProperty](#struct-pastedataproperty)|属性描述对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
let property = pasteData.getProperty()
```

### func getRecord(Int32)

```cangjie
public func getRecord(index: Int32): PasteDataRecord
```

**功能：** 获取剪贴板内容中指定下标的条目。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|指定条目的下标。|

**返回值：**

|类型|说明|
|:----|:----|
|[PasteDataRecord](#class-pastedatarecord)|指定下标的条目。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
let res = pasteData.getRecord(0)
```

### func getRecordCount()

```cangjie
public func getRecordCount(): UIntNative
```

**功能：** 获取剪贴板内容中条目的个数。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|UIntNative|条目的个数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
let res = pasteData.getRecordCount()
```

### func getTag()

```cangjie
public func getTag(): String
```

**功能：** 获取剪贴板内容中用户自定义的标签内容，如果没有设置用户自定义的标签内容将返回空。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回用户自定义的标签内容，如果没有设置用户自定义的标签内容，将返回空。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
var property = pasteData.getProperty()
property.tag = "mytag"
pasteData.setProperty(property)
var property1 = pasteData.getProperty()
let resTag = pasteData.getTag()
```

### func hasType(String)

```cangjie
public func hasType(mimeType: String): Bool
```

**功能：** 检查剪贴板内容中是否有指定的MIME数据类型。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|待查询的数据类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|有指定的数据类型返回true，否则返回false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
let resBool = pasteData.hasType(MIMETYPE_TEXT_PLAIN)
```