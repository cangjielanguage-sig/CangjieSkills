### func query(RdbPredicates, Array\<String>)

```cangjie
public func query(predicates: RdbPredicates, columns!: Array<String> = []): ResultSet
```

**功能：** 根据指定条件查询数据库中的数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#func-queryrdbpredicates-arraystring)或[querySql](#func-querysqlstring-arrayrelationalstorevaluetype)接口获取ResultSet后，调用[getString](#func-getstringint32)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|predicates|[RdbPredicates](#class-rdbpredicates)|是|-|RdbPredicates的实例对象指定的查询条件。|
|columns|Array\<String>|否|[]|**命名参数。** 表示要查询的列。如果值为空，则查询应用于所有列。|

**返回值：**

|类型|说明|
|:----|:----|
|[ResultSet](#class-resultset)|返回ResultSet对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14800000 | Inner error. |
  | 14800014 | The RdbStore or ResultSet is already closed. |
  | 14800015 | The database does not respond. |

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
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.equalTo("NAME", RelationalStoreValueType.StringValue("Rose"))
    let columns = ["ID", "NAME", "AGE", "SALARY", "CODES"]
    let resultSet = rdbStore.query(predicates, columns: columns)
    resultSet.goToNextRow()
    let id = resultSet.getLong(resultSet.getColumnIndex("ID"))
    let name = resultSet.getString(resultSet.getColumnIndex("NAME"))
    let age = resultSet.getLong(resultSet.getColumnIndex("AGE"))
    let salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```