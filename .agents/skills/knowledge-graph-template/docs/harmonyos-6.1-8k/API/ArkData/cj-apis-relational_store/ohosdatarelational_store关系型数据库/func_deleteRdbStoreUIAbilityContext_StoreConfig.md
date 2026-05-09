## func deleteRdbStore(UIAbilityContext, StoreConfig)

```cangjie
public func deleteRdbStore(context: UIAbilityContext, config: StoreConfig): Unit
```

**功能：** 使用指定的数据库文件配置删除数据库。

若数据库文件处于公共沙箱目录下，则删除数据库时必须使用该接口。当存在多个进程操作同一个数据库的情况，建议向其他进程发送数据库删除通知使其感知并处理。建立数据库时，若在[StoreConfig](#class-storeconfig)中配置了自定义路径，则必须调用此接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|应用的上下文。|
|config|[StoreConfig](#class-storeconfig)|是|-|与此RDB存储相关的数据库配置。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported. |
  | 14800000 | Inner error. |
  | 14800010 | Failed to open or delete the database by an invalid database path. |
  | 14801001 | The operation is supported in the stage model only. |
  | 14801002 | Invalid data group ID. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    var rdbStore: RdbStore = getRdbStore(Global.abilityContext, StoreConfig(RelationalStoreSecurityLevel.S1, name: "RdbTest.db")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    deleteRdbStore(Global.abilityContext, StoreConfig(RelationalStoreSecurityLevel.S1, name: "RdbTest.db"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```