### func generateSymKey()

```cangjie
public func generateSymKey(): SymKey
```

**功能：** 获取对称密钥生成器随机生成的密钥。

必须在使用[createSymKeyGenerator](#func-createsymkeygeneratorstring)创建对称密钥生成器后，才能使用本函数。

目前支持使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。

> **说明：**
>
> - 对于HMAC算法的对称密钥，如果已经在创建对称密钥生成器时指定了具体哈希算法（如指定“HMAC|SHA256”），则会随机生成与哈希长度一致的二进制密钥数据（如指定“HMAC|SHA256”会随机生成256位的密钥数据）。
> - 如果在创建对称密钥生成器时没有指定具体哈希算法，如仅指定“HMAC”，则不支持随机生成对称密钥数据，可通过[convertKey](#func-convertkeydatablob)方式生成对称密钥数据。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[SymKey](#class-symkey)|返回对称密钥SymKey。|

**异常：**

- BusinessException：对应错误码如下表，详见[crypto framework错误码](./cj-errorcode-crypto.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17620001 | memory operation failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let symAlgName = "AES128"
    let symKeyGenerator = createSymKeyGenerator(symAlgName)
    let symKey = symKeyGenerator.generateSymKey()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```