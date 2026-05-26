## class DataBlob

```cangjie
public class DataBlob {
    public DataBlob(
        public var data: Array<UInt8>)
}
```

**功能：** 表示buffer数组。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### var data

```cangjie
public var data: Array<UInt8>
```

**功能：** 表示数据。

**类型：** Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### DataBlob(Array\<UInt8>)

```cangjie
public DataBlob(
    public var data: Array<UInt8>)
```

**功能：** 构造DataBlob实例。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|data|Array\<UInt8>|是|数据。|

## class EncodingBlob

```cangjie
public class EncodingBlob {
    public EncodingBlob(
        public var data: Array<UInt8>,
        public var encodingFormat: UInt32
    )
}
```

**功能：** 表示带编码格式的证书二进制数组。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### var data

```cangjie
public var data: Array<UInt8>
```

**功能：** 表示传入的证书数据。

**类型：** Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### var encodingFormat

```cangjie
public var encodingFormat: UInt32
```

**功能：** 表示指明证书编码格式。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### EncodingBlob(Array\<UInt8>, UInt32)

```cangjie
public EncodingBlob(
    public var data: Array<UInt8>,
    public var encodingFormat: UInt32
)
```

**功能：** 构造EncodingBlob实例。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|data|Array\<UInt8>|是|传入的证书数据。|
|encodingFormat|UInt32|是|指明证书编码格式。|

## class GeneralName

```cangjie
public class GeneralName {
    public GeneralName(
        public var `type`: GeneralNameType,
        public var name: ?Array<UInt8>
    )
}
```

**功能：** 用于表示证书主体信息对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### var \`type`

```cangjie
public var `type`: GeneralNameType
```

**类型：** [GeneralNameType](#enum-generalnametype)

**读写能力：** 可读写

**起始版本：** 19

### var name

```cangjie
public var name: ?Array<UInt8>
```

**功能：** 指定具体的证书主体DER格式内容。

**类型：** ?Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### GeneralName(GeneralNameType, ?Array\<UInt8>)

```cangjie
public GeneralName(
    public var `type`: GeneralNameType,
    public var name: ?Array<UInt8>
)
```

**功能：** 构造GeneralName实例。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[GeneralNameType](#enum-generalnametype)|是|指定具体的证书主体类型。|
|name|?Array\<UInt8>|是|指定具体的证书主体DER格式内容。|