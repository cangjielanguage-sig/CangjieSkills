### func between(String, RelationalStoreValueType, RelationalStoreValueType)

```cangjie
public func between(field: String, lowValue: RelationalStoreValueType, highValue: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值在给定范围内的字段（包含范围边界）。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|lowValue|[RelationalStoreValueType](#enum-relationalstorevaluetype)|是|-|指示与谓词匹配的最小值。|
|highValue|[RelationalStoreValueType](#enum-relationalstorevaluetype)|是|-|指示与谓词匹配的最大值。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回与指定字段匹配的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

// 匹配数据表的"AGE"列中大于等于10且小于等于50的值
let predicates = RdbPredicates("EMPLOYEE")
predicates.between("AGE", RelationalStoreValueType.integer(10), RelationalStoreValueType.integer(50))
```

### func contains(String, String)

```cangjie
public func contains(field: String, value: String): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中包含value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

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

// 匹配数据表的"NAME"列中包含"os"的字段，如"Rose"
let predicates = RdbPredicates("EMPLOYEE")
predicates.contains("NAME", "os")
```

### func distinct()

```cangjie
public func distinct(): RdbPredicates
```

**功能：** 配置谓词，以过滤重复记录并仅保留其中一个。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回可用于过滤重复记录的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let predicates = RdbPredicates("EMPLOYEE")
predicates
    .equalTo("NAME", RelationalStoreValueType.string("Rose"))
    .distinct()
```

### func endWrap()

```cangjie
public func endWrap(): RdbPredicates
```

**功能：** 向谓词添加右括号。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回带有右括号的Rdb谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let predicates = RdbPredicates("EMPLOYEE")
predicates
    .equalTo("NAME", RelationalStoreValueType.string("Lisa"))
    .beginWrap()
    .equalTo("AGE", RelationalStoreValueType.integer(18))
    .or()
    .equalTo("SALARY", RelationalStoreValueType.double(200.5))
    .endWrap()
```