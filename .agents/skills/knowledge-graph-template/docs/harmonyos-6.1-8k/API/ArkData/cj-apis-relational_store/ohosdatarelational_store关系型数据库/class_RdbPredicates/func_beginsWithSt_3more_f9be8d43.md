### func beginsWith(String, String)

```cangjie
public func beginsWith(field: String, value: String): RdbPredicates
```

**功能：** 配置谓词以匹配数据表的field列中以value开头的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|value|String|是|-|指示要与谓词匹配的值。|

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
    // 匹配数据表的"NAME"列中以"Li"开头的字段，如"Lisa"
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.beginsWith("NAME", "Li")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func between(String, RelationalStoreValueType, RelationalStoreValueType)

```cangjie
public func between(field: String, low: RelationalStoreValueType, high: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词以匹配数据表的field列中值在给定范围内的字段（包含范围边界）。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|low|[RelationalStoreValueType](#enum-relationalstorevaluetype)|是|-|指示与谓词匹配的最小值。|
|high|[RelationalStoreValueType](#enum-relationalstorevaluetype)|是|-|指示与谓词匹配的最大值。|

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
    // 匹配数据表的"AGE"列中大于等于10且小于等于50的值
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.between("AGE", RelationalStoreValueType.Integer(10), RelationalStoreValueType.Integer(50))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func contains(String, String)

```cangjie
public func contains(field: String, value: String): RdbPredicates
```

**功能：** 配置谓词以匹配数据表的field列中包含value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|value|String|是|-|指示要与谓词匹配的值。|

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
    // 匹配数据表的"NAME"列中包含"os"的字段，如"Rose"
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.contains("NAME", "os")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```