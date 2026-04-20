### func getEncodedPem(String)

```cangjie
public func getEncodedPem(format: String): String
```

**功能：** 获取密钥数据的字符串。密钥可以为RSA公钥或者私钥。其中，公钥格式满足X.509规范、PKCS#1规范和PEM编码格式。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|format|String|是|-|指定的获取密钥字符串的编码格式。其中，公钥可为'PKCS1' 或'X509'格式。|

**返回值：**

|类型|说明|
|:----|:----|
|String|用于获取指定密钥格式的具体内容。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters.  Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let publicPkcs1Str1024 = "-----BEGIN RSA PUBLIC KEY-----\n"
    + "MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n"
    + "h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n"
    + "SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n"
    + "-----END RSA PUBLIC KEY-----\n"
let rsaGenerator = createAsyKeyGenerator("RSA1024")
let keyPair = rsaGenerator.convertPemKey(publicPkcs1Str1024, None)
let pubPemKey = keyPair.pubKey
let pubString = pubPemKey.getEncodedPem("X509")
```