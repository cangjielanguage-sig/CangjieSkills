### func cleanDirtyData(String, UInt64)

```cangjie
public func cleanDirtyData(table: String, cursor: UInt64): Unit
```

**功能：** 清理云端删除的数据同步到本地后，未自动清理的，且数据的游标（cursor）小于指定游标的数据。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|table|String|是|-|表示当前数据库的表的名称。|
|cursor|UInt64|是|-|整数类型，表示数据游标，小于此游标的脏数据将被清理。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息     |
  |:-----------|:---------------|
  | 401       | Parameter error. Possible causes: 1. Need 1 - 3  parameter(s)! 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. 4. The cursor must be valid cursor. |
  | 801       | Capability not supported. |
  | 14800000  | Inner error. |
  | 14800011  | Database corrupted. |
  | 14800014  | Already closed. |
  | 14800015  | The database does not respond. |
  | 14800021  | SQLite: Generic error. |
  | 14800022  | SQLite: Callback routine requested an abort. |
  | 14800023  | SQLite: Access permission denied. |
  | 14800024  | SQLite: The database file is locked. |
  | 14800025  | SQLite: A table in the database is locked. |
  | 14800026  | SQLite: The database is out of memory. |
  | 14800027  | SQLite: Attempt to write a readonly database. |
  | 14800028  | SQLite: Some kind of disk I/O error occurred. |
  | 14800029  | SQLite: The database is full. |
  | 14800030  | SQLite: Unable to open the database file. |
  | 14800031  | SQLite: TEXT or BLOB exceeds size limit. |
  | 14800032  | SQLite: Abort due to constraint violation. |
  | 14800033  | SQLite: Data type mismatch. |
  | 14800034  | SQLite: Library used incorrectly. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(), StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
rdbStore.cleanDirtyData("EMPLOYEE", 100)
```