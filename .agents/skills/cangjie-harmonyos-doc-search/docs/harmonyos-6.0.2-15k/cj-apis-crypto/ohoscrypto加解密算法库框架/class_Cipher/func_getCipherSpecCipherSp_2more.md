### func getCipherSpec(CipherSpecItem)

```cangjie
public func getCipherSpec(itemType: CipherSpecItem): ResultSpec
```

**功能：** 获取加解密参数。当前只支持RSA算法和SM2算法。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemType|[CipherSpecItem](#enum-cipherspecitem)|是|-|用于指定需要获取的加解密参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[ResultSpec](#enum-resultspec)|获取的加解密参数的具体值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |801|this operation is not supported.|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let cipherAlgName = "RSA|PKCS1_OAEP|SHA256|MGF1_SHA1"
let cipher = createCipher(cipherAlgName)
let syg = createSymKeyGenerator("AES128")
let sk = syg.generateSymKey()
cipher.`init`(CryptoMode.ENCRYPT_MODE, sk, None)
let mdName = cipher.getCipherSpec(OAEP_MD_NAME_STR)
```

### func setCipherSpec(CipherSpecItem, Array\<UInt8>)

```cangjie
public func setCipherSpec(itemType: CipherSpecItem, itemValue: Array<UInt8>): Unit
```

**功能：** 设置加解密参数。常用的加解密参数可以直接通过[createCipher](#func-createcipherstring) 来指定，剩余参数可以通过本接口指定。当前只支持RSA算法。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemType|[CipherSpecItem](#enum-cipherspecitem)|是|-|用于指定需要设置的加解密参数。|
|itemValue|Array\<UInt8>|是|-|用于指定加解密参数的具体值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |801|this operation is not supported.|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let cipherAlgName = "RSA|PKCS1_OAEP|SHA256|MGF1_SHA1"
let cipher = createCipher(cipherAlgName)
let syg = createSymKeyGenerator("AES128")
let sk = syg.generateSymKey()
cipher.`init`(CryptoMode.ENCRYPT_MODE, sk, None)
let pSource: Array<UInt8> = [1, 2, 3, 4]
cipher.setCipherSpec(OAEP_MGF1_PSRC_UINT8ARR, pSource)
```