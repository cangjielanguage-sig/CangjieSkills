## class SymKeyGenerator

```cangjie
public class SymKeyGenerator {}
```

**功能：** 对称密钥生成器。

在使用该类的方法前，需要先使用[createSymKeyGenerator](#func-createsymkeygeneratorstring)方法构建一个symKeyGenerator实例。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### prop algName

```cangjie
public prop algName: String
```

**功能：** 对称密钥生成器指定的算法名称。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### func convertKey(DataBlob)

```cangjie
public func convertKey(key: DataBlob): SymKey
```

**功能：** 根据指定数据生成对称密钥。

必须在使用[createSymKeyGenerator](#func-createsymkeygeneratorstring)创建对称密钥生成器后，才能使用本函数。

> **说明：**
>
> 对于HMAC算法的对称密钥，如果已经在创建对称密钥生成器时指定了具体哈希算法（如指定“HMAC|SHA256”），则需要传入与哈希长度一致的二进制密钥数据（如传入SHA256对应256位的密钥数据）。
> 如果在创建对称密钥生成器时没有指定具体哈希算法，如仅指定“HMAC”，则支持传入长度在[1,4096]范围内（单位为byte）的任意二进制密钥数据。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[DataBlob](#struct-datablob)|是|-|指定的密钥材料数据。|

**返回值：**

|类型|说明|
|:----|:----|
|[SymKey](#class-symkey)|返回对称密钥SymKey。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters.|
  |17620001|memory error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let arr: Array<UInt8> = [0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56, 0xad, 0x47, 0xfc, 0x5a,
    0x46, 0x39, 0xee, 0x7c, 0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72] // keyLen = 192 (24 bytes)
let symAlgName = "3DES192"
let symKeyGenerator = createSymKeyGenerator(symAlgName)
symKeyGenerator.convertKey(DataBlob(arr))
```

### func generateSymKey()

```cangjie
public func generateSymKey(): SymKey
```

**功能：** 获取该对称密钥生成器随机生成的密钥。

必须在使用[createSymKeyGenerator](#func-createsymkeygeneratorstring)创建对称密钥生成器后，才能使用本函数。

目前支持使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[SymKey](#class-symkey)|对称密钥SymKey。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17620001|memory error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let symAlgName = "AES128"
let symKeyGenerator = createSymKeyGenerator(symAlgName)
let symKey = symKeyGenerator.generateSymKey()
```