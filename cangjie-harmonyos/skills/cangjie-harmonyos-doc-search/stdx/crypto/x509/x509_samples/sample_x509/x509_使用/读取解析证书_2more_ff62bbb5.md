## 读取、解析证书

> **说明：**
>
> 需要自行准备证书文件。

示例：

<!-- compile -->
```cangjie
import std.fs.File
import stdx.crypto.x509.*

let readPath = "./files/root_rsa.cer"

main() {
    /* 读取本地证书*/
    let pem = String.fromUtf8(File.readFrom(readPath))
    let certificates = X509Certificate.decodeFromPem(pem)

    /* 解析证书中的必选字段 */
    let cert = certificates[0]
    println(cert)
    println("Serial Number: ${cert.serialNumber}")
    println("Issuer: ${cert.issuer}")
    println("NotBefore: ${cert.notBefore}")
    println("NotAfter: ${cert.notAfter}")
    println(cert.signatureAlgorithm)
    let signature = cert.signature
    println(signature.hashCode())
    println(cert.publicKeyAlgorithm)
    let pubKey = cert.publicKey
    println(pubKey.encodeToPem().encode())

    /* 解析证书中的扩展字段 */
    println("DNSNames: ${cert.dnsNames}")
    println("EmailAddresses: ${cert.emailAddresses}")
    println("IPAddresses: ${cert.IPAddresses}")
    println("KeyUsage: ${cert.keyUsage}")
    println("ExtKeyUsage: ${cert.extKeyUsage}")

    /* 解析证书使用者的可辨识名称 */
    println("Subject: ${cert.subject}")

    return 0
}
```

## 读取、验证证书

> **说明：**
>
> 需要自行准备证书文件。

示例：

<!-- compile -->
```cangjie
import std.fs.File
import stdx.crypto.x509.*
import std.time.DateTime

let prefixPath = "./files/"
let certFile = "servers.crt"
let rootFile = "roots.crt"
let middleFile = "middles.crt"

func getX509Cert(path: String) {
    let pem = String.fromUtf8(File.readFrom(path))
    X509Certificate.decodeFromPem(pem)
}

func testVerifyByTime(cert: X509Certificate, roots: Array<X509Certificate>, middles: Array<X509Certificate>) {
    var opt = VerifyOption()
    opt.roots = roots
    opt.intermediates = middles
    cert.verify(opt)
    println("Verify result: ${cert.verify(opt)}")
    opt.time = DateTime.of(year: 2023, month: 7, dayOfMonth: 1)
    println("Verify result:: ${cert.verify(opt)}")
}

func testVerifyByDNS(cert: X509Certificate) {
    var opt = VerifyOption()
    opt.dnsName = "www.example.com"
    println("cert DNS names: ${cert.dnsNames}")
    let res = cert.verify(opt)
    println("Verify result: ${res}")
}

/**
 * The relation of certs.
 *    root[0]         root[1]
 *    /      \            |
 *  mid[0]  mid[1]    mid[2]
 *   |                  |
 *  server[0]         server[1]
 */
func testVerify(cert: X509Certificate, roots: Array<X509Certificate>, middles: Array<X509Certificate>) {
    var opt = VerifyOption()
    opt.roots = roots
    opt.intermediates = middles
    let res = cert.verify(opt)
    println("Verify result: ${res}")
}

main() {
    /* 两个服务端证书 */
    let certs = getX509Cert(prefixPath + certFile)
    /* 两个根证书 */
    let roots = getX509Cert(prefixPath + rootFile)
    /* 三个中间证书 */
    let middles = getX509Cert(prefixPath + middleFile)
    /* 验证有效期 */
    testVerifyByTime(certs[0], [roots[0]], [middles[0]])
    /* 验证 DNS 域名 */
    testVerifyByDNS(certs[0])

    /* 根据根证书和中间证书验证其有效性 */
    /* cert0 <- root0: false */
    testVerify(certs[0], [roots[0]], [])
    /* cert0 <- middle0 <- root0: true */
    testVerify(certs[0], [roots[0]], [middles[0]])
    /* cert0 <- (middle0, middle1, middle2) <- (root0, root1) : true */
    testVerify(certs[0], roots, middles)
    /* cert1 <- middle0 <- root0: false */
    testVerify(certs[1], [roots[0]], [middles[0]])
    /* cert1 <- middle2 <- root1: true */
    testVerify(certs[1], [roots[1]], [middles[2]])
    /* cert1 <- (middle0, middle1, middle2) <- (root0, root1) : true */
    testVerify(certs[1], roots, middles)
    return 0
}
```