### func limitAs(Int32)

```cangjie
public func limitAs(value: Int32): RdbPredicates
```

**功能：** 设置最大数据记录数的谓词。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|最大数据记录数。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回可用于设置最大数据记录数的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let predicates = RdbPredicates("EMPLOYEE")
predicates
    .equalTo("NAME", RelationalStoreValueType.string("Rose"))
    .limitAs(3)
```

### func notBetween(String, RelationalStoreValueType, RelationalStoreValueType)

```cangjie
public func notBetween(field: String, lowValue: RelationalStoreValueType, highValue: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值超出给定范围的字段（不包含范围边界）。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|lowValue|[RelationalStoreValueType](#enum-relationalstorevaluetype)|是|-|指示与谓词匹配的最小值。|
|highValue|[RelationalStoreValueType](#enum-relationalstorevaluetype)|是|-|指示要与谓词匹配的最大值。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回与指定字段匹配的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

// 数据表的"AGE"列中小于10或大于50的值
let predicates = RdbPredicates("EMPLOYEE")
predicates.notBetween("AGE", RelationalStoreValueType.integer(10), RelationalStoreValueType.integer(50))
```

### func notEqualTo(String, RelationalStoreValueType)

```cangjie
public func notEqualTo(field: String, value: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值不为value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

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

// 数据表的"NAME"列中的值不为"Lisa"的字段
let predicates = RdbPredicates("EMPLOYEE")
predicates.notEqualTo("NAME", RelationalStoreValueType.string("Lisa"))
```