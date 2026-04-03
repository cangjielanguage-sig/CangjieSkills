### func insert(String, Map\<String, RelationalStoreValueType>)

```cangjie
public func insert(table: String, values: Map<String, RelationalStoreValueType>): Int64
```

**功能：** 向目标表中插入一行数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|table|String|是|-|指定的目标表名。|
|values|Map\<String, [RelationalStoreValueType](#enum-relationalstorevaluetype)>|是|-|表示要插入到表中的数据行。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|如果操作成功，返回行ID；否则返回-1。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息                                                 |
  |:-----------| :------------------------------------------------------------ |
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
rdbStore.executeSql(
    "CREATE TABLE EMPLOYEE(ID int NOT NULL, NAME varchar(255) NOT NULL, AGE int, SALARY float NOT NULL, CODES Bit NOT NULL, PRIMARY KEY (Id))"
)
var values = HashMap<String, RelationalStoreValueType>()
values.add("ID", RelationalStoreValueType.integer(1))
values.add("NAME", RelationalStoreValueType.string("Lisa"))
values.add("AGE", RelationalStoreValueType.integer(18))
values.add("SALARY", RelationalStoreValueType.double(100.5))
values.add("CODES", RelationalStoreValueType.boolean(true))
rdbStore.insert("EMPLOYEE", values)
```