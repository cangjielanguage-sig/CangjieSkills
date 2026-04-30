# 对称密钥加解密算法规格

当前章节将说明系统目前支持的算法及其对应的规格。

对于每种算法采用支持的加密模式，将会在具体的每个算法规格中介绍。

## AES

算法库当前提供了[AES](./cj-crypto-sym-key-generation-conversion-spec.md#aes)加解密常用的7种加密模式：ECB、CBC、OFB、CFB、CTR、GCM和CCM。不同的加密模式适用的加解密参数不同，具体请参见[ParamsSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#interface-paramsspec)。

由于AES为分组加密算法，分组长度为128位。在实际应用中，最后一组明文可能不足128位（16字节），此时可以通过不同的[填充模式](#填充模式)进行数据填充。

由于需要填充至分组大小，所以实际算法库中的PKCS5和PKCS7都是以分组大小作为填充长度的，即AES加密填充至16字节。

> **说明：**
>
> - ECB、CBC加密模式，明文长度不是128位整数倍，必须使用填充方法补足。
> - CCM加密模式，必须指定附加验证数据aad且其长度必须大于等于1字节且小于等于2048字节。

当前支持以字符串参数完成AES加解密，具体的“字符串参数”由“对称密钥类型（加解密算法+密钥长度）”、“分组模式”和“填充模式”使用符号“|”拼接而成，用于在创建对称加解密实例时，指定算法规格。

- 如表所示，各取值范围（即[]中的内容）中，只能选取一项完成字符串拼接。

  举例说明如下：

    - 当需要分组模式为ECB、密钥长度为128bit、填充模式为PKCS7的AES密钥，其字符串参数为"AES128|ECB|PKCS7"。
    - 当需要分组模式为CFB、密钥长度为256bit、填充模式为NoPadding的AES密钥，其字符串参数为"AES256|CFB|NoPadding"。

  | 分组模式 | 密钥长度（bit） | 填充模式 | API版本 |
  | :-------- | :-------- | :-------- | :-------- |
  | ECB | [128\|192\|256] | [NoPadding\|PKCS5\|PKCS7] | 12+ |
  | CBC | [128\|192\|256] | [NoPadding\|PKCS5\|PKCS7] | 12+ |
  | CTR | [128\|192\|256] | [NoPadding\|PKCS5\|PKCS7] | 12+ |
  | OFB | [128\|192\|256] | [NoPadding\|PKCS5\|PKCS7] | 12+ |
  | CFB | [128\|192\|256] | [NoPadding\|PKCS5\|PKCS7] | 12+ |
  | GCM | [128\|192\|256] | [NoPadding\|PKCS5\|PKCS7] | 12+ |
  | CCM | [128\|192\|256] | [NoPadding\|PKCS5\|PKCS7] | 12+ |

- 从API版本12开始，支持对称加解密不带密钥长度的规格。加解密参数输入密钥类型时，支持不带长度，加解密运算取决于实际输入的密钥长度。

  举例说明，当需要分组模式为CFB、不带密钥长度、填充模式为NoPadding的AES密钥，其字符串参数为"AES|CFB|NoPadding"。