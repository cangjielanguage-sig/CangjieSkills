### func lessThan(String, RelationalStoreValueType)

```cangjie
public func lessThan(field: String, value: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词以匹配数据表的field列中的值小于value的字段。

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
    // 匹配数据表的"AGE"列中小于20的值
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.lessThan("AGE", RelationalStoreValueType.Integer(20))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func lessThanOrEqualTo(String, RelationalStoreValueType)

```cangjie
public func lessThanOrEqualTo(field: String, value: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词以匹配数据表的field列中的值小于或者等于value的字段。

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
    // 匹配数据表的"AGE"列中小于等于20的值
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.lessThanOrEqualTo("AGE", RelationalStoreValueType.Integer(20))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func like(String, String)

```cangjie
public func like(field: String, value: String): RdbPredicates
```

**功能：** 配置模糊查询条件，指定`field`列的模糊匹配条件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|value|String|是|-|指定模糊匹配条件，通常配合通配符使用，`%`表示任意长度任意字符，`_`表示单个字符。|

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
    // 数据表的"NAME"列中的值类似于"os"的字段，如"Rose"
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.like("NAME", "%os%")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```