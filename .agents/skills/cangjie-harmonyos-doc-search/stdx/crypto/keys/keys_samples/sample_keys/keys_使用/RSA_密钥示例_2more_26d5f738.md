## RSA 密钥示例

### 生成 rsa 公钥及私钥，并使用公钥的 OAEP 填充模式加密，用私钥的 OAEP 填充模式解密

示例：

<!-- verify -->
```cangjie
import stdx.crypto.keys.*
import stdx.crypto.digest.*
import std.io.*
import std.crypto.digest.*

main() {
    var rsaPri = RSAPrivateKey(2048)
    var rsaPub = RSAPublicKey(rsaPri)

    var str: String = "hello world, hello cangjie"
    var bas1 = ByteBuffer()
    var bas2 = ByteBuffer()
    var bas3 = ByteBuffer()
    bas1.write(str.toArray())

    var encOpt = OAEPOption(SHA1(), SHA256())
    rsaPub.encrypt(bas1, bas2, padType: OAEP(encOpt))
    var encOpt2 = OAEPOption(SHA1(), SHA256())
    rsaPri.decrypt(bas2, bas3, padType: OAEP(encOpt2))

    var buf = Array<Byte>(str.size, repeat: 0)
    bas3.read(buf)
    if (str.toArray() == buf) {
        println("success")
    } else {
        println("fail")
    }
}
```

运行结果：

```text
success
```

### 从文件中读取 rsa 公钥和私钥，并使用私钥的 PKCS1 填充模式签名，用公钥的 PKCS1 填充模式验证签名结果

**说明：**
>
> - 需要自行准备公私钥文件。

示例：

<!-- compile -->
```cangjie
import stdx.crypto.keys.*
import stdx.crypto.digest.*
import std.crypto.digest.*
import std.fs.*
import std.io.*

main() {
    var pemPri = String.fromUtf8(readToEnd(File("./files/rsaPri.pem", Read)))
    var rsaPri = RSAPrivateKey.decodeFromPem(pemPri)

    var pemPub = String.fromUtf8(readToEnd(File("./files/rsaPub.pem", Read)))
    var rsaPub = RSAPublicKey.decodeFromPem(pemPub)

    var str: String = "helloworld"
    var sha512Instance = SHA512()
    sha512Instance.write(str.toArray())
    var md: Array<Byte> = sha512Instance.finish()

    var sig = rsaPri.sign(sha512Instance, md, padType: PKCS1)
    if (rsaPub.verify(sha512Instance, md, sig, padType: PKCS1)) {
        println("verify successful")
    }
}
```

运行结果：

```text
verify successful
```

## ECDSA 密钥示例

### 生成 ECDSA 公钥及私钥，并使用私钥签名，公钥验证签名结果

示例：

<!-- verify -->
```cangjie
import stdx.crypto.keys.*
import stdx.crypto.digest.*
import std.convert.*
import std.crypto.digest.*

main() {
    var ecPri = ECDSAPrivateKey(P224)
    var ecPub = ECDSAPublicKey(ecPri)

    var str: String = "helloworld"
    var sha512Instance = SHA512()
    sha512Instance.write(str.toArray())
    var md: Array<Byte> = sha512Instance.finish()

    var sig = ecPri.sign(md)
    if (ecPub.verify(md, sig)) {
        println("verify successful")
    }
}
```

运行结果：

```text
verify successful
```