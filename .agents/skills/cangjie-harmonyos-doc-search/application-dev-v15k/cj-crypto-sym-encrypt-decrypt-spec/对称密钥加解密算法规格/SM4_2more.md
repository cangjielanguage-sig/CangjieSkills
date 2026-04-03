## SM4

算法库当前提供了[SM4](./cj-crypto-sym-key-generation-conversion-spec.md#sm4)加解密常用的7种加密模式：ECB、CBC、CTR、OFB、CFB、CFB128和GCM。不同的加密模式适用的加解密参数不同，具体请参见[ParamsSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#interface-paramsspec)。

由于SM4为分组加密算法，分组长度为128位。在实际应用中，最后一组明文可能不足128位（16字节），此时可以通过不同的[填充模式](#填充模式)进行数据填充。

由于需要填充至分组大小，所以实际算法库中的PKCS5和PKCS7都是以分组大小作为填充长度的，即SM4加密填充至16字节。

> **说明：**
>
> ECB、CBC加密模式，明文长度不是128位整数倍，必须使用填充方法补足。

当前支持以字符串参数完成SM4加解密，具体的“字符串参数”由“对称密钥类型（加解密算法+密钥长度）”、“分组模式”和“填充模式”使用符号“|”拼接而成，用于在创建对称加解密实例时，指定算法规格。

如表所示，各取值范围（即[]中的内容）中，只能选取一项完成字符串拼接。SM4算法和密钥长度中间采用符号“_”拼接。

举例说明如下：

- 当需要分组模式为ECB、密钥长度为128bit、填充模式为PKCS7的SM4密钥，其字符串参数为"SM4_128|ECB|PKCS7"。
- 当需要分组模式为CFB、密钥长度为128bit、填充模式为NoPadding的SM4密钥，其字符串参数为"SM4_128|CFB|NoPadding"。
- 当需要分组模式为GCM、密钥长度为128bit、填充模式为NoPadding的SM4密钥，其字符串参数为"SM4_128|GCM|NoPadding"。

| 分组模式 | 密钥长度（bit） | 填充模式 | API版本 |
| :-------- | :-------- | :-------- | :-------- |
| ECB | 128 | [NoPadding\|PKCS5\|PKCS7] | 12+ |
| CBC | 128 | [NoPadding\|PKCS5\|PKCS7] | 12+ |
| CTR | 128 | [NoPadding\|PKCS5\|PKCS7] | 12+ |
| OFB | 128 | [NoPadding\|PKCS5\|PKCS7] | 12+ |
| CFB | 128 | [NoPadding\|PKCS5\|PKCS7] | 12+ |
| CFB128 | 128 | [NoPadding\|PKCS5\|PKCS7] | 12+ |
| GCM | 128 | [NoPadding\|PKCS5\|PKCS7] | 12+ |

## 填充模式

分组加密算法有固定的分组长度，在实际应用中，最后一组明文的数据量可能无法达到固定的长度要求，此时可以通过不同的填充模式进行数据填充。填充模式有：

- NoPadding：不带填充。输入数据需要与分组长度匹配。
- PKCS5：填充字符由一个字节序列组成，而且每个字节填充的值与要填充的字节序列长度相同。且PKCS5为8字节填充，即需将数据填充为8字节的倍数。
- PKCS7：填充方法和PKCS5一致。但PKCS7的可以在1-255字节之间任意填充，PKCS5固定为8字节。

对于CFB、OFB、CTR、GCM、CCM这类将分组密码转化为流模式实现的模式，不需要填充，因此无论是否指定填充模式，都会按照NoPadding实现