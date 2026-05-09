## 创建、解析证书

> **说明：**
>
> 需要自行准备根证书文件。

示例：

<!-- compile -->
```cangjie
import std.fs.*
import stdx.crypto.x509.*
import std.time.*
import std.io.*

main() {
    let x509Name = X509Name(
        countryName: "CN",
        provinceName: "beijing",
        localityName: "haidian",
        organizationName: "organization",
        organizationalUnitName: "organization unit",
        commonName: "x509",
        email: "test@email.com"
    )
    let serialNumber = SerialNumber(length: 20)
    let startTime: DateTime = DateTime.now()
    let endTime: DateTime = startTime.addYears(1)
    let ip1: IP = [8, 8, 8, 8]
    let ip2: IP = [0, 1, 0, 1, 0, 1, 0, 1, 0, 8, 0, 8, 0, 8, 0, 8]
    let parentCertPem = String.fromUtf8(readToEnd(File("./certificate.pem", Read)))
    let parentCert = X509Certificate.decodeFromPem(parentCertPem)[0]
    let parentKeyPem = String.fromUtf8(readToEnd(File("./rsa_private_key.pem", Read)))
    let parentPrivateKey = PrivateKey.decodeFromPem(parentKeyPem)
    let usrKeyPem = String.fromUtf8(readToEnd(File("./ecdsa_public_key.pem", Read)))
    let usrPublicKey = PublicKey.decodeFromPem(usrKeyPem)

    let certInfo = X509CertificateInfo(serialNumber: serialNumber, notBefore: startTime, notAfter: endTime,
        subject: x509Name, dnsNames: ["b.com"], IPAddresses: [ip1, ip2]);
    let cert = X509Certificate(certInfo, parent: parentCert, publicKey: usrPublicKey, privateKey: parentPrivateKey)

    println(cert)
    println("Serial Number: ${cert.serialNumber}")
    println("Issuer: ${cert.issuer}")
    println("Subject: ${cert.subject}")
    println("NotBefore: ${cert.notBefore}")
    println("NotAfter: ${cert.notAfter}")
    println(cert.signatureAlgorithm)
    println("DNSNames: ${cert.dnsNames}")
    println("IPAddresses: ${cert.IPAddresses}")

    return 0
}
```

## 创建、解析证书签名请求

> **说明：**
>
> 需要自行准备私钥等文件。

示例：

<!-- compile -->
```cangjie
import std.fs.*
import std.io.*
import stdx.crypto.x509.*

main() {
    let x509Name = X509Name(
        countryName: "CN",
        provinceName: "beijing",
        localityName: "haidian",
        organizationName: "organization",
        organizationalUnitName: "organization unit",
        commonName: "x509",
        email: "test@email.com"
    )
    let ip1: IP = [8, 8, 8, 8]
    let ip2: IP = [0, 1, 0, 1, 0, 1, 0, 1, 0, 8, 0, 8, 0, 8, 0, 8]
    let rsaPem = String.fromUtf8(readToEnd(File("./rsa_private_key.pem", Read)))
    let rsa = PrivateKey.decodeFromPem(rsaPem)

    let csrInfo = X509CertificateRequestInfo(subject: x509Name, dnsNames: ["b.com"], IPAddresses: [ip1, ip2]);
    let csr = X509CertificateRequest(rsa, certificateRequestInfo: csrInfo, signatureAlgorithm: SHA256WithRSA)

    println("Subject: ${csr.subject.toString()}")
    println("IPAddresses: ${csr.IPAddresses}")
    println("dnsNames: ${csr.dnsNames}")

    return 0
}
```