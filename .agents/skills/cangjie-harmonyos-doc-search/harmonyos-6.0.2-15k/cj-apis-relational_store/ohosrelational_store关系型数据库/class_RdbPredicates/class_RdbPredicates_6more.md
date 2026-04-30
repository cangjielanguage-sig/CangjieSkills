## class RdbPredicates

```cangjie
public class RdbPredicates {
    public init(name: String)
}
```

**功能：** 表示关系型数据库（RDB）的谓词。该类确定RDB中条件表达式的值是true还是false。该类型不是多线程安全的，如果应用中存在多线程同时操作该类派生出的实例，注意加锁保护。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### init(String)

```cangjie
public init(name: String)
```

**功能：** RdbPredicates类的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|数据库表名。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let predicates = RdbPredicates("EMPLOYEE")
```

### func \`in\`(String, Array\<RelationalStoreValueType>)

```cangjie
public func `in`(field: String, values: Array<RelationalStoreValueType>): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值在给定范围内的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|values|Array\<[RelationalStoreValueType](#enum-relationalstorevaluetype)>|是|-|以RelationalStoreValueType数组形式指定的要匹配的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回与指定字段匹配的谓词。|

### func and()

```cangjie
public func and(): RdbPredicates
```

**功能：** 向谓词添加和条件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回带有和条件的Rdb谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

// 匹配数据表的"NAME"列中的值为"Lisa"且"SALARY"列中的值为"200.5"的字段
let predicates = RdbPredicates("EMPLOYEE")
predicates
    .equalTo("NAME", RelationalStoreValueType.string("Lisa"))
    .and()
    .equalTo("SALARY", RelationalStoreValueType.double(200.5))
```

### func beginWrap()

```cangjie
public func beginWrap(): RdbPredicates
```

**功能：** 向谓词添加左括号。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回带有左括号的Rdb谓词。|

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

### func beginsWith(String, String)

```cangjie
public func beginsWith(field: String, value: String): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中以value开头的字段。

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

// 匹配数据表的"NAME"列中以"Li"开头的字段，如"Lisa"
let predicates = RdbPredicates("EMPLOYEE")
predicates.beginsWith("NAME", "Li")
```