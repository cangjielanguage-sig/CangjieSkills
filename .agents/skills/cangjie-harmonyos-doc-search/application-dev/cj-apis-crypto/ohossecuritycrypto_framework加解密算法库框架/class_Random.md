## class Random

```cangjie
public class Random {}
```

**功能：** Random类，调用Random方法可以进行随机数计算。调用前，需要通过[createRandom](#func-createrandom)构造Random实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

**起始版本：** 22

### prop algName

```cangjie
public prop algName: String
```

**功能：** 代表当前使用的随机数生成算法，目前只支持“CTR_DRBG"。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

**起始版本：** 22

### func generateRandom(Int32)

```cangjie
public func generateRandom(len: Int32): DataBlob
```

**功能：** 生成指定长度的随机数。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|len|Int32|是|-|表示生成随机数的长度，单位为byte，范围在[1, INT32_MAX]。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示生成的随机数。|

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
    let rand = createRandom()
    let randomData = rand.generateRandom(12)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func setSeed(DataBlob)

```cangjie
public func setSeed(seed: DataBlob): Unit
```

**功能：** 设置指定的种子。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|seed|[DataBlob](#class-datablob)|是|-|设置的种子。|

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
    let rand = createRandom()
    rand.setSeed(DataBlob("test".toArray()))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```