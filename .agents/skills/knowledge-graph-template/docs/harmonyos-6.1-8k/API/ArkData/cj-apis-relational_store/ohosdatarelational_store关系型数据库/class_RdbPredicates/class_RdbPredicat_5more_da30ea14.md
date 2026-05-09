## class RdbPredicates

```cangjie
public class RdbPredicates {
    public init(name: String)
}
```

**功能：** 表示关系型数据库（RDB）的谓词。该类确定RDB中条件表达式的值是true还是false。谓词间支持多语句拼接，拼接时默认使用and()连接。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### init(String)

```cangjie
public init(name: String)
```

**功能：** 构造函数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|数据库表名。|

### func inValues(String, Array\<RelationalStoreValueType>)

```cangjie
public func inValues(field: String, value: Array<RelationalStoreValueType>): RdbPredicates
```

**功能：** 配置谓词条件，表示字段`field`的值必须在给定的`value`集合内。

> **说明：**
>
> `value`集合不能为空。如果传入空集，此条件将失效，导致操作针对所有数据（如全量查询、更新或删除）。请在调用前判断`value`是否为空集，避免误操作。

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
    // 数据表的"NAME"列中在["Lisa", "Rose"]中的值
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.inValues("NAME", [RelationalStoreValueType.StringValue("Lisa"), RelationalStoreValueType.StringValue("Rose")])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func and()

```cangjie
public func and(): RdbPredicates
```

**功能：** 向谓词添加和条件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回带有和条件的Rdb谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    // 匹配数据表的"NAME"列中的值为"Lisa"且"SALARY"列中的值为"200.5"的字段
    let predicates = RdbPredicates("EMPLOYEE")
    predicates
        .equalTo("NAME", RelationalStoreValueType.StringValue("Lisa"))
        .and()
        .equalTo("SALARY", RelationalStoreValueType.Double(200.5))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func beginWrap()

```cangjie
public func beginWrap(): RdbPredicates
```

**功能：** 向谓词添加左括号。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回带有左括号的Rdb谓词。|

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
        .equalTo("NAME", RelationalStoreValueType.StringValue("Lisa"))
        .beginWrap()
        .equalTo("AGE", RelationalStoreValueType.Integer(18))
        .or()
        .equalTo("SALARY", RelationalStoreValueType.Double(200.5))
        .endWrap()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```