## class SymKey

```cangjie
public class SymKey <: Key {}
```

**功能：** 对称密钥，是[Key](#interface-key)的子类，在对称加解密时需要将其对象传入[Cipher](#class-cipher)实例的[init()](#func-initcryptomode-key-paramsspec)方法使用。

对称密钥可以通过对称密钥生成器[SymKeyGenerator](#class-symkeygenerator)来生成。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**父类型：**

- [Key](#interface-key)

### func clearMem()

```cangjie
public func clearMem(): Unit
```

**功能：** 同步方法，将系统底层内存中的的密钥内容清零。建议在不需要使用对称密钥实例时，调用本函数，避免内存中密钥数据存留过久。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let generator = createSymKeyGenerator("3DES192")
let key = generator.generateSymKey()
var encodedKey = key.getEncoded()
AppLog.info("key blob: ${encodedKey.data}") // Display key content.
key.clearMem()
encodedKey = key.getEncoded()
AppLog.info("key blob: ${encodedKey.data}") // Display all 0s.
```