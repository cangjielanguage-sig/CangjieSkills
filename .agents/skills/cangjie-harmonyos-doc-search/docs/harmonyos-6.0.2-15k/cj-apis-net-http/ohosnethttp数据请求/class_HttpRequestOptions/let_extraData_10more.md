### let extraData

```cangjie
public let extraData: ?HttpData = None
```

**功能：** 发送请求的额外数据，默认无此字段。

- 当HTTP请求为POST、PUT等方法时，此字段为HTTP请求的content，以UTF-8编码形式作为请求体。
    - 当'content-Type'为'application/x-www-form-urlencoded'时，请求提交的信息主体数据应在key和value进行URL转码后按照键值对"key1=value1&key2=value2&key3=value3"的方式进行编码，该字段对应的类型通常为String。
    - 当'content-Type'为'text/xml'时，该字段对应的类型通常为String。
    - 当'content-Type'为'application/json'时，该字段对应的类型通常为Object。
    - 当'content-Type'为'application/octet-stream'时，该字段对应的类型通常为ArrayBuffer。
    - 当'content-Type'为'multipart/form-data'且需上传的字段为文件时，该字段对应的类型通常为ArrayBuffer。
- 当HTTP请求为GET、OPTIONS、DELETE、TRACE、CONNECT等方法时，此字段为HTTP请求参数的补充。开发者需传入Encode编码后的string类型参数，Object类型的参数无需预编码，参数内容会拼接到URL中进行发送；ArrayBuffer类型的参数不会做拼接处理。

以上信息仅供参考，并可能根据具体情况有所不同。

**类型：** ?[HttpData](#enum-httpdata)

**读写能力：** 只读

**起始版本：** 12

### let header

```cangjie
public let header: ?HashMap<String, String> = None
```

**功能：** HTTP请求头字段。默认{'content-Type': 'application/json'}。

**类型：** ?HashMap\<String,String>

**读写能力：** 只读

**起始版本：** 12

### let maxLimit

```cangjie
public let maxLimit: UInt32 = 5 * 1024 * 1024
```

**功能：** 响应消息的最大字节限制，默认值为5MB，以字节为单位。最大值为10MB，以字节为单位。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let method

```cangjie
public let method: RequestMethod = RequestMethod.GET
```

**功能：** 请求方式，默认为GET。

**类型：** [RequestMethod](#enum-requestmethod)

**读写能力：** 只读

**起始版本：** 12

### let multiFormDataList

```cangjie
public let multiFormDataList: ?Array<MultiFormData> = None
```

**功能：** 当'content-Type'为'multipart/form-data'时，则上传该字段定义的数据字段表单列表。

**类型：** ?Array\<[MultiFormData](#class-multiformdata)>

**读写能力：** 只读

**起始版本：** 12

### let priority

```cangjie
public let priority: UInt32 = 1
```

**功能：** 优先级，范围[1,1000]，默认是1。若传参超出范围则使用默认值1。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let readTimeout

```cangjie
public let readTimeout: UInt32 = 60000
```

**功能：** 读取超时时间。单位为毫秒（ms），默认为60000ms。<br />设置为0表示不会出现超时情况。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let resumeFrom

```cangjie
public let resumeFrom: ?Int64 = None
```

**功能：** 用于设置上传或下载起始位置。HTTP标准（RFC 7233第3.1节）允许服务器忽略范围请求。<br />使用HTTP PUT时设置此参数，可能出现未知问题。<br />取值范围是:1~4294967296(4GB)，超出范围则不生效。无默认值。

**类型：** ?Int64

**读写能力：** 只读

**起始版本：** 12

### let resumeTo

```cangjie
public let resumeTo: ?Int64 = None
```

**功能：** 用于设置上传或下载结束位置。HTTP标准（RFC 7233第3.1节）允许服务器忽略范围请求。<br />使用HTTP PUT时设置此参数，可能出现未知问题。<br />取值范围是:1~4294967296(4GB)，超出范围则不生效。无默认值。

**类型：** ?Int64

**读写能力：** 只读

**起始版本：** 12

### let usingCache

```cangjie
public let usingCache: Bool = true
```

**功能：** 是否使用缓存，默认为true，请求时优先读取缓存。 缓存跟随当前进程生效。新缓存会替换旧缓存。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12