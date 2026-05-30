## func createCipher(String)

```cangjie
public func createCipher(transformation: String): Cipher
```

**功能：** 通过指定算法名称，获取相应的[Cipher](#class-cipher)实例。

支持的规格详见[对称密钥加解密算法规格](../../../../Dev_Guide/security/CryptoArchitectureKit/cj-crypto-sym-encrypt-decrypt-spec.md)和[非对称密钥加解密算法规格](../../../../Dev_Guide/security/CryptoArchitectureKit/cj-crypto-asym-encrypt-decrypt-spec.md)。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|transformation|String|是|-|待生成Cipher的算法名称（含密钥长度）、加密模式以及填充方法的组合。|

**返回值：**

|类型|说明|
|:----|:----|
|[Cipher](#class-cipher)|返回加解密生成器的对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters.|
  |801|this operation is not supported.|
  |17620001|memory error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let cipherAlgName = "3DES192|ECB|PKCS7"
let cipher = createCipher(cipherAlgName)
```

## func createKdf(String)

```cangjie
public func createKdf(algName: String): Kdf
```

**功能：** 密钥派生函数（key derivation function）实例生成。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指定密钥派生算法（包含HMAC配套的散列函数）：目前支持PBKDF2、HKDF算法，如"PBKDF2MagIc_StrINgSHA256", "HKDFMagIc_StrINgSHA256"。|

**返回值：**

|类型|说明|
|:----|:----|
|[Kdf](#class-kdf)|返回由输入算法指定生成的Kdf对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |801|this operation is not supported.|
  |17620001|memory error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj
import kit.CryptoArchitectureKit.*

let kdf = createKdf('PBKDF2|SHA256')
```

## func createKeyAgreement(String)

```cangjie
public func createKeyAgreement(algName: String): KeyAgreement
```

**功能：** KeyAgreement实例生成。

**系统能力：** SystemCapability.Security.CryptoFramework.KeyAgreement

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指定密钥协商算法：目前支持ECC，X25519和DH。|

**返回值：**

|类型|说明|
|:----|:----|
|[KeyAgreement](#class-keyagreement)|返回由输入算法指定生成的KeyAgreement对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |801|this operation is not supported.|
  |17620001|memory error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj
import kit.CryptoArchitectureKit.*

let keyAgreement = createKeyAgreement('ECC256')
```