### func limitAs(Int32)

```cangjie
public func limitAs(value: Int32): RdbPredicates
```

**功能：** 设置谓词的最大数据记录数量。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|最大数据记录数，取值应为正整数，传入值小于等于0时，不会限制记录数量。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回可用于设置最大数据记录数的谓词。|

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
        .limitAs(3)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func notBetween(String, RelationalStoreValueType, RelationalStoreValueType)

```cangjie
public func notBetween(field: String, low: RelationalStoreValueType, high: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词以匹配数据表的field列中值超出给定范围的字段（不包含范围边界）。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|low|[RelationalStoreValueType](#enum-relationalstorevaluetype)|是|-|指示与谓词匹配的最小值。|
|high|[RelationalStoreValueType](#enum-relationalstorevaluetype)|是|-|指示要与谓词匹配的最大值。|

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
    // 数据表的"AGE"列中小于10或大于50的值
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.notBetween("AGE", RelationalStoreValueType.Integer(10), RelationalStoreValueType.Integer(50))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func notEqualTo(String, RelationalStoreValueType)

```cangjie
public func notEqualTo(field: String, value: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词以匹配数据表的field列中值不为value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|value|[RelationalStoreValueType](#enum-relationalstorevaluetype)|是|-|指示要与谓词匹配的值。|

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
    // 数据表的"NAME"列中的值不为"Lisa"的字段
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.notEqualTo("NAME", RelationalStoreValueType.StringValue("Lisa"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```