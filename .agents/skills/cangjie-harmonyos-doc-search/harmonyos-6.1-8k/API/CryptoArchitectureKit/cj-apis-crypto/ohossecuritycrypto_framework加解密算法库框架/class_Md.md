## class Md

```cangjie
public class Md {}
```

**功能：** Md类，调用Md方法可以进行MD（Message Digest）摘要计算。调用前，需要通过[createMd](#func-createmdstring)构造Md实例。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

**起始版本：** 22

### prop algName

```cangjie
public prop algName: String
```

**功能：** 代表指定的摘要算法名。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

**起始版本：** 22

### func digest()

```cangjie
public func digest(): DataBlob
```

**功能：** 返回Md的计算结果。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|返回计算结果DataBlob。|

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
    let md = createMd("SHA256")
    let blob: DataBlob = DataBlob("test".toArray())
    md.update(blob)
    let res = md.digest()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getMdLength()

```cangjie
public func getMdLength(): UInt32
```

**功能：** 获取Md消息摘要长度（字节数）。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回md计算结果的字节长度。|

**异常：**

- BusinessException：对应错误码如下表，详见[crypto framework错误码](./cj-errorcode-crypto.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17630001 | crypto operation error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let md = createMd("SHA256")
    let mdLen = md.getMdLength()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func update(DataBlob)

```cangjie
public func update(input: DataBlob): Unit
```

**功能：** 传入消息进行Md更新摘要状态。update和digest为两段式接口，需要成组使用。其中digest必选，update可选。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|input|[DataBlob](#class-datablob)|是|-|传入的消息。|

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
    let md = createMd("SHA256")
    let blob: DataBlob = DataBlob("test".toArray())
    md.update(blob)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```