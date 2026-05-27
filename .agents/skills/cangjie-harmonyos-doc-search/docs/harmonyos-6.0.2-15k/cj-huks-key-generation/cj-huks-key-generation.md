# 生成密钥（仓颉）

以生成DH密钥为例，生成随机密钥。具体的场景介绍及支持的算法规格，请参见[密钥生成支持的算法](./cj-huks-key-generation-overview.md#支持的算法)。

> **注意：**
>
> 密钥别名中禁止包含个人数据等敏感信息。

## 开发步骤

1. 指定待生成的密钥别名keyAlias。

    - 密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。
    - 对于不同业务间生成的密钥，HUKS将基于业务身份信息进行存储路径隔离，不会因为和其他业务密钥同名导致冲突。

2. 初始化密钥属性集。通过[HuksParam](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-huksparam)封装密钥属性，搭配Array组成密钥属性集，并赋值给[HuksOptions](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-huksoptions)中的properties字段。

    密钥属性集中必须包含[HuksKeyAlg](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-hukskeyalg)、[HuksKeySize](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-hukskeysize)、[HuksKeyPurpose](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-hukskeypurpose)属性，即必传TAG，HUKS_TAG_ALGORITHM、HUKS_TAG_PURPOSE、HUKS_TAG_KEY_SIZE。注：一个密钥只能有一类PURPOSE，并且，生成密钥时指定的用途要与使用时的方式一致，否则会导致异常，请参见[密钥用途](./cj-huks-key-generation-overview.md#密钥用途)。

3. 调用[generateKeyItem](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#func-generatekeyitemstring-huksoptions)，传入密钥别名和密钥属性集，生成密钥。

> **说明：**
>
> 如果业务再次使用相同别名调用HUKS生成密钥，HUKS将生成新密钥并直接覆盖历史的密钥文件。

## 示例

```cangjie
/* 以生成DH密钥为例 */
import kit.UniversalKeystoreKit.*

/* 1.确定密钥别名 */
let keyAlias = 'dh_key'
/* 2.初始化密钥属性集 */
let properties1: Array<HuksParam> = [
    HuksParam(
        HuksTag.HUKS_TAG_ALGORITHM,
        HuksKeyAlg.HUKS_ALG_DH
    ),
    HuksParam(
        HuksTag.HUKS_TAG_PURPOSE,
        HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE
    ),
    HuksParam(
        HuksTag.HUKS_TAG_KEY_SIZE,
        HuksKeySize.HUKS_DH_KEY_SIZE_2048
    )
]
let huksOptions: HuksOptions = HuksOptions(
    properties1,
    None
)

/* 3.生成密钥 */
func publicGenKeyFunc(keyAlias: String, huksOptions: HuksOptions) {
    AppLog.info("enter generateKeyItem")
    try {
        generateKeyItem(keyAlias, huksOptions)
    } catch (e: Exception) {
        AppLog.error("generateKeyItem input arg invalid, ${e}")
    }
}

func TestGenKey() {
    publicGenKeyFunc(keyAlias, huksOptions)
}
```
