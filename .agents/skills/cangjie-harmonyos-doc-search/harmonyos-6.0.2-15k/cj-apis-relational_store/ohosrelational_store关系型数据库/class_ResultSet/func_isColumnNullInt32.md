### func isColumnNull(Int32)

```cangjie
public func isColumnNull(columnIndex: Int32): Bool
```

**功能：** 检查当前行中指定列的值是否为null。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|columnIndex|Int32|是|-|指定的列索引，从0开始。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果当前行中指定列的值为null，则返回true，否则返回false。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |14800000|Inner error.|
  |14800011|Database corrupted.|
  |14800012|Row out of bounds.|
  |14800013|Column out of bounds.|
  |14800014|Already closed.|
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

var rdbStore: RdbStore = getRdbStore(
    Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)
) // 需获取Context应用上下文，详见本文使用说明
let resultSet = rdbStore.querySql("SELECT * FROM EMPLOYEE WHERE NAME = 'Peter'")
let isColumnNull = resultSet.isColumnNull(resultSet.getColumnIndex("CODES"))
```