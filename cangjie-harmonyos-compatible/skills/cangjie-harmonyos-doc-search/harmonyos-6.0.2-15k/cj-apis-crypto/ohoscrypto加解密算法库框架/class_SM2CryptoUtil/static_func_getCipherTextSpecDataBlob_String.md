### static func getCipherTextSpec(DataBlob, String)

```cangjie
public static func getCipherTextSpec(cipherText: DataBlob, mode!: String = "C1C3C2"): SM2CipherTextSpec
```

**功能：** 从符合国密标准的ASN.1格式的SM2密文中，获取具体的SM2密文参数。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cipherText|[DataBlob](#struct-datablob)|是|-|符合国密标准的ASN.1格式的SM2密文。|
|mode|String|否|"C1C3C2"| **命名参数。** 可选的密文转换模式，可用于指定密文参数的拼接顺序，当前仅支持默认值"C1C3C2"。|

**返回值：**

|类型|说明|
|:----|:----|
|[SM2CipherTextSpec](#class-sm2ciphertextspec)|返回具体的SM2密文参数。|

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

let cipherText: Array<UInt8> = [48, 118, 2, 32, 45, 153, 88, 82, 104, 221, 226, 43, 174, 21, 122, 248, 5, 232, 105, 41,
    92, 95, 102, 224, 216, 149, 85, 236, 110, 6, 64, 188, 149, 70, 70, 183, 2, 32, 107, 93, 198, 247, 119, 18, 40, 110,
    90, 156, 193, 158, 205, 113, 170, 128, 146, 109, 75, 17, 181, 109, 110, 91, 149, 5, 110, 233, 209, 78, 229, 96, 4,
    32, 87, 167, 167, 247, 88, 146, 203, 234, 83, 126, 117, 129, 52, 142, 82, 54, 152, 226, 201, 111, 143, 115, 169,
    125, 128, 42, 157, 31, 114, 198, 109, 244, 4, 14, 100, 227, 78, 195, 249, 179, 43, 70, 242, 69, 169, 10, 65, 123]
let spec = SM2CryptoUtil.getCipherTextSpec(DataBlob(cipherText))
```