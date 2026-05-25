### func getLong(Int32)

```cangjie
public func getLong(columnIndex: Int32): Int64
```

**功能：** 以Int64形式获取当前行中指定列的值，如果当前列的数据类型为INTEGER、DOUBLE、TEXT、BLOB类型，会转成Int64类型返回指定值，如果该列内容为空时，会返回0，其他类型则返回14800000。如果当前列的数据类型为INTEGER，值大于 2^53 - 1 或小于 -(2^53 - 1) 且不希望丢失精度，建议使用[getString](#func-getstringint32)接口获取。如果当前列的数据类型为DOUBLE且不希望丢失精度，建议使用[getDouble](#func-getdoubleint32)接口获取。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|columnIndex|Int32|是|-|指定的列索引，从0开始。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|以Int64形式返回指定列的值。<br>该接口支持的数据范围是：-(2^53 - 1)~2^53 - 1，若超出该范围，，建议对于DOUBLE类型的值使用[getDouble](#func-getdoubleint32)，对于INTEGER类型的值使用[getString](#func-getstringint32)。|

**异常：**

- BusinessException：对应错误码如下表，详见[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14800000 | Inner error. |
  | 14800011 | Failed to open the database because it is corrupted. |
  | 14800012 | ResultSet is empty or pointer index is out of bounds. |
  | 14800013 | Resultset is empty or column index is out of bounds. |
  | 14800014 | The RdbStore or ResultSet is already closed. |
  | 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
  | 14800022 | SQLite: Callback routine requested an abort. |
  | 14800023 | SQLite: Access permission denied. |
  | 14800024 | SQLite: The database file is locked. |
  | 14800025 | SQLite: A table in the database is locked. |
  | 14800026 | SQLite: The database is out of memory. |
  | 14800027 | SQLite: Attempt to write a readonly database. |
  | 14800028 | SQLite: Some kind of disk I/O error occurred. |
  | 14800029 | SQLite: The database is full. |
  | 14800030 | SQLite: Unable to open the database file. |
  | 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
  | 14800032 | SQLite: Abort due to constraint violation. |
  | 14800033 | SQLite: Data type mismatch. |
  | 14800034 | SQLite: Library used incorrectly. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    var rdbStore: RdbStore = getRdbStore(Global.abilityContext,
        StoreConfig(RelationalStoreSecurityLevel.S1, name: "RdbTest.db")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let resultSet = rdbStore.querySql("SELECT * FROM EMPLOYEE WHERE NAME = 'Peter'")
    let age = resultSet.getLong(resultSet.getColumnIndex("AGE"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```