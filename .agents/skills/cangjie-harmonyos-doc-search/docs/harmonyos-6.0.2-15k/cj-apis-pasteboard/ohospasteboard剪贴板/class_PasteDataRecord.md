## class PasteDataRecord

```cangjie
public class PasteDataRecord {
    public let htmlText: String
    public let mimeType: String
    public let plainText: String
    public let uri: String
    public let pixelMap: PixelMap
}
```

**功能：** 对于剪贴板中内容记录的抽象定义，称之为条目。剪贴板内容部分由一个或者多个条目构成，例如一条文本内容、一份HTML、一个URI。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

### let htmlText

```cangjie
public let htmlText: String
```

**功能：** HTML内容。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let mimeType

```cangjie
public let mimeType: String
```

**功能：** 数据类型。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let pixelMap

```cangjie
public let pixelMap: PixelMap
```

**功能：** PixelMap内容。

**类型：** [PixelMap](../../apis/ImageKit/cj-apis-image.md#class-pixelmap)

**读写能力：** 只读

**起始版本：** 12

### let plainText

```cangjie
public let plainText: String
```

**功能：** 纯文本内容。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let uri

```cangjie
public let uri: String
```

**功能：** URI内容。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### func toPlainText()

```cangjie
public func toPlainText(): String
```

**功能：** 将一个PasteData中的内容强制转换为文本内容。

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

let uri = "dataability:///com.example.myapplication1/user.txt"
let pasteData = createData(MIMETYPE_TEXT_URI, uri)
let record = pasteData.getRecord(0)
let text = record.toPlainText()
```