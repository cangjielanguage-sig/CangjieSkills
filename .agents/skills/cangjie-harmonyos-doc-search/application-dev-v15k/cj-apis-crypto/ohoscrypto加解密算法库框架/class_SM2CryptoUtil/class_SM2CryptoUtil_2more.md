## class SM2CryptoUtil

```cangjie
public class SM2CryptoUtil {}
```

**功能：** 用于SM2密码学运算的工具类。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### static func genCipherTextBySpec(SM2CipherTextSpec, String)

```cangjie
public static func genCipherTextBySpec(spec: SM2CipherTextSpec, mode!: String = "C1C3C2"): DataBlob
```

**功能：** 根据指定的SM2密文参数，生成符合国密标准的ASN.1格式的SM2密文。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|spec|[SM2CipherTextSpec](#class-sm2ciphertextspec)|是|-|指定的SM2密文参数。|
|mode|String|否|"C1C3C2"| **命名参数。** 可选的密文转换模式，可用于指定密文参数的拼接顺序，当前仅支持默认值"C1C3C2"。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#struct-datablob)|返回符合国密标准的ASN.1格式的SM2密文。|

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
import std.math.numeric.BigInt

let xCoordinate = BigInt("20625015362595980457695435345498579729138244358573902431560627260141789922999")
let yCoordinate = BigInt("48563164792857017065725892921053777369510340820930241057309844352421738767712")
let cipherTextData: Array<UInt8> = [100, 227, 78, 195, 249, 179, 43, 70, 242, 69, 169, 10, 65, 123]
let hashData: Array<UInt8> = [87, 167, 167, 247, 88, 146, 203, 234, 83, 126, 117, 129, 52, 142, 82, 54, 152, 226, 201,
    111, 143, 115, 169, 125, 128, 42, 157, 31, 114, 198, 109, 244]
let spec = SM2CipherTextSpec(
    xCoordinate: xCoordinate,
    yCoordinate: yCoordinate,
    cipherTextData: cipherTextData,
    hashData: hashData
)
let data = SM2CryptoUtil.genCipherTextBySpec(spec)
```