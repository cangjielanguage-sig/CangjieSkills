## func createMac(String)

```cangjie
public func createMac(algName: String): Mac
```

**功能：** 生成Mac实例，用于消息认证码的计算与操作。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指定摘要算法。|

**返回值：**

|类型|说明|
|:----|:----|
|[Mac](#class-mac)|返回由输入算法指定生成的[Mac](#class-mac)对象。|

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
    var mac = createMac("SHA256")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func createMd(String)

```cangjie
public func createMd(algName: String): Md
```

**功能：** 生成Md实例，用于进行消息摘要的计算与操作。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指定摘要算法。|

**返回值：**

|类型|说明|
|:----|:----|
|[Md](#class-md)|返回由输入算法指定生成的[Md](#class-md)对象。|

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
    let md = createMd("SHA256")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func createRandom()

```cangjie
public func createRandom(): Random
```

**功能：** 生成Random实例，用于进行随机数的计算与设置种子。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Random](#class-random)|返回由输入算法指定生成的[Random](#class-random)对象。|

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
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```