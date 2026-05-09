### func getColumnIndex(String)

```cangjie
public func getColumnIndex(columnName: String): Int32
```

**功能：** 根据指定的列名获取列索引。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|columnName|String|是|-|表示结果集中指定列的名称。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回指定列的索引。|

**异常：**

- BusinessException：对应错误码如下表，详见[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14800000 | Inner error. |
  | 14800011 | Failed to open the database because it is corrupted. |
  | 14800013 | Resultset is empty or column index is out of bounds. |
  | 14800014 | The RdbStore or ResultSet is already closed. |
  | 14800019 | The SQL must be a query statement. |
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
    let id = resultSet.getLong(resultSet.getColumnIndex("ID"))
    let name = resultSet.getString(resultSet.getColumnIndex("NAME"))
    let age = resultSet.getLong(resultSet.getColumnIndex("AGE"))
    let salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```