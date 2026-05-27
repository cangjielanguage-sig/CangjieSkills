## func getRdbStore(StageContext, StoreConfig)

```cangjie
public func getRdbStore(context: StageContext, config: StoreConfig): RdbStore
```

**功能：** 获得一个相关的RdbStore，操作关系型数据库，用户可以根据自己的需求配置RdbStore的参数，然后调用RdbStore接口执行相关的数据操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|应用的上下文。context的获取方式请参见[getStageContext](../AbilityKit/cj-apis-ability.md#func-getstagecontextabilitycontext)。|
|config|[StoreConfig](#class-storeconfig)|是|-|与此RDB存储相关的数据库配置。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbStore](#class-rdbstore)|返回RdbStore对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |14800000|Inner error.|
  |14800010|Invalid database path.|
  |14800011|Database corrupted.|
  |14801001|Only supported in stage mode.|
  |14801002|The data group id is not valid.|
  |14800017|Config changed.|
  |14800021|SQLite: Generic error.|
  |14800022|SQLite: Callback routine requested an abort.|
  |14800023|SQLite: Access permission denied.|
  |14800027|SQLite: Attempt to write a readonly database.|
  |14800028|SQLite: Some kind of disk I/O error occurred.|
  |14800029|SQLite: The database is full.|
  |14800030|SQLite: Unable to open the database file.|