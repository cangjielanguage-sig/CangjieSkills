## ECDSA

ECDSA（Elliptic Curve Digital Signature Algorithm，椭圆曲线数字签名算法）是基于椭圆曲线密码（ECC）的数字签名算法（DSA）。相比DLP（Discrete logarithm Problem，普通的离散对数问题）和IFP（integer factorization problem，大数分解问题），椭圆曲线密码的单位比特强度要高于其他公钥体制。

算法库框架提供了多种椭圆曲线及摘要算法组合的ECDSA签名验签能力。

以字符串参数完成ECDSA签名验签，具体的“字符串参数”由“非对称密钥类型”和“摘要”使用符号“|”拼接而成，用于在创建非对称签名验签实例时，指定非对称签名验签算法规格。

如表所示，各取值范围（即[]中的内容）中，只能选取一项完成字符串拼接。举例说明，当需要非对称密钥类型为ECC224、摘要算法为SHA256的密钥时，其字符串参数为"ECC224|SHA256"。

| 非对称密钥类型 | 摘要 | API版本 |
| :-------- | :-------- | :-------- |
| ECC224 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC256 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC384 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC521 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP160r1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP160t1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP192r1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP192t1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP224r1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP224t1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP256r1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP256t1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP320r1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP320t1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP384r1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP384t1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP512r1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_BrainPoolP512t1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC_Secp256k1 | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |
| ECC | [SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | 12+ |

如表中最后一行所示，为了兼容由密钥参数生成的密钥，ECDSA签名验签参数输入密钥类型时支持不指定长度和曲线，签名验签运算取决于实际输入的密钥。