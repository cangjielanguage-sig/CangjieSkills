## class Md

```cangjie
public class Md {}
```

**功能：** Md类，调用Md方法可以进行MD（Message Digest）摘要计算。调用前，需要通过[createMd](#func-createmdstring)构造Md实例。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### prop algName

```cangjie
public prop algName: String
```

**功能：** 代表指定的摘要算法名。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### func digest()

```cangjie
public func digest(): DataBlob
```

**功能：** 返回Md的计算结果。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#struct-datablob)|返回计算结果DataBlob。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let md = createMd("SHA256")
let blob: DataBlob = DataBlob("test".toArray())
md.update(blob)
let res = md.digest()
```

### func getMdLength()

```cangjie
public func getMdLength(): UInt32
```

**功能：** 获取Md消息摘要长度（字节数）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回md计算结果的字节长度。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let md = createMd("SHA256")
let mdLen = md.getMdLength()
```

### func update(DataBlob)

```cangjie
public func update(input: DataBlob): Unit
```

**功能：** 传入消息进行Md更新计算。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|input|[DataBlob](#struct-datablob)|是|-|传入的消息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let md = createMd("SHA256")
let blob: DataBlob = DataBlob("test".toArray())
md.update(blob)
```