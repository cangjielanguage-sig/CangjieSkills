### static func getEncodedPoint(String, Point, String)

```cangjie
public static func getEncodedPoint(curveName: String, point: Point, format: String): Array<UInt8>
```

**功能：** 根据椭圆曲线的曲线名，即相应的NID(Name IDentifier)，按照指定的点数据格式，将Point对象转换为点数据。当前支持压缩/非压缩格式的点数据。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|curveName|String|是|-|椭圆曲线的曲线名，即相应的NID(Name IDentifier)。|
|point|[Point](#class-point)|是|-|椭圆曲线上的Point点对象。|
|format|String|是|-|需要获取的点数据格式，当前支持"COMPRESSED"或"UNCOMPRESSED"。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|返回指定格式的点数据。|

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
import kit.CryptoArchitectureKit.Point as CpPoint
import std.math.numeric.BigInt

let generator = createAsyKeyGenerator("ECC_BrainPoolP256r1")
let keyPair = generator.generateKeyPair()
let eccPkX = keyPair.pubKey.getAsyKeySpec(ECC_PK_X_BN)
let eccPkY = keyPair.pubKey.getAsyKeySpec(ECC_PK_Y_BN)
let returnPoint = CpPoint(
    x: BigInt(eccPkX.toString()),
    y: BigInt(eccPkY.toString())
)
let returnData = ECCKeyUtil.getEncodedPoint('NID_brainpoolP256r1', returnPoint, 'UNCOMPRESSED')
```