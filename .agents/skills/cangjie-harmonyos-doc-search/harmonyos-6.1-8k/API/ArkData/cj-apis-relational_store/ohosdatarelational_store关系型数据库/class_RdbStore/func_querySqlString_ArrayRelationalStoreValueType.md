### func querySql(String, Array\<RelationalStoreValueType>)

```cangjie
public func querySql(sql: String, bindArgs!: Array<RelationalStoreValueType> = []): ResultSet
```

**功能：** 根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#func-queryrdbpredicates-arraystring)或[querySql](#func-querysqlstring-arrayrelationalstorevaluetype)接口获取ResultSet后，调用[getString](#func-getstringint32)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

该接口支持[向量数据库](#class-storeconfig)使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sql|String|是|-|指定要执行的SQL语句。|
|bindArgs|Array\<[RelationalStoreValueType](#enum-relationalstorevaluetype)>|否|[]|**命名参数。** SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。|

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
    let resultSet = rdbStore.querySql("SELECT * FROM EMPLOYEE WHERE NAME = 'Peter'")
    resultSet.goToNextRow()
    let id = resultSet.getLong(resultSet.getColumnIndex("ID"))
    let name = resultSet.getString(resultSet.getColumnIndex("NAME"))
    let age = resultSet.getLong(resultSet.getColumnIndex("AGE"))
    let salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```