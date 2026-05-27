## class Random

```cangjie
public class Random {}
```

**功能：** Random类，调用Random方法可以进行随机数计算。调用前，需要通过[createRandom](#func-createrandom)构造Random实例。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### prop algName

```cangjie
public prop algName: String
```

**功能：** 代表当前使用的随机数生成算法，目前只支持“CTR_DRBG"。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### func generateRandom(Int32)

```cangjie
public func generateRandom(len: Int32): DataBlob
```

**功能：** 生成指定长度的随机数并返回。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|len|Int32|是|-|表示生成随机数的长度，单位为byte，范围在[1, INT32_MAX]。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#struct-datablob)|DataBlob对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters.|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let rand = createRandom()
let promiseGenerateRand = rand.generateRandom(12)
```

### func setSeed(DataBlob)

```cangjie
public func setSeed(seed: DataBlob): Unit
```

**功能：** 设置指定的种子。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|seed|[DataBlob](#struct-datablob)|是|-|设置的种子。|

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

let rand = createRandom()
rand.setSeed(DataBlob("test".toArray()))
```