### func update(Map\<String, RelationalStoreValueType>, RdbPredicates)

```cangjie
public func update(values: Map<String, RelationalStoreValueType>, predicates: RdbPredicates): Int64
```

**功能：** 根据RdbPredicates的指定实例对象更新数据库中的数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|values|Map\<String, [RelationalStoreValueType](#enum-relationalstorevaluetype)>|是|-|values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。|
|predicates|[RdbPredicates](#class-rdbpredicates)|是|-|RdbPredicates的实例对象指定的更新条件。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回受影响的行数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息                                                 |
  |:-----------| :------------------------------------------------------------ |
  | 202       | Permission verification failed, application which is not a system application uses system API. |
  | 401       | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
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
  | 14800047  | The WAL file size exceeds the default limit. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import std.collection.HashMap

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let predicates = RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", RelationalStoreValueType.string("TOM"))
var values = HashMap<String, RelationalStoreValueType>()
values.add("NAME", RelationalStoreValueType.string("TOM"))
values.add("AGE", RelationalStoreValueType.integer(88))
values.add("SALARY", RelationalStoreValueType.double(9999.513))
rdbStore.update(values, predicates)
```