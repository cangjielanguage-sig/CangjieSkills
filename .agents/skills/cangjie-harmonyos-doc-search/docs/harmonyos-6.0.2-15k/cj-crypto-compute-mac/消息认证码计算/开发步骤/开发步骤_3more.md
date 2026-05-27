## 开发步骤

在调用update接口传入数据时，可以[一次性传入所有数据](#hmac一次性传入)，也可以把数据人工分段，然后[分段update](#分段hmac)。对于同一段数据而言，是否分段，计算结果没有差异。对于数据量较大的数据，开发者可以根据实际需求选择是否分段传入。

下面分别提供两种方式的示例代码。

### HMAC（一次性传入）

1. 调用[createMac](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createmacstring)，指定摘要算法SHA256，生成消息认证码实例（Mac）。

2. 调用[createSymKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createsymkeygeneratorstring)、[convertKey](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-convertkeydatablob)，生成密钥算法为HMAC的对称密钥（SymKey）。
   生成对称密钥的详细开发指导，请参见[指定二进制数据生成对称密钥](./cj-crypto-convert-binary-data-to-sym-key.md)。

3. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initsymkey)，指定共享对称密钥（SymKey），初始化Mac对象。

4. 调用[update](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-updatedatablob-1)，传入自定义消息，进行消息认证码计算。单次update长度没有限制。

5. 调用[doFinal](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-dofinal)，获取Mac计算结果。

6. 调用[getMacLength](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-getmaclength)，获取Mac消息认证码的长度，单位为字节。

### 以一次性传入数据，获取消息认证码计算结果为例

```cangjie
import kit.CryptoArchitectureKit.*

func genSymKeyByData(symKeyData: Array<UInt8>) {
    let symKeyBlob: DataBlob = DataBlob(symKeyData)
    let aesGenerator = createSymKeyGenerator('HMAC')
    let symKey = aesGenerator.convertKey(symKeyBlob)
    AppLog.info('convertKey success')
    return symKey
}

func doHmacBySync() {
    // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节
    let keyData = "12345678abcdefgh".toArray()
    let key = genSymKeyByData(keyData)
    let macAlgName = 'SHA256' // 摘要算法名
    let message = 'hmacTestMessgae' // 待进行HMAC的数据
    let mac = createMac(macAlgName)
    mac.`init`(key)
    // 数据量较少时，可以只做一次update，将数据全部传入，接口未对入参长度做限制
    mac.update(DataBlob(keyData))
    let macResult = mac.doFinal()
    AppLog.info('[Sync]HMAC result: ${macResult.data}')
    let macLen = mac.getMacLength()
    AppLog.info('HMAC len: ${macLen}')
}
```