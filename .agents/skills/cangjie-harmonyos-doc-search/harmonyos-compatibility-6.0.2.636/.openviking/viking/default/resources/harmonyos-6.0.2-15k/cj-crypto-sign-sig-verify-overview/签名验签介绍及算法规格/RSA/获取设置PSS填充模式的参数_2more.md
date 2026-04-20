### 获取/设置PSS填充模式的参数

当前支持RSA使用PSS填充模式时，获取、设置相关参数，“√”表示支持对获取或设置该参数。

| PSS参数 | 枚举值 | 获取 | 设置 |
| :-------- | :-------- | :-------- | :-------- |
| md | PSS_MD_NAME_STR | √ | - |
| mgf | PSS_MGF_NAME_STR | √ | - |
| mgf1_md | PSS_MGF1_MD_STR | √ | - |
| saltLen | PSS_SALT_LEN_NUM | √ | √ |
| trailer_field | PSS_TRAILER_FIELD_NUM | √ | - |

### 签名模式为OnlySign

算法库框架目前提供了RSA签名不做摘要仅签名功能。

以字符串参数完成RSA签名，具体的“字符串参数”由“非对称密钥类型”、“填充模式”、“摘要”和“签名模式”使用符号“|”拼接而成，用于在创建非对称签名实例时，指定非对称签名算法规格。

如表所示，各取值范围（即[]中的内容）中，只能选取一项完成字符串拼接。举例说明，当需要非对称密钥类型为RSA2048、填充模式为PKCS1、摘要算法为SHA256、签名模式为OnlySign的密钥时，其字符串参数为"RSA2048|PKCS1|SHA256|OnlySign"。

> **说明：**
>
> - RSA仅签名时，对待签名数据有长度要求：
> - PKCS1填充模式，NoHash不设置摘要算法，数据需要小于RSA密钥字节长度-11（PKCS1填充长度）。
> - PKCS1填充模式，设置任意摘要算法，待签名的数据必须是对应的摘要数据。
> - NoPadding不设置填充模式，NoHash不设置摘要算法，待签名的数据长度需要等于RSA密钥字节长度，且其数值小于RSA模数。

| 非对称密钥类型 | 填充模式 | 摘要算法 | 签名模式 | API版本 |
| :-------- | :-------- | :-------- | :-------- | :-------- |
| RSA512 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256] | OnlySign | 12+ |
| RSA768 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | OnlySign | 12+ |
| RSA1024 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | OnlySign | 12+ |
| RSA2048 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | OnlySign | 12+ |
| RSA3072 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | OnlySign | 12+ |
| RSA4096 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | OnlySign | 12+ |
| RSA8192 | PKCS1 | [NoHash\|MD5\|SHA1\|SHA224\|SHA256\|SHA384\|SHA512] | OnlySign | 12+ |
| [RSA512\|RSA768\|RSA1024\|RSA2048\|RSA3072\|RSA4096\|RSA8192\|RSA] | NoPadding | NoHash | OnlySign | 12+ |
| RSA | PKCS1 | 符合长度要求的摘要算法 | OnlySign | 12+ |

如表中最后一行所示，为了兼容由密钥参数生成的密钥，RSA签名参数输入密钥类型时支持不带长度，签名运算取决于实际输入的密钥长度。