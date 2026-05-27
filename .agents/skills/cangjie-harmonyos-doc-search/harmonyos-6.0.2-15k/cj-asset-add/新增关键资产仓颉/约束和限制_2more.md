## 约束和限制

- 基于别名的访问

  关键资产以密文的形式存储在ASSET数据库中，以业务身份+别名作为唯一索引。故业务需要保证每条关键资产的别名唯一。

- 业务自定义数据存储

  ASSET为业务预留了12个关键资产自定义属性，名称以"DATA_LABEL"开头。对于超过12个自定义属性的情况，业务可以将多段数据按照一定的格式（如JSON）拼接到同一个ASSET属性中。

  ASSET对部分属性会进行完整性保护，这部分属性名称以"DATA_LABEL_CRITICAL"开头，写入后不支持更新。

## 代码示例

本模块提供了同步接口，以下为同步接口的使用示例。

新增一条密码是demo_pwd，别名是demo_alias，附属信息是demo_label的数据，该数据在用户首次解锁设备后可被访问。

```cangjie
import kit.AssetStoreKit.*
import ohos.base.BusinessException

try{
  let secret: AssetParam = AssetParam.SECRET("demo_pwd".toArray())
  let data_label_n1: AssetParam = AssetParam.DATA_LABEL_NORMAL_1("demo_label".toArray())
  let alias: AssetParam = AssetParam.ALIAS("demo_alias".toArray())
  let access: AssetParam = AssetParam.ACCESSIBILITY(AssetAccessibility.DEVICE_FIRST_UNLOCKED)
  let add_attr: Array<AssetParam> = [secret, data_label_n1, alias, access]
  add(add_attr)
} catch(e: BusinessException) {
  AppLog.error("Failed to add Asset. Code is : ${e.code}, message is ${e.message}")
}
```