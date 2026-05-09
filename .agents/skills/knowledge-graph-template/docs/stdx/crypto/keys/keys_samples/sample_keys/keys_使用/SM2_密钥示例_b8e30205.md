## SM2 密钥示例

### 生成 SM2 公钥及私钥，并使用私钥签名，公钥验证签名结果

示例：

<!-- verify -->
```cangjie
import stdx.crypto.keys.*
import stdx.crypto.digest.*
import std.convert.*
import std.crypto.digest.*
import std.fs.*
import std.io.*

main(): Unit {
    /* 无参生成公钥私钥 */
    let sm2PrivateKey = SM2PrivateKey()
    let sm2PublicKey = SM2PublicKey(sm2PrivateKey)

    /* 公钥和私钥导出 */
    let priPem = sm2PrivateKey.encodeToPem()
    let file1: File = File("./sm2Pri.pem", Write)
    file1.write(priPem.encode().toArray())
    file1.close()

    let pubPem = sm2PublicKey.encodeToPem()
    let file2: File = File("./sm2Pub.pem", Write)
    file2.write(pubPem.encode().toArray())
    file2.close()

    /* 公钥加密，私钥解密 */
    let str: String = "helloworld"
    let encresult = sm2PublicKey.encrypt(str.toArray())
    let decresult = sm2PrivateKey.decrypt(encresult)
    println(String.fromUtf8(decresult))

    /* 私钥签名，公钥验证 */
    let strSig: String = "helloworld"
    let sigRe = sm2PrivateKey.sign(strSig.toArray())
    let verifyre = sm2PublicKey.verify(strSig.toArray(), sigRe)
    println(verifyre)

    /* 私钥公钥导入 */
    let pemPri = String.fromUtf8(readToEnd(File("./sm2Pri.pem", Read)))
    let sm2PrivateKeyNew = SM2PrivateKey.decodeFromPem(pemPri)
    println(sm2PrivateKeyNew)
    let pemPub = String.fromUtf8(readToEnd(File("./sm2Pub.pem", Read)))
    let sm2PublicKeyNew = SM2PublicKey.decodeFromPem(pemPub)
    println(sm2PublicKeyNew)
}
```

运行结果：

```text
helloworld
true
SM2 PRIVATE KEY
SM2 PUBLIC KEY
```