### func executeSql(String, Array\<RelationalStoreValueType>)

```cangjie
public func executeSql(sql: String, bindArgs!: Array<RelationalStoreValueType> = []): Unit
```

**功能：**  执行指定的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](#func-querysqlstring-arrayrelationalstorevaluetype)、[query](#func-queryrdbpredicates-arraystring)、[beginTransaction](#func-begintransaction)、[commit](#func-commit)等接口代替。

不支持分号分隔的多条语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sql|String|是|-|指定要执行的SQL语句。|
|bindArgs|Array\<[RelationalStoreValueType](#enum-relationalstorevaluetype)>|否|[]|**命名参数。** SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。|

**异常：**

- BusinessException：对应错误码如下表，详见[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
  | 14800000 | Inner error. |
  | 14800011 | Failed to open the database because it is corrupted. |
  | 14800014 | The RdbStore or ResultSet is already closed. |
  | 14800015 | The database does not respond. |
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
  | 14800047 | The WAL file size exceeds the default limit. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    var rdbStore: RdbStore = getRdbStore(Global.abilityContext, StoreConfig(RelationalStoreSecurityLevel.S1, name: "RdbTest.db")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    rdbStore.executeSql("DELETE FROM EMPLOYEE WHERE ID = ?", bindArgs: [RelationalStoreValueType.Integer(3)])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```