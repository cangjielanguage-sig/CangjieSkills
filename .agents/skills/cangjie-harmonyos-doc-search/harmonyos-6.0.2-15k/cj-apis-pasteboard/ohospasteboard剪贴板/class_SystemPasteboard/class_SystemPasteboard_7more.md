## class SystemPasteboard

```cangjie
public class SystemPasteboard {}
```

**功能：** 系统剪贴板。

在调用SystemPasteboard的接口前，需要先通过getSystemPasteboard()方法获取系统剪贴板。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

### func clearData()

```cangjie
public func clearData(): Unit
```

**功能：** 清空系统剪贴板内容。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let sysBoard = getSystemPasteboard()
let hasRes = sysBoard.clearData()
```

### func getData()

```cangjie
public func getData(): PasteData
```

**功能：** 读取系统剪贴板内容。

**需要权限：** ohos.permission.READ_PASTEBOARD

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[PasteData](#class-pastedata)|返回剪贴板内容对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[剪贴板错误码](../../errorcodes/cj-errorcode-pasteboard.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |12900003|Another copy or paste is in progress.|
  |77987860|No data in clipboard.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let sysBoard = getSystemPasteboard()
let dataText1 = "hello"
let pasteData = createData("text/plain", dataText1)
let pasteData_sys = sysBoard.getData()
```

### func getDataSource()

```cangjie
public func getDataSource(): String
```

**功能：** 获取系统剪贴板中的数据的来源。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|系统剪贴板中的数据的来源。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let sysBoard = getSystemPasteboard()
let res = sysBoard.getDataSource()
```

### func hasData()

```cangjie
public func hasData(): Bool
```

**功能：** 判断系统剪贴板中是否有内容。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true表示剪贴板中有内容。false表示剪贴板中没有内容。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let sysBoard = getSystemPasteboard()
let hasRes = sysBoard.hasData()
```

### func hasDataType(String)

```cangjie
public func hasDataType(mimeType: String): Bool
```

**功能：** 检查系统剪贴板中是否有指定的MIME数据类型。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|待查询的数据类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|系统剪贴板中有指定的数据类型返回true，否则返回false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let sysBoard = getSystemPasteboard()
let res = sysBoard.hasDataType(MIMETYPE_TEXT_PLAIN)
```

### func isRemoteData()

```cangjie
public func isRemoteData(): Bool
```

**功能：** 判断剪贴板中的数据是否来自其他设备。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是来自其他设备返回true，否则返回false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let sysBoard = getSystemPasteboard()
let res = sysBoard.isRemoteData()
```