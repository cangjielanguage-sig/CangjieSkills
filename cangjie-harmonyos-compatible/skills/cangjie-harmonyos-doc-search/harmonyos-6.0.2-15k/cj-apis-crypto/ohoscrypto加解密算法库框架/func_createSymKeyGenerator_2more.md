## func createSymKeyGenerator(String)

```cangjie
public func createSymKeyGenerator(algName: String): SymKeyGenerator
```

**功能：** 通过指定算法名称的字符串，获取相应的对称密钥生成器实例。

支持的规格详见[对称密钥生成和转换规格](../../../../Dev_Guide/security/CryptoArchitectureKit/cj-crypto-sym-key-generation-conversion-spec.md)。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|待生成对称密钥生成器的算法名称。具体取值详见[对称密钥生成和转换规格](../../../../Dev_Guide/security/CryptoArchitectureKit/cj-crypto-sym-key-generation-conversion-spec.md)一节中的“字符串参数”。|

**返回值：**

|类型|说明|
|:----|:----|
|[SymKeyGenerator](#class-symkeygenerator)|返回对称密钥生成器的对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息               |
  | :-------- | :---------------------- |
  | 801 | this operation is not supported. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let symKeyGenerator = createSymKeyGenerator("3DES192")
```

## func createVerify(String)

```cangjie
public func createVerify(algName: String): Verify
```

**功能：** Verify实例生成。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指定签名算法：RSA，ECC，DSA，SM2或ED25519。使用RSA PKCS1模式时需要设置摘要，使用RSA PSS模式时需要设置摘要和掩码摘要。<br/>使用RSA算法验签时，通过设置Recover参数可支持对签名后数据进行验签恢复。|

**返回值：**

|类型|说明|
|:----|:----|
|[Verify](#class-verify)|返回由输入算法指定生成的Verify对象。|

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

let verifyer1 = createVerify('RSA1024|PKCS1|SHA256')
let verifyer2 = createVerify('RSA1024|PSS|SHA256|MGF1_SHA256')
let verifyer3 = createVerify('RSA1024|PKCS1|SHA256|Recover')
```