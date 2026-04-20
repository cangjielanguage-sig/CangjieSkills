### func notInValues(String, Array\<RelationalStoreValueType>)

```cangjie
public func notInValues(field: String, value: Array<RelationalStoreValueType>): RdbPredicates
```

**功能：** 将谓词配置为匹配数据字段为RelationalStoreValueType且值超出给定范围的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|value|Array\<[RelationalStoreValueType](#enum-relationalstorevaluetype)>|是|-|以RelationalStoreValueType数组形式指定的要匹配的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回与指定字段匹配的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    // 数据表的"NAME"列中不在["Lisa", "Rose"]中的值
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.notInValues("NAME", [RelationalStoreValueType.StringValue("Lisa"), RelationalStoreValueType.StringValue("Rose")])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func offsetAs(Int32)

```cangjie
public func offsetAs(rowOffset: Int32): RdbPredicates
```

**功能：** 设置谓词查询结果返回的起始位置。需要同步调用limitAs接口指定查询数量，否则将无查询结果。如需查询指定偏移位置后的所有行，limitAs接口入参需小于等于0。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rowOffset|Int32|是|-|指定查询结果的起始位置，默认初始位置为结果集的最前端。当rowOffset为负数时，起始位置为结果集的最前端。当rowOffset超出结果集最后位置时，查询结果为空。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回具有指定返回结果起始位置的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let predicates = RdbPredicates("EMPLOYEE")
    predicates
        .equalTo("NAME", RelationalStoreValueType.StringValue("Rose"))
        .offsetAs(3)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func or()

```cangjie
public func or(): RdbPredicates
```

**功能：** 将或条件添加到谓词中。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回带有或条件的Rdb谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    // 数据表的"NAME"列中的值为"Lisa"或"Rose"的字段
    let predicates = RdbPredicates("EMPLOYEE")
    predicates
        .equalTo("NAME", RelationalStoreValueType.StringValue("Lisa"))
        .or()
        .equalTo("NAME", RelationalStoreValueType.StringValue("Rose"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```