# ohos.relational_store（关系型数据库）

关系型数据库（Relational Database，RDB）是一种基于关系模型来管理数据的数据库。关系型数据库基于SQLite组件提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户输入的SQL语句来满足复杂的场景需要。不支持Worker线程。

仓颉侧支持的基本数据类型：Int64、Float64、String、二进制类型数据、Bool。为保证插入并读取数据成功，建议一条数据不要超过2M。超出该大小，插入成功，读取失败。

该模块提供以下关系型数据库相关的常用功能：

- [RdbPredicates](#class-rdbpredicates)： 数据库中用来代表数据实体的性质、特征或者数据实体之间关系的词项，主要用来定义数据库的操作条件。
- [RdbStore](#class-rdbstore)：提供管理关系数据库(RDB)方法的接口。
- [ResultSet](#class-resultset)：提供用户调用关系型数据库查询接口之后返回的结果集合。

## 导入模块

```cangjie
import kit.ArkData.*
```

## 权限列表

ohos.permission.DISTRIBUTED_DATASYNC

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func deleteRdbStore(StageContext, String)

```cangjie
public func deleteRdbStore(context: StageContext, name: String): Unit
```

**功能：** 使用指定的数据库文件配置删除数据库。删除成功后，建议将数据库对象置为None。建立数据库时，若在[StoreConfig](#class-storeconfig)中配置了自定义路径，则调用此接口进行删库无效，必须使用[deleteRdbStore(StageContext, StoreConfig)](#func-deleterdbstorestagecontext-storeconfig)接口进行删库。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-| 应用的上下文。context的获取方式请参见[getStageContext](../AbilityKit/cj-apis-ability.md#func-getstagecontextabilitycontext)。|
|name|String|是|-|数据库名称。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息|
  |:-----------| :------------|
  | 401       | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
  | 14800000  | Inner error. |
  | 14800010  | Invalid database path. |
  | 14800011  | Database corrupted.  |
  | 14800017  | Config changed. |
  | 14800021  | SQLite: Generic error. |
  | 14800027  | SQLite: Attempt to write a readonly database. |
  | 14800028  | SQLite: Some kind of disk I/O error occurred. |
  | 14800029  | SQLite: The database is full. |
  | 14800030  | SQLite: Unable to open the database file. |
  | 14801001  | Only supported in stage mode.|
  | 14801002  | The data group id is not valid.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(), StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
deleteRdbStore(Global.getStageContext(), "RdbTest.db")
```