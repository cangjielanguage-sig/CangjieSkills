### func update(ValuesBucket, RdbPredicates, ConflictResolution)

```cangjie
public func update(values: ValuesBucket, predicates: RdbPredicates,
    conflict!: ConflictResolution = ConflictResolution.OnConflictNone): Int64
```

**功能：** 根据RdbPredicates的指定实例对象更新数据库中的数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#func-queryrdbpredicates-arraystring)或[querySql](#func-querysqlstring-arrayrelationalstorevaluetype)接口获取ResultSet后，调用[getString](#func-getstringint32)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|values|[ValuesBucket](#type-valuesbucket)|是|-|values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。|
|predicates|[RdbPredicates](#class-rdbpredicates)|是|-|RdbPredicates的实例对象指定的更新条件。|
|conflict|[ConflictResolution](#enum-conflictresolution)|否|ConflictResolution.OnConflictNone|**命名参数。** 指定冲突解决方式。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回受影响的行数。|

**异常：**

- BusinessException：对应错误码如下表，详见[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
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
import std.collection.HashMap
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    var rdbStore: RdbStore = getRdbStore(Global.abilityContext,
        StoreConfig(RelationalStoreSecurityLevel.S1, name: "RdbTest.db")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.equalTo("NAME", RelationalStoreValueType.StringValue("TOM"))
    var values = HashMap<String, RelationalStoreValueType>()
    values.add("NAME", RelationalStoreValueType.StringValue("TOM"))
    values.add("AGE", RelationalStoreValueType.Integer(88))
    values.add("SALARY", RelationalStoreValueType.Double(9999.513))
    let count = rdbStore.update(values, predicates, conflict: OnConflictReplace)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```