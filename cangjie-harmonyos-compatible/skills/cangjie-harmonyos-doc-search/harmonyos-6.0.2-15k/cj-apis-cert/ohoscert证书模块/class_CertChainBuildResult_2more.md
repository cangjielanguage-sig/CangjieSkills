## class CertChainBuildResult

```cangjie
public class CertChainBuildResult {}
```

**功能：** 用于指定证书链创建结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### let certChain

```cangjie
public let certChain: X509CertChain
```

**功能：** 生成的证书链对象。

**类型：** [X509CertChain](#class-x509certchain)

**读写能力：** 只读

**起始版本：** 19

### let validationResult

```cangjie
public let validationResult: CertChainValidationResult
```

**功能：** 指定最终证书链的最大长度。

**类型：** [CertChainValidationResult](#class-certchainvalidationresult)

**读写能力：** 只读

**起始版本：** 19

## class CertChainData

```cangjie
public class CertChainData {
    public CertChainData(
        public var data: Array<UInt8>,
        public var count: UInt32,
        public var encodingFormat: UInt32
    )
}
```

**功能：** 表示证书链数据，在证书链校验时，作为入参传入。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### var count

```cangjie
public var count: UInt32
```

**功能：** 表示传入的数据中，包含的证书数量。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var data

```cangjie
public var data: Array<UInt8>
```

**功能：** 表示证书数据，按照长度(2字节)-数据的形式传入，如：08ABCDEFGH07ABCDEFG,第一本证书，前2个字节表示证书的长度为8字节，后面附加8字节的证书数据；第2本证书前2个字节表示证书的长度为7字节，后面附加7字节的证书数据。

**类型：** Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### var encodingFormat

```cangjie
public var encodingFormat: UInt32
```

**功能：** 表示证书编码格式。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### CertChainData(Array\<UInt8>, UInt32, UInt32)

```cangjie
public CertChainData(
    public var data: Array<UInt8>,
    public var count: UInt32,
    public var encodingFormat: UInt32
)
```

**功能：** 构造CertChainData实例。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|data|Array\<UInt8>|是|证书数据，按照长度(2字节)-数据的形式传入，如：08ABCDEFGH07ABCDEFG,第一本证书，前2个字节表示证书的长度为8字节，后面附加8字节的证书数据；第2本证书前2个字节表示证书的长度为7字节，后面附加7字节的证书数据。|
|count|UInt32|是|传入的数据中，包含的证书数量。|
|encodingFormat|UInt32|是|指明证书编码格式。|