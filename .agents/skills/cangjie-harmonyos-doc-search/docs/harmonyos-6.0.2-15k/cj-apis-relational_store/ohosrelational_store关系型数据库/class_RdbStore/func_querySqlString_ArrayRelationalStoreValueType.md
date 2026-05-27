### func querySql(String, Array\<RelationalStoreValueType>)

```cangjie
public func querySql(sql: String, bindArgs!: Array<RelationalStoreValueType> = Array<RelationalStoreValueType>()): ResultSet
```

**功能：** 根据指定SQL语句查询数据库中的数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sql|String|是|-|指定要执行的SQL语句。|
|bindArgs|Array\<[RelationalStoreValueType](#enum-relationalstorevaluetype)>|否|Array\< RelationalStoreValueType>()| **命名参数。** SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。|

**返回值：**

|类型|说明|
|:----|:----|
|[ResultSet](#class-resultset)|如果操作成功，则返回ResultSet对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |14800000|Inner error.|
  |14800014|Already closed.|
  |14800015|The database does not respond.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let resultSet = rdbStore.querySql("SELECT * FROM EMPLOYEE WHERE NAME = 'Peter'")
resultSet.goToNextRow()
let id = resultSet.getLong(resultSet.getColumnIndex("ID"))
let name = resultSet.getString(resultSet.getColumnIndex("NAME"))
let age = resultSet.getLong(resultSet.getColumnIndex("AGE"))
let salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"))
```