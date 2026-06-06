# 查询密钥是否存在（仓颉）

HUKS提供了接口供应用查询指定密钥是否存在。

## 开发步骤

1. 指定密钥别名keyAlias，密钥别名最大长度为128字节。

2. 初始化密钥属性集。用于查询时指定[密钥的属性TAG](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-huksoptions)，当查询单个密钥时，TAG字段可传空。

3. 调用接口[isKeyItemExist](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#func-iskeyitemexiststring-huksoptions)，查询密钥是否存在。

## 示例

```cangjie
import kit.UniversalKeystoreKit.*

/* 1. 确定密钥别名 */
let keyAlias = "test_is_key_item_exist"

/* 2. 判断密钥是否存在，a应为false */
var a = isKeyItemExist(keyAlias, HuksOptions.NONE)

let options = HuksOptions(
    [
        HuksParam(HuksTag.HUKS_TAG_ALGORITHM, HuksKeyAlg.HUKS_ALG_AES),
        HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, HuksKeySize.HUKS_AES_KEY_SIZE_128),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
        )
    ],
    Option.None
)

/* 3. 生成密钥 */
generateKeyItem(keyAlias, options)
/* 4. 判断密钥是否存在，此时a应为true */
a = isKeyItemExist(keyAlias, HuksOptions.NONE)
```
