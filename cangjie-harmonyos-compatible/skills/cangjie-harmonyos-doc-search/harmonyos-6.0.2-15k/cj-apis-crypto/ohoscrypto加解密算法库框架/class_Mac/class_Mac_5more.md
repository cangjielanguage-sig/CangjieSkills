## class Mac

```cangjie
public class Mac {}
```

**功能：** Mac类，调用Mac方法可以进行MAC（Message Authentication Code）加密计算。调用前，需要通过[createMac](#func-createmacstring)构造Mac实例。

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

### func \`init\`(SymKey)

```cangjie
public func `init`(key: SymKey): Unit
```

**功能：** 使用对称密钥初始化[Mac](#class-mac)计算，通过注册回调函数获取结果。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[SymKey](#class-symkey)|是|-|共享对称密钥。|

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

let skg = createSymKeyGenerator("AES128")
let sk = skg.generateSymKey()
let mac = createMac("SHA256")
mac.`init`(sk)
```

### func doFinal()

```cangjie
public func doFinal(): DataBlob
```

**功能：** 返回Mac的计算结果。

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

let mac = createMac("SHA256")

let skg = createSymKeyGenerator("AES128")
let sk = skg.generateSymKey()
mac.`init`(sk)
let blob = DataBlob("this is test!".toArray())
mac.update(blob)
mac.doFinal()
```

### func getMacLength()

```cangjie
public func getMacLength(): UInt32
```

**功能：** 获取Mac消息认证码的长度（字节数）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回mac计算结果的字节长度。|

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

let mac = createMac("SHA256")
let skg = createSymKeyGenerator("AES128")
let sk = skg.generateSymKey()
mac.`init`(sk)
let blob = DataBlob("this is test!".toArray())
mac.update(blob)
mac.doFinal()
var macLen = mac.getMacLength()
```