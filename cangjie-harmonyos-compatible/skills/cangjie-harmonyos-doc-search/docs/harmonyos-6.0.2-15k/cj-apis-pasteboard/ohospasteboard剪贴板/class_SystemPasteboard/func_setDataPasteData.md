### func setData(PasteData)

```cangjie
public func setData(data: PasteData): Unit
```

**功能：** 将数据写入系统剪贴板。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[PasteData](#class-pastedata)|是|-|PasteData对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[剪贴板错误码](../../errorcodes/cj-errorcode-pasteboard.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |12900003|Another copy or paste is in progress.|
  |12900004|Replication is prohibited.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let sysBoard = getSystemPasteboard()
let dataText = "hello"
let pasteData = createData("text/plain", dataText)
sysBoard.setData(pasteData)
```