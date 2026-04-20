## class SymKey

```cangjie
public class SymKey <:  Key {}
```

**功能：** 对称密钥，是[Key](#interface-key)的子类，在对称加解密时需要将其对象传入[Cipher](#class-cipher)实例的[initialize()](#func-initializecryptomode-key-paramsspec)方法使用。

对称密钥可以通过对称密钥生成器[SymKeyGenerator](#class-symkeygenerator)来生成。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**起始版本：** 22

**父类型：**

- [Key](#interface-key)

### prop algName

```cangjie
public prop algName: String
```

**功能：** 对称密钥生成器指定的算法名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**起始版本：** 22

### prop format

```cangjie
public prop format: String
```

**功能：** 密钥的格式。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**起始版本：** 22

### func clearMem()

```cangjie
public func clearMem(): Unit
```

**功能：** 将系统底层内存中的密钥内容清零。建议在不再使用对称密钥实例时调用此函数，避免密钥数据在内存中存留过久。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let generator = createSymKeyGenerator("3DES192")
    let key = generator.generateSymKey()
    var encodedKey = key.getEncoded()
    Hilog.info(0, "AppLogCj", "key blob: ${encodedKey.data}") // Display key content.
    key.clearMem()
    encodedKey = key.getEncoded()
    Hilog.info(0, "AppLogCj", "key blob: ${encodedKey.data}") // Display all 0s.
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getEncoded()

```cangjie
public func getEncoded(): DataBlob
```

**功能：** 获取密钥数据的字节流。密钥可以为对称密钥，公钥或者私钥。其中，公钥格式满足ASN.1语法、X.509规范、DER编码格式；私钥格式满足ASN.1语法，PKCS#8规范、DER编码方式。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|用于查看密钥的具体内容。|

**异常：**

- BusinessException：对应错误码如下表，详见[crypto framework错误码](./cj-errorcode-crypto.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | this operation is not supported. |
  | 17620001 | memory operation failed. |
  | 17630001 | crypto operation error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let generator = createSymKeyGenerator("3DES192")
    let key = generator.generateSymKey()
    var encodedKey = key.getEncoded()
    Hilog.info(0, "AppLogCj", "key blob: ${encodedKey.data}") // Display key content.
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```