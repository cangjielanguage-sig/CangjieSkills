### func getOidList(ExtensionOidType)

```cangjie
public func getOidList(valueType: ExtensionOidType): Array<DataBlob>
```

**功能：** 表示获取证书扩展域段对象标识符列表。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|valueType|[ExtensionOidType](#enum-extensionoidtype)|是|表示证书扩展域段对象标识符类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[DataBlob](#class-datablob)>|表示证书扩展域段对象标识符列表。|

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
let oid = ext.getOidList(ExtensionOidType.EXTENSION_OID_TYPE_ALL)
```

### func hasUnsupportedCriticalExtension()

```cangjie
public func hasUnsupportedCriticalExtension(): Bool
```

**功能：** 判断是否存在不支持的关键扩展。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当存在不支持的关键扩展时，该方法返回true，否则返回false。|

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
let hasExt = ext.hasUnsupportedCriticalExtension()
```