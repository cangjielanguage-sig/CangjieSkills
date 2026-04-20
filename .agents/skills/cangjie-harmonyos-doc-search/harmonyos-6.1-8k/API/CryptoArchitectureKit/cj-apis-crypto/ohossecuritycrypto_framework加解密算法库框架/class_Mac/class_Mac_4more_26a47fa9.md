## class Mac

```cangjie
public class Mac {}
```

**功能：** Mac类，调用Mac方法可以进行MAC（Message Authentication Code）加密计算。调用前，需要通过[createMac](#func-createmacstring)构造Mac实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**起始版本：** 22

### prop algName

```cangjie
public prop algName: String
```

**功能：** 代表指定的摘要算法名。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**起始版本：** 22

### func initialize(SymKey)

```cangjie
public func initialize(key: SymKey): Unit
```

**功能：** 使用对称密钥初始化Mac计算。initialize、update、doFinal为三段式接口，需要成组使用。其中initialize和doFinal必选，update可选。

> **说明：**
>
> - 建议通过[HMAC密钥生成规格](../../security/CryptoArchitectureKit/cj-crypto-sym-key-generation-conversion-spec.md#hmac)创建对称密钥生成器，调用[generateSymKey](#func-createsymkeygeneratorstring)随机生成对称密钥或调用[convertKey](#func-convertkeydatablob)传入与密钥规格长度一致的二进制密钥数据生成密钥。
> - 当指定“HMAC”生成对称密钥生成器时，仅支持调用[convertKey](#func-convertkeydatablob)传入长度在[1,4096]范围内（单位为byte）的任意二进制密钥数据生成密钥。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[SymKey](#class-symkey)|是|-|对称密钥。|

**异常：**

- BusinessException：对应错误码如下表，详见[crypto framework错误码](./cj-errorcode-crypto.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
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
    let skg = createSymKeyGenerator("AES128")
    let sk = skg.generateSymKey()
    let mac = createMac("SHA256")
    mac.initialize(sk)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func doFinal()

```cangjie
public func doFinal(): DataBlob
```

**功能：** 返回Mac的计算结果。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|返回Mac的计算结果。|

**异常：**

- BusinessException：对应错误码如下表，详见[crypto framework错误码](./cj-errorcode-crypto.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17620001 | memory operation failed. |
  | 17620002 | failed to convert parameters between cj and c. |
  | 17630001 | crypto operation error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let mac = createMac("SHA256")

    let skg = createSymKeyGenerator("AES128")
    let sk = skg.generateSymKey()
    mac.initialize(sk)
    let blob = DataBlob("this is test!".toArray())
    mac.update(blob)
    mac.doFinal()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```