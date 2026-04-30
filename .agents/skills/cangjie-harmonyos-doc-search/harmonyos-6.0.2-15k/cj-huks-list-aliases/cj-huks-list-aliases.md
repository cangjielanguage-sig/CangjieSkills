# 查询密钥别名集（仓颉）

HUKS提供了接口供应用查询密钥别名集。

> **说明：**
>
> 轻量级设备不支持查询密钥别名集功能。

## 开发步骤

1. 初始化密钥属性集。用于查询指定密钥别名集TAG，TAG仅支持[HUKS_TAG_AUTH_STORAGE_LEVEL](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#huks_tag_auth_storage_level)。

2. 调用接口[listAliases](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#func-listaliaseshuksoptions)，查询密钥别名集。

## 示例

```cangjie
/*
 * 以下查询密钥别名集操作使用为例
 */
import kit.UniversalKeystoreKit.*

func testListAliases() {
    /* 1. 初始化密钥属性集 */
    let queryProperties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
            HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_DE
        )
    ]
    let queryOptions: HuksOptions = HuksOptions(queryProperties, None)

    try {
        /* 2. 查询密钥别名集 */
        let result = listAliases(queryOptions)
        AppLog.info("promise: listAliases success ${result.size}")
    } catch (e: Exception) {
        AppLog.error("promise: listAliases fail")
    }
}
```
