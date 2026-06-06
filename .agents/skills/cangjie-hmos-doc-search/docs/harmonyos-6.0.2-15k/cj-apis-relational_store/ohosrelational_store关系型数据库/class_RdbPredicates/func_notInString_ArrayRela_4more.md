### func notIn(String, Array\<RelationalStoreValueType>)

```cangjie
public func notIn(field: String, values: Array<RelationalStoreValueType>): RdbPredicates
```

**功能：** 将谓词配置为匹配数据字段为ValueType且值超出给定范围的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|values|Array\<[RelationalStoreValueType](#enum-relationalstorevaluetype)>|是|-|以ValueType数组形式指定的要匹配的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回与指定字段匹配的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

// 数据表的"NAME"列中不在["Lisa", "Rose"]中的值
let predicates = RdbPredicates("EMPLOYEE")
predicates.notIn("NAME", [RelationalStoreValueType.string("Lisa"), RelationalStoreValueType.string("Rose")])
```

### func offsetAs(Int32)

```cangjie
public func offsetAs(rowOffset: Int32): RdbPredicates
```

**功能：** 配置谓词以指定返回结果的起始位置，此方法必须与[limitAs](#func-limitasint32)一起使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rowOffset|Int32|是|-|返回结果的起始位置，取值为正整数。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回具有指定返回结果起始位置的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let predicates = RdbPredicates("EMPLOYEE")
predicates
    .equalTo("NAME", RelationalStoreValueType.string("Rose"))
    .offsetAs(3)
```

### func or()

```cangjie
public func or(): RdbPredicates
```

**功能：** 将或条件添加到谓词中。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回带有或条件的Rdb谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

// 数据表的"NAME"列中的值为"Lisa"或"Rose"的字段
let predicates = RdbPredicates("EMPLOYEE")
predicates
    .equalTo("NAME", RelationalStoreValueType.string("Lisa"))
    .or()
    .equalTo("NAME", RelationalStoreValueType.string("Rose"))
```

### func orderByAsc(String)

```cangjie
public func orderByAsc(field: String): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值按升序排序的列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回与指定字段匹配的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let predicates = RdbPredicates("EMPLOYEE")
predicates.orderByAsc("NAME")
```