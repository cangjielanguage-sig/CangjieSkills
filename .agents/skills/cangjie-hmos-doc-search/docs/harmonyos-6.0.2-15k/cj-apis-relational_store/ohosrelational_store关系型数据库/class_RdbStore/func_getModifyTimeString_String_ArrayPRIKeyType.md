### func getModifyTime(String, String, Array\<PRIKeyType>)

```cangjie
public func getModifyTime(table: String, columnName: String, primaryKeys: Array<PRIKeyType>): HashMap<PRIKeyType, DateTime>
```

**功能：** 获取数据库表中数据的最后修改时间。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|table|String|是|-|指定要查询的数据库表的表名。|
|columnName|String|是|-|指定要查询的数据库表的列名。|
|primaryKeys|Array\<[PRIKeyType](#enum-prikeytype)>|是|-|指定要查询的行的主键。<br>如果数据库表无主键，参数columnName需传入"rowid"，此时primaryKeys为要查询的数据库表的行号。<br>如果数据库表无主键，参数columnName传入不为"rowid"，返回对应的错误码。|

**返回值：**

|类型|说明|
|:----|:----|
| HashMap&lt;[PRIKeyType](#enum-prikeytype), DateTime&gt;|表示数据最后的修改时间。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Need 3 - 4  parameter(s)! 2. The RdbStore must be not nullptr.3. The tablesNames must be not empty string. 4. The columnName must be not empty string. 5. The PRIKey must be number or string.|
  |801|Capability not supported.|
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

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(), StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let PRIKey = [PRIKeyType.Integer(1)]
rdbStore.getModifyTime("EMPLOYEE", "ID", PRIKey)
```