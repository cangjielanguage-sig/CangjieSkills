## class FormItem

```cangjie
public class FormItem {
    public FormItem(
        public var name!: String,
        public var value!: FormItemValueType
    )
}
```

**功能：** 上传/下载任务的配置信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

### var name

```cangjie
public var name: String
```

**功能：** 表单参数名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var value

```cangjie
public var value: FormItemValueType
```

**功能：** 表单参数值。

**类型：** [FormItemValueType](#enum-formitemvaluetype)

**读写能力：** 可读写

**起始版本：** 12

### FormItem(String, FormItemValueType)

```cangjie
public FormItem(
    public var name!: String,
    public var value!: FormItemValueType
)
```

**功能：** 创建FormItem对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-| **命名参数。** 表单参数名。|
|value|[FormItemValueType](#enum-formitemvaluetype)|是|-| **命名参数。** 表单参数值。|

## class HttpResponseMessage

```cangjie
public class HttpResponseMessage {
    public let version: String,
    public let statusCode: Int32,
    public let reason: String,
    public let headers: HashMap<String, Array<String>>
}
```

**功能：** 任务响应头的数据结构。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

### let headers

```cangjie
public let headers: HashMap<String, Array<String>>
```

**功能：** Http响应头部。

**类型：** HashMap\<String, Array\<String>>

**读写能力：** 只读

**起始版本：** 15

### let reason

```cangjie
public let reason: String
```

**功能：** Http响应原因。

**类型：** String

**读写能力：** 只读

**起始版本：** 15

### let statusCode

```cangjie
public let statusCode: Int32
```

**功能：** Http响应状态码。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 15

### let version

```cangjie
public let version: String
```

**功能：** Http版本。

**类型：** String

**读写能力：** 只读

**起始版本：** 15