## class MultiFormData

```cangjie
public class MultiFormData {
    public MultiFormData(
        public let name: String,
        public let contentType: String,
        public let remoteFileName!: ?String = None,
        public let data!: ?HttpData = None,
        public let filePath!: ?String = None
    ) {}
}
```

**功能：** 多部分表单数据的类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### let contentType

```cangjie
public let contentType: String
```

**功能：** 数据类型，如'text/plain'，'image/png', 'image/jpeg', 'audio/mpeg', 'video/mp4'等。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let data

```cangjie
public let data: ?HttpData = None
```

**功能：** 表单数据内容。

**类型：** ?[HttpData](#enum-httpdata)

**读写能力：** 只读

**起始版本：** 12

### let filePath

```cangjie
public let filePath: ?String = None
```

**功能：** 此参数根据文件的内容设置mime部件的正文内容。用于代替data将文件数据设置为数据内容，如果data为空，则必须设置filePath。如果data有值，则filePath不会生效。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 数据名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let remoteFileName

```cangjie
public let remoteFileName: ?String = None
```

**功能：** 上传到服务器保存为文件的名称。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### MultiFormData(String, String, ?String, ?HttpData, ?String)

```cangjie
public MultiFormData(
    public let name: String,
    public let contentType: String,
    public let remoteFileName!: ?String = None,
    public let data!: ?HttpData = None,
    public let filePath!: ?String = None
)
```

**功能：** 构造MultiFormData实例。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|数据名称。|
|contentType|String|是|-|数据类型，如'text/plain'，'image/png', 'image/jpeg', 'audio/mpeg', 'video/mp4'等。|
|remoteFileName|?String|否|None| **命名参数。** 上传到服务器保存为文件的名称。|
|data|?[HttpData](#enum-httpdata)|否|None| **命名参数。** 表单数据内容。|
|filePath|?String|否|None| **命名参数。** 此参数根据文件的内容设置mime部件的正文内容。用于代替data将文件数据设置为数据内容，如果data为空，则必须设置filePath。如果data有值，则filePath不会生效。|