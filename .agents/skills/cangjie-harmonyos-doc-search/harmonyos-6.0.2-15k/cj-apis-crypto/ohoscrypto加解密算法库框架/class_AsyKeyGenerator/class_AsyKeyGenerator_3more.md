## class AsyKeyGenerator

```cangjie
public class AsyKeyGenerator {}
```

**功能：** 非对称密钥生成器。在使用该类的方法前，需要先使用createAsyKeyGenerator()方法构建一个AsyKeyGenerator实例。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop algName

```cangjie
public prop algName: String
```

**功能：** 非对称密钥生成器指定的算法名称。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### func convertKey(?DataBlob, ?DataBlob)

```cangjie
public func convertKey(pubKey: ?DataBlob, priKey: ?DataBlob): KeyPair
```

**功能：** 获取指定数据生成非对称密钥。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pubKey|?[DataBlob](#struct-datablob)|是|-|指定的公钥材料。如果公钥不需要转换，可直接传入None。|
|priKey|?[DataBlob](#struct-datablob)|是|-|指定的私钥材料。如果私钥不需要转换，可直接传入None。|

**返回值：**

|类型|说明|
|:----|:----|
|[KeyPair](#class-keypair)|非对称密钥。|

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

let pubKeyArray: Array<UInt8> = [48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7,
    3, 66, 0, 4, 83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202,
    121, 26, 105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99,
    92, 235, 215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]
let priKeyArray: Array<UInt8> = [48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16,
    27, 4, 171, 57, 10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61,
    3, 1, 7]
let pubKeyBlob = DataBlob(pubKeyArray) // 公钥二进制数据
let priKeyBlob = DataBlob(priKeyArray) // 私钥二进制数据
let asyKeyGenerator = createAsyKeyGenerator('ECC256')
let keyPairData = asyKeyGenerator.convertKey(pubKeyBlob, priKeyBlob)
```