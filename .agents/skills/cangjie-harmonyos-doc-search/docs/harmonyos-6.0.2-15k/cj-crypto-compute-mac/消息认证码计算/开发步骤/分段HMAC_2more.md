### 分段HMAC

1. 调用[createMac](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createmacstring)，指定摘要算法SHA256，生成消息认证码实例（Mac）。

2. 调用[createSymKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createsymkeygeneratorstring)，生成密钥算法为HMAC的对称密钥（SymKey）。
   生成对称密钥的详细开发指导，请参见[指定二进制数据生成对称密钥](./cj-crypto-convert-binary-data-to-sym-key.md)。

3. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initsymkey)，指定共享对称密钥（SymKey），初始化Mac对象。

4. 传入自定义消息，将一次传入数据量设置为20字节，多次调用[update](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-updatedatablob-1)，进行消息认证码计算。

5. 调用[doFinal](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-dofinal)，获取Mac计算结果。

6. 调用[getMacLength](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-getmaclength)，获取Mac消息认证码的长度，单位为字节。

### 以分段传入数据，获取消息认证码计算结果为例

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
    let message = 'aaaaa.....bbbbb.....ccccc.....ddddd.....eee'.toArray() // 待进行HMAC的数据
    let mac = createMac(macAlgName)
    mac.`init`(key)
    let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求
    let size = message.size
    // 数据量较少时，可以只做一次update，将数据全部传入，接口未对入参长度做限制
    for (i in 0..size : updateLength) {
        let len = if (i + updateLength > size) {
            size
        } else {
            i + updateLength
        }
        let updateMessage = message[i..len]
        let updateMessageBlob: DataBlob = DataBlob(updateMessage)
        mac.update(updateMessageBlob)
    }
    let macResult = mac.doFinal()
    AppLog.info('[Sync]HMAC result: ${macResult.data}')
    let macLen = mac.getMacLength()
    AppLog.info('HMAC len: ${macLen}')
}
```