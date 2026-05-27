### func query(RdbPredicates, Array\<String>)

```cangjie
public func query(predicates: RdbPredicates, columns: Array<String>): ResultSet
```

**功能：** 根据指定条件查询数据库中的数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|predicates|[RdbPredicates](#class-rdbpredicates)|是|-|RdbPredicates的实例对象指定的查询条件。|
|columns|Array\<String>|是|-|表示要查询的列。如果值为空，则查询应用于所有列。|

**返回值：**

|类型|说明|
|:----|:----|
|[ResultSet](#class-resultset)|ResultSet对象。|

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
let predicates = RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", RelationalStoreValueType.string("Rose"))
let columns = ["ID", "NAME", "AGE", "SALARY", "CODES"]
let resultSet = rdbStore.query(predicates, columns)
resultSet.goToNextRow()
let id = resultSet.getLong(resultSet.getColumnIndex("ID"))
let name = resultSet.getString(resultSet.getColumnIndex("NAME"))
let age = resultSet.getLong(resultSet.getColumnIndex("AGE"))
let salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"))
```