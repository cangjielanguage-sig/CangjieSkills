## func createMac(String)

```cangjie
public func createMac(algName: String): Mac
```

**功能：** 生成Mac实例，用于进行消息认证码的计算与操作。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指定摘要算法。|

**返回值：**

|类型|说明|
|:----|:----|
|[Mac](#class-mac)|返回由输入算法指定生成的Mac对象。|

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

var mac = createMac("SHA256")
```

## func createMd(String)

```cangjie
public func createMd(algName: String): Md
```

**功能：** 生成Md实例，用于进行消息摘要的计算与操作。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指定摘要算法。|

**返回值：**

|类型|说明|
|:----|:----|
|[Md](#class-md)|返回由输入算法指定生成的[Md](#class-md)对象。|

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

let md = createMd("SHA256")
```

## func createRandom()

```cangjie
public func createRandom(): Random
```

**功能：** 生成Random实例，用于进行随机数的计算与设置种子。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[Random](#class-random)|返回由输入算法指定生成的[Random](#class-random)对象。|

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
```

## func createSign(String)

```cangjie
public func createSign(algName: String): Sign
```

**功能：** Sign实例生成。

支持的规格详见[签名验签规格](../../../../Dev_Guide/security/CryptoArchitectureKit/cj-crypto-sign-sig-verify-overview.md)。

**系统能力：** SystemCapability.Security.CryptoFramework.Sign

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指定签名算法：RSA，ECC，DSA或SM2。使用RSA PKCS1模式时需要设置摘要，使用RSA PSS模式时需要设置摘要和掩码摘要。|

**返回值：**

|类型|说明|
|:----|:----|
|[Sign](#class-sign)|返回由输入算法指定生成的Sign对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters.|
  |801|this operation is not supported.|
  |17620001|memory error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj
import kit.CryptoArchitectureKit.*

var sign = createSign("ECC224|SHA256")
```