# 获取密钥属性（仓颉）

HUKS提供了接口供业务获取指定密钥的相关属性。在获取指定密钥属性前，需要确保已在HUKS中生成或导入持久化存储的密钥。

> **说明：**
>
> 轻量级设备不支持获取密钥属性功能。

## 开发步骤

1. 指定待查询的密钥别名keyAlias，密钥别名最大长度为128字节。

2. 调用接口[getKeyItemProperties](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#func-getkeyitempropertiesstring-huksoptions)，传入参数keyAlias和options。options为预留参数，当前可传入空。

3. 返回值为[HuksReturnResult](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-huksreturnresult)类型对象，获取的属性集在properties字段中。

## 示例

```cangjie
import kit.UniversalKeystoreKit.*

/* 1. 设置密钥别名 */
let keyAlias = "keyAlias"
/* option对象传空 */
let emptyOptions: HuksOptions = HuksOptions([], None)
try {
    /* 2. 获取密钥属性 */
    getKeyItemProperties(keyAlias, emptyOptions)
    AppLog.info("getKeyItemProperties success")
} catch (e: Exception) {
    AppLog.error("getKeyItemProperties input arg invalid, ${e.toString()}")
}
```
