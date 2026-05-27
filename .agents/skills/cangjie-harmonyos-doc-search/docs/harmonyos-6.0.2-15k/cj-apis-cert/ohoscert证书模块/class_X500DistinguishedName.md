## class X500DistinguishedName

```cangjie
public class X500DistinguishedName {
    public func getName(): String
    public func getName(typeName: String): Array<String>
    public func getEncoded(): EncodingBlob
}
```

**功能：** X509定义的Name类型的对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### func getEncoded()

```cangjie
public func getEncoded(): EncodingBlob
```

**功能：** 获取X509证书扩展域的数据。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[EncodingBlob](#class-encodingblob)|X509证书序列化数据。|

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

let nameStr = '/CN=John Doe/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS'
let dgName = createX500DistinguishedName(nameStr)
let dgData = dgName.getEncoded().data
```

### func getName(String)

```cangjie
public func getName(typeName: String): Array<String>
```

**功能：** 获取可分辨名的字符串。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|typeName|String|是|指定类型的名称。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|可分辨名的字符串。|

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

let nameStr = '/CN=John Doe/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS'
let dgName = createX500DistinguishedName(nameStr)
let name2 = dgName.getName("CN")
```

### func getName()

```cangjie
public func getName(): String
```

**功能：** 获取可分辨名的字符串。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|可分辨名的字符串。|

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

let nameStr = '/CN=John Doe/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS'
let dgName = createX500DistinguishedName(nameStr)
let name = dgName.getName()
```