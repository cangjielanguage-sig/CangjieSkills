### var extraData

```cangjie
public var extraData: HttpData
```

**功能：** 发送请求的额外数据。

> **说明：**
>
> 没有额外数据时，避免添加该参数；若必须添加，避免直接传入空字符串或者空数组。

1. 当HTTP请求为POST、PUT、DELETE等方法时，此字段为HTTP请求的content，以UTF-8编码形式作为请求体。

    示例如下：

    (1) 当'content-Type'为'application/x-www-form-urlencoded'时，请求提交的信息主体数据必须在key和value进行URL转码后（encodeURIComponent/encodeURI），按照键值对"key1=value1&key2=value2&key3=value3"的方式进行编码，该字段对应的类型通常为String。

    (2) 当'content-Type'为'text/xml'时，该字段对应的类型通常为String。

    (3) 当'content-Type'为'application/json'时，该字段对应的类型通常为Object。

    (4) 当'content-Type'为'application/octet-stream'时，该字段对应的类型通常为ArrayBuffer。

    (5) 当'content-Type'为'multipart/form-data'且需上传的字段为文件时，该字段对应的类型通常为ArrayBuffer。

    以上信息仅供参考，并可能根据具体情况有所不同。

2. 当HTTP请求为GET、OPTIONS、TRACE、CONNECT等方法时，此字段为HTTP请求参数的补充。开发者需传入Encode编码后的string类型参数，Object类型的参数无需预编码，参数内容会拼接到URL中进行发送。ArrayBuffer类型的参数不会做拼接处理。

**类型：** [HttpData](#enum-httpdata)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var header

```cangjie
public var header: HashMap<String, String>
```

**功能：** HTTP请求头字段。当请求方式为"POST" "PUT" "DELETE" 或者""时，默认{'content-Type': 'application/json'}， 否则默认{'content-Type': 'application/x-www-form-urlencoded'}。<br />如果head中包含number类型的字段，最大支持int64的整数。

**类型：** HashMap\<String,String>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var maxLimit

```cangjie
public var maxLimit: UInt32
```

**功能：** 响应消息的最大字节限制。<br />最大值为100\*1024\*1024，以字节为单位。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var method

```cangjie
public var method: RequestMethod
```

**功能：** 请求方式，默认为Get。

**类型：** [RequestMethod](#enum-requestmethod)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var multiFormDataList

```cangjie
public var multiFormDataList: Array<MultiFormData>
```

**功能：** 当'content-Type'为'multipart/form-data'时，则上传该字段定义的数据字段表单列表。

**类型：** Array\<[MultiFormData](#class-multiformdata)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var priority

```cangjie
public var priority: UInt32
```

**功能：** HTTP/HTTPS请求并发优先级，值越大优先级越高，范围[1,1000]。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var readTimeout

```cangjie
public var readTimeout: UInt32
```

**功能：** 读取超时时间。单位为毫秒（ms）。传入值需为uint32_t范围内的整数。<br />设置为0表示不会出现超时情况。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22