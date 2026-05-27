# 指定PEM格式字符串数据转换非对称密钥对（仓颉）

以RSA为例，根据指定的非对称密钥字符串数据，生成非对称密钥对（KeyPair）。

> **说明：**
>
> 针对非对称密钥的convertPemKey操作：
>
> - 公钥需满足：X.509规范、PKCS\#1规范、PEM编码格式。
>
> - 私钥需满足：PKCS\#8规范、PKCS\#1规范、PEM编码格式。
>
> - 当前只支持RSA非对称密钥的转换。

## 指定PEM格式字符串数据转换RSA密钥对

对应的算法规格请参见[非对称密钥生成和转换规格：RSA](./cj-crypto-asym-key-generation-conversion-spec.md#rsa)。

1. 调用[createAsyKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorstring)，指定字符串参数'RSA1024'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（AsyKeyGenerator）。

   生成RSA非对称密钥时，默认素数为2，此处省略了参数PRIMES_2。

2. 调用[convertPemKey](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-convertpemkeystring-string)，传入二进制密钥数据，生成非对称密钥对象（KeyPair）。
3. 调用[getEncodedPem](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-getencodedpemstring-1)，将非对称密钥对象中的公钥转换成pkcs1或x509格式，私钥转换成pkcs1或pkcs8格式。

以生成RSA密钥对为例：

```cangjie
import kit.CryptoArchitectureKit.*
import ohos.base.BusinessException

let priKeyPkcs1Str1024: String = """
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCwIN3mr218+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W
Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g
YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB
AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP
LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr
7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4
D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg
e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp
a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som
MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7
DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY
qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia
akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO
-----END RSA PRIVATE KEY-----
"""
let publicPkcs1Str1024: String = """
-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE
h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg
SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=
-----END RSA PUBLIC KEY-----
"""

func TestPkcs1ToPkcs8BySync() {
    let asyKeyGenerator = createAsyKeyGenerator('RSA1024')
    try {
        let keyPairData = asyKeyGenerator.convertPemKey(publicPkcs1Str1024, priKeyPkcs1Str1024)
        let priPemKey = keyPairData.priKey
        let pubPemKey = keyPairData.pubKey
        let priString = priPemKey.getEncodedPem('PKCS8')
        let pubString = pubPemKey.getEncodedPem('X509')
        AppLog.info("[Sync]TestPkcs1ToPkcs8BySync priString output is " + priString)
        AppLog.info("[Sync]TestPkcs1ToPkcs8BySync pubString output is " + pubString)
    } catch (e: BusinessException) {
        AppLog.error("Sync error, ${e.code}, ${e.message}")
    }
}
```
