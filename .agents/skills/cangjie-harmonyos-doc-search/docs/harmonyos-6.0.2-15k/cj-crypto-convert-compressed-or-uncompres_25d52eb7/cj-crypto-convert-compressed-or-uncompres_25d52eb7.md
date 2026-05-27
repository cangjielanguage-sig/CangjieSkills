# 使用ECC压缩/非压缩公钥格式转换（仓颉）

可通过指定ECC公钥数据，生成公钥对象（PubKey）；也可从公钥对象（PubKey）中，获取ECC公钥数据。
当前仅支持ECC算法中，满足X509规范的压缩/非压缩格式的公钥数据。此处的公钥数据应当是完整的X509公钥，对于只使用点数据的情况，请参见[使用ECC压缩/非压缩点格式转换](./cj-crypto-convert-compressed-or-uncompressed-ECC-point.md)。
ECC的算法规格请参见[非对称密钥生成和转换规格：ECC](./cj-crypto-asym-key-generation-conversion-spec.md#ecc)。
通过传入字符串参数format，可指定需要获取的ECC公钥数据格式。如果需要获取满足X509规范的压缩格式数据，则指定format为："X509|COMPRESSED"；如果需要获取非压缩格式，则指定format为："X509|UNCOMPRESSED"。

## 指定非压缩公钥数据转换为压缩公钥数据

1. 指定Uint8Array类型的ECC非压缩公钥数据，封装成DataBlob对象。

公钥和私钥可只传入其中一个，此处示例以传入非压缩公钥为例。

1. 调用[createAsyKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorstring)，指定字符串参数'ECC_BrainPoolP256r1'，创建密钥算法为ECC、密钥长度为256位的非对称密钥生成器（AsyKeyGenerator）。

2. 调用[convertKey](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-convertkeydatablob-datablob)，传入封装后的DataBlob对象，生成非对称密钥对象（KeyPair）。

3. 调用[getEncodedDer](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-getencodedderstring-1)，设置参数为'X509|COMPRESSED'，获取压缩公钥数据的字节流。

```cangjie
import kit.CryptoArchitectureKit.*

func eccPubUncompressedToCompressed() {
    let pkData: Array<UInt8> = [48, 90, 48, 20, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 9, 43, 36, 3, 3, 2, 8, 1, 1, 7, 3,
        66, 0, 4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195, 157,
        111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242,
        206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152]
    let pubKeyBlob: DataBlob = DataBlob(pkData)
    let generator = createAsyKeyGenerator('ECC_BrainPoolP256r1')
    let keyPair = generator.convertKey(pubKeyBlob, None)
    let returnBlob = keyPair.pubKey.getEncodedDer('X509|COMPRESSED')
    AppLog.info('returnBlob data：${returnBlob.data}')
}
```
