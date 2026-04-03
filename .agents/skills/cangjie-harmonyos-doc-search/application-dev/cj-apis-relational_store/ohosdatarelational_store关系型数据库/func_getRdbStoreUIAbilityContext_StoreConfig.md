## func getRdbStore(UIAbilityContext, StoreConfig)

```cangjie
public func getRdbStore(context: UIAbilityContext, config: StoreConfig): RdbStore
```

**功能：** 创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。

对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](#class-storeconfig)。对应路径下已有数据库文件时，将打开已有数据库文件。

开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](#var-encrypt)，数据库创建后，禁止对该参数进行修改。

| 当前开库的加密类型  | 本设备上创建该数据库时的加密类型           | 结果 |
| ------- | -------------------------------- | ---- |
| 非加密 | 加密                          | 将数据库以加密方式打开。   |
| 加密 | 非加密                          | 将数据库以非加密方式打开。   |

getRdbStore目前不支持多线程并发操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|应用的上下文。|
|config|[StoreConfig](#class-storeconfig)|是|-|与此RDB存储相关的数据库配置。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbStore](#class-rdbstore)|返回RdbStore对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14800000 | Inner error. |
  | 14800010 | Failed to open or delete the database by an invalid database path. |
  | 14800011 | Failed to open the database because it is corrupted. |
  | 14801001 | The operation is supported in the stage model only. |
  | 14801002 | Invalid data group ID. |
  | 14800017 | StoreConfig is changed. |
  | 14800020 | The secret key is corrupted or lost. |
  | 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
  | 14800022 | SQLite: Callback routine requested an abort. |
  | 14800023 | SQLite: Access permission denied. |
  | 14800027 | SQLite: Attempt to write a readonly database. |
  | 14800028 | SQLite: Some kind of disk I/O error occurred. |
  | 14800029 | SQLite: The database is full. |
  | 14800030 | SQLite: Unable to open the database file. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    var rdbStore: RdbStore = getRdbStore(Global.abilityContext, StoreConfig(RelationalStoreSecurityLevel.S1, name: "RdbTest.db")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```