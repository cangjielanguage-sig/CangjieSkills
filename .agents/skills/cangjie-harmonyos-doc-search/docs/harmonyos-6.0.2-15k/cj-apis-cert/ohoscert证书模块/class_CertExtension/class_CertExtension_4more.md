## class CertExtension

```cangjie
public class CertExtension {}
```

**功能：** 证书扩展域段类。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### func checkCA()

```cangjie
public func checkCA(): Int32
```

**功能：** 表示校验证书是否为CA证书。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|当证书扩展域段中密钥用途包含签名用途，并且基本约束中cA字段为true时，表示证书为CA证书。如果不是CA，则返回-1；否则返回基本约束中的路径长度。如果证书是CA证书，但是基本约束中未给定路径长度，则返回-2，表示无路径长度限制。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |19020001|memory error.|
  |19020002|runtime error.|
  |19030001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let extensionData: Array<UInt8> = [0x30, 0x40, 0x30, 0x0F, 0x06] //example data
let ext = createCertExtension(EncodingBlob(extensionData, EncodingFormat.FORMAT_DER))
let ca = ext.checkCA()
```

### func getEncoded()

```cangjie
public func getEncoded(): EncodingBlob
```

**功能：** 表示获取证书扩展域段序列化数据。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[EncodingBlob](#class-encodingblob)|表示证书扩展域段序列化数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |19020001|memory error.|
  |19020002|runtime error.|
  |19030001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let extensionData: Array<UInt8> = [0x30, 0x40, 0x30, 0x0F, 0x06] //example data
let ext = createCertExtension(EncodingBlob(extensionData, EncodingFormat.FORMAT_DER))
let extData = ext.getEncoded().data
```

### func getEntry(ExtensionEntryType, DataBlob)

```cangjie
public func getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob
```

**功能：** 表示获取证书扩展域段对象信息。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|valueType|[ExtensionEntryType](#enum-extensionentrytype)|是|表示证书扩展域段获取的类型。|
|oid|[DataBlob](#class-datablob)|是|表示证书扩展域段获取的对象标识符。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示证书扩展域段对象的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |19020001|memory error.|
  |19020002|runtime error.|
  |19030001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let extensionData: Array<UInt8> = [0x30, 0x40, 0x30, 0x0F, 0x06] //example data
let ext = createCertExtension(EncodingBlob(extensionData, EncodingFormat.FORMAT_DER))
let entryData = ext.getEntry(ExtensionEntryType.EXTENSION_ENTRY_TYPE_ENTRY, DataBlob("demo_str".toArray())).data
```