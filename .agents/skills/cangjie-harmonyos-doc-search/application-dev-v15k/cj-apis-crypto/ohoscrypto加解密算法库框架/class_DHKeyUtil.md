## class DHKeyUtil

```cangjie
public class DHKeyUtil {}
```

**功能：** 根据素数P的长度和私钥长度（bit位数）生成DH公共密钥参数。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### static func genDHCommonParamsSpec(Int32, Int32)

```cangjie
public static func genDHCommonParamsSpec(pLen: Int32, skLen!: Int32 = 0): DHCommonParamsSpec
```

**功能：** 根据素数P的长度和私钥长度（bit位数）生成DH公共密钥参数。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pLen|Int32|是|-|用于指定DH公共密钥参数中素数P的长度，单位为bit。|
|skLen|Int32|否|0| **命名参数。** 用于指定DH公共密钥参数中私钥的长度，单位为bit。|

**返回值：**

|类型|说明|
|:----|:----|
|[DHCommonParamsSpec](#class-dhcommonparamsspec)|返回DH公共密钥参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |801|this operation is not supported.|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let dHCommonParamsSpec = DHKeyUtil.genDHCommonParamsSpec(2048)
```