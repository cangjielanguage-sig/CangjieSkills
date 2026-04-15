## class MultiFormData

```cangjie
public class MultiFormData {
    public var name: String
    public var contentType: String
    public var remoteFileName: String
    public var data: HttpData
    public var filePath: String
    public init(name: String, contentType: String,  remoteFileName!: String = "",
        data!: HttpData = HttpData.StringData(""), filePath!: String = "")
}
```

**功能：** 多部分表单数据的类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var contentType

```cangjie
public var contentType: String
```

**功能：** 数据类型，如'text/plain'，'image/png', 'image/jpeg', 'audio/mpeg', 'video/mp4'等。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var data

```cangjie
public var data: HttpData
```

**功能：** 表单数据内容。

**类型：** [HttpData](#enum-httpdata)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var filePath

```cangjie
public var filePath: String
```

**功能：** 此参数将文件路径指向的文件内容设置为表单数据，如果未指定data内容，则必须设置filePath。

> **说明：**
>
> 需传入文件管理模块支持的格式，可以通过文件管理的[access](../CoreFileKit/cj-apis-file_fs.md#static-func-accessstring-accessmodetype-accessflagtype)接口，验证文件是否存在且可访问。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 数据名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var remoteFileName

```cangjie
public var remoteFileName: String
```

**功能：** 上传到服务器保存为文件的名称。

> **说明：**
>
> - 指定该字段后，请求头中会添加filename字段，表示上传到服务器文件的名称。
>
> - （1）当上传数据为文件时，若通过data字段指定文件内容，通常需要设置remoteFileName字段，用以指定上传到服务器文件的名称（实际结果与服务器具体行为有关）；若通过filePath字段指定文件路径，请求头中会自动添加filename字段，其默认值为filePath中的文件名称，如需特殊指定，也可通过本字段对filename重新设置。
>
> - （2）当上传数据为二进制格式时，则必须设置remoteFileName字段。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### init(String, String, String, HttpData, String)

```cangjie
public init(name: String, contentType: String,  remoteFileName!: String = "",
    data!: HttpData = HttpData.StringData(""), filePath!: String = "")
```

**功能：** 构造MultiFormData实例。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|数据名称。|
|contentType|String|是|-|数据类型，如'text/plain'，'image/png', 'image/jpeg', 'audio/mpeg', 'video/mp4'等。|
|remoteFileName|String|否|""|**命名参数。** 上传到服务器保存为文件的名称。|
|data|[HttpData](#enum-httpdata)|否|HttpData.StringData("")|**命名参数。** 表单数据内容。|
|filePath|String|否|""|**命名参数。** 此参数将文件路径指向的文件内容设置为表单数据，如果未指定data内容，则必须设置filePath。|