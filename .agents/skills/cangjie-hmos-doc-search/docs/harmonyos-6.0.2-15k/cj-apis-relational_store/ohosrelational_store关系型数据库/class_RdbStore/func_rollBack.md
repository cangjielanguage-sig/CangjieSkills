### func rollBack()

```cangjie
public func rollBack(): Unit
```

**功能：** 回滚已经执行的SQL语句。此接口不支持在多进程或多线程中使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. The store must not be nullptr.|
  |14800000|Inner error.|
  |14800011|Database corrupted.|
  |14800014|Already closed.|
  |14800015|The database does not respond.|
  |14800021|SQLite: Generic error.|
  |14800022|SQLite: Callback routine requested an abort.|
  |14800023|SQLite: Access permission denied.|
  |14800024|SQLite: The database file is locked.|
  |14800025|SQLite: A table in the database is locked.|
  |14800026|SQLite: The database is out of memory.|
  |14800027|SQLite: Attempt to write a readonly database.|
  |14800028|SQLite: Some kind of disk I/O error occurred.|
  |14800029|SQLite: The database is full.|
  |14800030|SQLite: Unable to open the database file.|
  |14800031|SQLite: TEXT or BLOB exceeds size limit.|
  |14800032|SQLite: Abort due to constraint violation.|
  |14800033|SQLite: Data type mismatch.|
  |14800034|SQLite: Library used incorrectly.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import std.collection.HashMap

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let predicates = RdbPredicates("THING")
var values = HashMap<String, RelationalStoreValueType>()
try {
    rdbStore.beginTransaction()
    values.add("ID", RelationalStoreValueType.integer(3))
    values.add("NAME", RelationalStoreValueType.string("Tom"))
    rdbStore.insert("THING", values)
    values.add("ID", RelationalStoreValueType.integer(4))
    values.add("NAME", RelationalStoreValueType.string("Wind"))
    rdbStore.insert("THING", values)
    rdbStore.commit()
} catch (e: Exception) {
    rdbStore.rollBack()
}
```