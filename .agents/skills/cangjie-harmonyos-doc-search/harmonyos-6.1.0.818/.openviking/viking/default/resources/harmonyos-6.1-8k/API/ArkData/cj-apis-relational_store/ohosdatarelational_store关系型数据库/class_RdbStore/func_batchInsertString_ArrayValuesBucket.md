### func batchInsert(String, Array\<ValuesBucket>)

```cangjie
public func batchInsert(table: String, values: Array<ValuesBucket>): Int64
```

**功能：** 向目标表中插入一组数据。

该接口支持[向量数据库](#class-storeconfig)使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|table|String|是|-|指定的目标表名。|
|values|Array\<[ValuesBucket](#type-valuesbucket)>|是|-|表示要插入到表中的一组数据。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|如果操作成功，返回插入的数据个数，否则返回-1。|

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
import std.collection.{HashMap, Map}
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    var rdbStore: RdbStore = getRdbStore(Global.abilityContext, StoreConfig(RelationalStoreSecurityLevel.S1, name: "RdbTest.db")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    var values1 = HashMap<String, RelationalStoreValueType>()
    values1.add("ID", RelationalStoreValueType.Integer(1))
    values1.add("NAME", RelationalStoreValueType.StringValue("Lisa"))
    values1.add("AGE", RelationalStoreValueType.Integer(18))
    values1.add("SALARY", RelationalStoreValueType.Double(100.5))
    var values2 = HashMap<String, RelationalStoreValueType>()
    values2.add("ID", RelationalStoreValueType.Integer(2))
    values2.add("NAME", RelationalStoreValueType.StringValue("Jack"))
    values2.add("AGE", RelationalStoreValueType.Integer(19))
    values2.add("SALARY", RelationalStoreValueType.Double(101.5))
    var values3 = HashMap<String, RelationalStoreValueType>()
    values3.add("ID", RelationalStoreValueType.Integer(3))
    values3.add("NAME", RelationalStoreValueType.StringValue("Tom"))
    values3.add("AGE", RelationalStoreValueType.Integer(20))
    values3.add("SALARY", RelationalStoreValueType.Double(102.5))
    let valueBuckets: Array<Map<String, RelationalStoreValueType>>= [values1, values2, values3]
    let count = rdbStore.batchInsert("EMPLOYEE", valueBuckets)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```