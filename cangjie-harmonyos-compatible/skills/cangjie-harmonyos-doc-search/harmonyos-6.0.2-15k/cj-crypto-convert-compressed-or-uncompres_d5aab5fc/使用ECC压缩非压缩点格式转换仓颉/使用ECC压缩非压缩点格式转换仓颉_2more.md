# 使用ECC压缩/非压缩点格式转换（仓颉）

支持将压缩/非压缩的点数据，转换为Point对象，用于密钥对象生成；也支持将Point对象转换为压缩/非压缩的点数据。
ECC的算法规格请参见[非对称密钥生成和转换规格：ECC](./cj-crypto-asym-key-generation-conversion-spec.md#ecc)
通过传入字符串参数format，可指定需要获取的点数据格式。如果需要获取压缩格式，则指定format为："COMPRESSED"；需要获取非压缩格式，则指定format为："UNCOMPRESSED"。

## 指定非压缩点数据转换为压缩点数据

1. 指定Uint8Array类型的ECC非压缩点数据，调用[convertPoint](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#static-func-convertpointstring-arrayuint8)对象，用于生成点数据。
2. 调用[getEncodedPoint](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#static-func-getencodedpointstring-point-string)，获取压缩点数据。

```cangjie
import kit.CryptoArchitectureKit.*

func eccPointUncompressedToCompressed() {
    let pkData: Array<UInt8> = [4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76,
        63, 8, 195, 157, 111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85,
        228, 123, 242, 206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152]
    let returnPoint = ECCKeyUtil.convertPoint('NID_brainpoolP256r1', pkData)
    AppLog.info('convertPoint success')
    let returnData = ECCKeyUtil.getEncodedPoint('NID_brainpoolP256r1', returnPoint, 'COMPRESSED')
    AppLog.info('returnData: ${returnData}') // (因为y为偶数，所以压缩点数据的前缀是02)returnData: 2,143,39,57,249,145,50,63,222,35,70,178,121,202,154,21,146,129,75,76,63,8,195,157,111,40,217,215,148,120,224,205,82
}
```