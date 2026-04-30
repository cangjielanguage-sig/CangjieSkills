### func isNull(String)

```cangjie
public func isNull(field: String): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值为null的字段。

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
predicates.isNull("NAME")
```

### func lessThan(String, RelationalStoreValueType)

```cangjie
public func lessThan(field: String, value: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值小于value的字段。

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

// 匹配数据表的"AGE"列中小于20的值
let predicates = RdbPredicates("EMPLOYEE")
predicates.lessThan("AGE", RelationalStoreValueType.integer(20))
```

### func lessThanOrEqualTo(String, RelationalStoreValueType)

```cangjie
public func lessThanOrEqualTo(field: String, value: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值小于或者等于value的字段。

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

// 匹配数据表的"AGE"列中小于等于20的值
let predicates = RdbPredicates("EMPLOYEE")
predicates.lessThanOrEqualTo("AGE", RelationalStoreValueType.integer(20))
```

### func like(String, String)

```cangjie
public func like(field: String, value: String): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值类似于value的字段。

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

// 数据表的"NAME"列中的值类似于"os"的字段，如"Rose"
let predicates = RdbPredicates("EMPLOYEE")
predicates.like("NAME", "%os%")
```