### func getMacLength()

```cangjie
public func getMacLength(): UInt32
```

**功能：** 获取Mac消息认证码的长度（字节数）。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回mac计算结果的字节长度。|

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
    let mac = createMac("SHA256")
    let skg = createSymKeyGenerator("AES128")
    let sk = skg.generateSymKey()
    mac.initialize(sk)
    let blob = DataBlob("this is test!".toArray())
    mac.update(blob)
    mac.doFinal()
    var macLen = mac.getMacLength()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func update(DataBlob)

```cangjie
public func update(input: DataBlob): Unit
```

**功能：** 传入消息进行Mac更新消息认证码状态。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

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
    let mac = createMac("SHA256")
    let skg = createSymKeyGenerator("AES128")
    let sk = skg.generateSymKey()
    mac.initialize(sk)
    let blob = DataBlob("this is test!".toArray())
    mac.update(blob)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```