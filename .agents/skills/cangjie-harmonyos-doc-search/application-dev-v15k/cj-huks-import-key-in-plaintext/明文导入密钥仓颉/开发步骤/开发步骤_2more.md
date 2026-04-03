## 开发步骤

1. 指定密钥别名keyAlias。

    密钥别名的最大长度为128字节。

2. 封装密钥属性集和密钥材料。

    - 密钥属性集同样与密钥生成中指定的密钥属性一致，须包含[HuksKeyAlg](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-hukskeyalg)、[HuksKeySize](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-hukskeysize)、[HuksKeyPurpose](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-hukskeypurpose)属性。
    - 密钥材料须符合[HUKS密钥材料格式](./cj-huks-concepts.md#密钥材料格式)，并以Array\<UInt8>形式赋值给[HuksOptions](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-huksoptions)的inData字段。

3. 调用[importKeyItem](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#func-importkeyitemstring-huksoptions)，传入密钥别名和密钥属性集，即可导入密钥。

    HuksParam和HuksOptions的含义参考：[HuksParam](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-huksparam) 和 [HuksOptions](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-huksoptions)

### 导入AES256密钥

```cangjie
/* 以下以导入AES256密钥的Callback操作使用为例 */
import kit.UniversalKeystoreKit.*

/* 以下以生成DH密钥为例 */
import kit.UniversalKeystoreKit.*

/* 密钥材料 */
let plainTextSize32: Array<UInt8> = [0xfb, 0x8b, 0x9f, 0x12, 0xa0, 0x83, 0x19, 0xbe, 0x6a, 0x6f, 0x63, 0x2a, 0x7c, 0x86,
    0xba, 0xca, 0x64, 0x0b, 0x88, 0x96, 0xe2, 0xfa, 0x77, 0xbc, 0x71, 0xe3, 0x0f, 0x0f, 0x9e, 0x3c, 0xe5, 0xf9]

/* 1.确定密钥别名 */
let keyAlias = 'AES256Alias_sample'

/* 2.封装密钥属性集和密钥材料 */
let properties: Array<HuksParam> = [
    HuksParam(
        HuksTag.HUKS_TAG_ALGORITHM,
        HuksKeyAlg.HUKS_ALG_AES
    ),
    HuksParam(
        HuksTag.HUKS_TAG_KEY_SIZE,
        HuksKeySize.HUKS_AES_KEY_SIZE_256
    ),
    HuksParam(
        HuksTag.HUKS_TAG_PURPOSE,
        HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
    )
]
let options: HuksOptions = HuksOptions(
    properties,
    plainTextSize32
)

/* 3.明文导入密钥 */
func importKeyFunc(): Unit {
    try {
        importKeyItem(keyAlias, options)
    } catch (e: Exception) {
        AppLog.error("callback: importKeyItem input arg invalid ${e}")
    }
}
```