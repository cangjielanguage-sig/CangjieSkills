### 验签模式为Recover

算法库框架目前提供了RSA签名恢复原始数据功能。

以字符串参数完成RSA签名恢复，具体的“字符串参数”由“非对称密钥类型”、“填充模式”、“摘要”和“验签模式”使用符号“|”拼接而成，用于在创建非对称验签实例时，指定非对称验签算法规格。

如表所示，各取值范围（即[]中的内容）中，只能选取一项完成字符串拼接。举例说明，当需要非对称密钥类型为RSA2048、填充模式为PKCS1、摘要算法为SHA256、验签模式为Recover的密钥时，其字符串参数为"RSA2048|PKCS1|SHA256|Recover"。

| 非对称密钥类型 | 填充模式 | 摘要算法 | 签名模式 | API版本 |
| :-------- | :-------- | :-------- | :-------- | :-------- |
| RSA512 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256] | Recover | 12+ |
| RSA768 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | Recover | 12+ |
| RSA1024 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | Recover | 12+ |
| RSA2048 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | Recover | 12+ |
| RSA3072 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | Recover | 12+ |
| RSA4096 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | Recover | 12+ |
| RSA8192 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | Recover | 12+ |
| [RSA512\|RSA768\|RSA1024\|RSA2048\|RSA3072\|RSA4096\|RSA8192\|RSA] | NoPadding | NoHash | Recover | 12+ |
| RSA | PKCS1 | 符合长度要求的摘要算法 | Recover | 12+ |

如表中最后一行所示，为了兼容由密钥参数生成的密钥，RSA签名恢复参数输入密钥类型时支持不带长度，签名恢复运算取决于实际输入的密钥长度。