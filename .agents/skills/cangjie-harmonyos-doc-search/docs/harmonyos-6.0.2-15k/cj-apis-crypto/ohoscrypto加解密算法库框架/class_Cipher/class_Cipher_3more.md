## class Cipher

```cangjie
public class Cipher {}
```

**功能：** 提供加解密的算法操作功能，按序调用本类中的[init()](#func-initcryptomode-key-paramsspec)、[update()](#func-updatedatablob)、[doFinal()](#func-dofinaldatablob)方法，可以实现对称加密/对称解密/非对称加密/非对称解密。

一次完整的加/解密流程在对称加密和非对称加密中略有不同：

- 对称加解密：init为必选，update为可选（且允许多次update加/解密大数据），doFinal为必选；doFinal结束后可以重新init开始新一轮加/解密流程。
- RSA、SM2非对称加解密：init为必选，不支持update操作，doFinal为必选（允许连续多次doFinal加/解密大数据）；RSA不支持重复init，切换加解密模式或填充方式时，需要重新创建Cipher对象。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### prop algName

```cangjie
public prop algName: String
```

**功能：** 加解密生成器指定的算法名称。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### func \`init\`(CryptoMode, Key, ?ParamsSpec)

```cangjie
public func `init`(opMode: CryptoMode, key: Key, params: ?ParamsSpec): Unit
```

**功能：** 初始化加解密的[cipher](#class-cipher)对象，通过注册回调函数获取结果。

必须在使用[createCipher](#func-createcipherstring)创建[Cipher](#class-cipher)实例后，才能使用本函数。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|opMode|[CryptoMode](#enum-cryptomode)|是|-|加密或者解密模式。|
|key|[Key](#interface-key)|是|-|指定加密或解密的密钥。|
|params|?[ParamsSpec](#interface-paramsspec)|是|-|指定加密或解密的参数，对于ECB等没有参数的算法模式，可以传入None。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters.|
  |17620001|memory error.|
  |17620002|runtime error.|
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
```