### func setVerifySpec(SignSpecItem, Int32)

```cangjie
public func setVerifySpec(itemType: SignSpecItem, itemValue: Int32): Unit
```

**功能：** 设置验签参数。常用的签名参数可以直接通过[createVerify](#func-createverifystring) 来指定，剩余参数可以通过本接口指定。

只支持RSA算法、SM2算法，支持SM2算法设置验签参数。

验签的参数应当与签名的参数保持一致。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemType|[SignSpecItem](#enum-signspecitem)|是|-|用于指定需要设置的验签参数。|
|itemValue|Int32|是|-|用于指定验签参数的具体值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  | 错误码ID | 错误信息               |
  | :-------- | :---------------------- |
  | 401 | invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  | 801 | this operation is not supported.          |
  | 17620001 | memory error.          |
  | 17630001 | crypto operation error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let keyGenAlg = "RSA1024"
let generator = createAsyKeyGenerator(keyGenAlg)
let keyPair = generator.generateKeyPair()
let verifyAlg = "RSA1024|PKCS1|SHA256"
let verifier = createVerify(verifyAlg)
verifier.initialize(keyPair.pubKey)
let setN = 20i32
verifier.setVerifySpec(PSS_SALT_LEN_NUM, setN)
```

### func setVerifySpec(SignSpecItem, Array\<UInt8>)

```cangjie
public func setVerifySpec(itemType: SignSpecItem, itemValue: Array<UInt8>): Unit
```

**功能：** 设置验签参数。常用的签名参数可以直接通过[createVerify](#func-createverifystring) 来指定，剩余参数可以通过本接口指定。

只支持RSA算法、SM2算法，支持SM2算法设置验签参数。

验签的参数应当与签名的参数保持一致。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemType|[SignSpecItem](#enum-signspecitem)|是|-|用于指定需要设置的验签参数。|
|itemValue|Array\<UInt8>|是|-|用于指定验签参数的具体值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  | 错误码ID | 错误信息               |
  | :-------- | :---------------------- |
  | 401 | invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  | 801 | this operation is not supported.          |
  | 17620001 | memory error.          |
  | 17630001 | crypto operation error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let keyGenAlg = "RSA1024"
let generator = createAsyKeyGenerator(keyGenAlg)
let keyPair = generator.generateKeyPair()
let verifyAlg = "RSA1024|PKCS1|SHA256"
let verifier = createVerify(verifyAlg)
verifier.initialize(keyPair.pubKey)
verifier.setVerifySpec(PSS_SALT_LEN_NUM, [1])
```