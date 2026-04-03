## class ECCKeyUtil

```cangjie
public class ECCKeyUtil {}
```

**功能：** 根据椭圆曲线名生成相应的非对称公共密钥参数。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### static func convertPoint(String, Array\<UInt8>)

```cangjie
public static func convertPoint(curveName: String, encodedPoint: Array<UInt8>): Point
```

**功能：** 根据椭圆曲线的曲线名，即相应的NID(Name IDentifier)，将指定的点数据转换为Point对象。当前支持压缩/非压缩格式的点数据。

> **说明：**
>
> 由RFC5480规范可知：
>
> - 非压缩的点数据，表示为：前缀0x04\|x坐标\|y坐标。
> - 对于Fp素数域（当前暂不支持F2m域）上的非压缩点数据，当坐标y是奇数时，表示为：前缀0x03|x坐标；当坐标y是偶数时，表示为：前缀0x02|x坐标。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|curveName|String|是|-|椭圆曲线的曲线名，即相应的NID(Name IDentifier)。|
|encodedPoint|Array\<UInt8>|是|-|指定的ECC椭圆曲线上的点的数据。|

**返回值：**

|类型|说明|
|:----|:----|
|[Point](#class-point)|返回ECC的Point对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let pkData: Array<UInt8> = [4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63,
    8, 195, 157, 111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123,
    242, 206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152]
let returnPoint = ECCKeyUtil.convertPoint('NID_brainpoolP256r1', pkData)
```

### static func genECCCommonParamsSpec(String)

```cangjie
public static func genECCCommonParamsSpec(curveName: String): ECCCommonParamsSpec
```

**功能：** 根据椭圆曲线相应的NID(Name IDentifier)字符串名称生成相应的非对称公共密钥参数。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|curveName|String|是|-|椭圆曲线相应的NID(Name IDentifier)字符串名称。|

**返回值：**

|类型|说明|
|:----|:----|
|[ECCCommonParamsSpec](#class-ecccommonparamsspec)|返回ECC公共密钥参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters.  Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let eCCCommonParamsSpec = ECCKeyUtil.genECCCommonParamsSpec('NID_brainpoolP160r1')
```