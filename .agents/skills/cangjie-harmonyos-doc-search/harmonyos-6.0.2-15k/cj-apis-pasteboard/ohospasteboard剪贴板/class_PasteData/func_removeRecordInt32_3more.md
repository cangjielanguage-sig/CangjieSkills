### func removeRecord(Int32)

```cangjie
public func removeRecord(index: Int32): Unit
```

**功能：** 移除剪贴板内容中指定下标的条目。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|指定的下标。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[剪贴板错误码](../../errorcodes/cj-errorcode-pasteboard.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |12900001|The index is out of the record.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText = "hello"
let pasteData = createData(MIMETYPE_TEXT_PLAIN, dataText)
let res = pasteData.getRecord(0)
pasteData.removeRecord(0)
```

### func replaceRecord(Int32, PasteDataRecord)

```cangjie
public func replaceRecord(index: Int32, record: PasteDataRecord): Unit
```

**功能：** 替换剪贴板内容中指定下标的条目。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|指定的下标。|
|record|[PasteDataRecord](#class-pastedatarecord)|是|-|待添加的条目。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let dataText1 = "hello"
let pasteData = createData("text/plain", dataText1)
let dataText2 = "word"
let pasteDataRecord1 = createRecord("text/plain", dataText2)
pasteData.replaceRecord(0, pasteDataRecord1)
```

### func setProperty(PasteDataProperty)

```cangjie
public func setProperty(pasteDataProperty: PasteDataProperty): Unit
```

**功能：** 设置剪贴板内容的属性描述对象PasteDataProperty。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pasteDataProperty|[PasteDataProperty](#struct-pastedataproperty)|是|-|属性描述对象。|

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
```