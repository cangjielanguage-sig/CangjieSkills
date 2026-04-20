### func greaterThanOrEqualTo(String, RelationalStoreValueType)

```cangjie
public func greaterThanOrEqualTo(field: String, value: RelationalStoreValueType): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值大于或者等于value的字段。

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

// 匹配数据表的"AGE"列中大于18的值
let predicates = RdbPredicates("EMPLOYEE")
predicates.greaterThanOrEqualTo("AGE", RelationalStoreValueType.integer(18))
```

### func groupBy(Array\<String>)

```cangjie
public func groupBy(fields: Array<String>): RdbPredicates
```

**功能：** 配置谓词，按指定列分组查询结果。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fields|Array\<String>|是|-|指定分组依赖的列名。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回分组查询列的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let predicates = RdbPredicates("EMPLOYEE")
predicates.groupBy(["AGE", "NAME"])
```

### func inAllDevices()

```cangjie
public func inAllDevices(): RdbPredicates
```

**功能：** 同步分布式数据库时，连接到组网内所有的远程设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

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
predicates.inAllDevices()
```

### func indexedBy(String)

```cangjie
public func indexedBy(field: String): RdbPredicates
```

**功能：** 配置谓词，以指定索引列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|索引列的名称。|

**返回值：**

|类型|说明|
|:----|:----|
|[RdbPredicates](#class-rdbpredicates)|返回具有指定索引列的RdbPredicates。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;  2. Incorrect parameter types.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let predicates = RdbPredicates("EMPLOYEE")
predicates.indexedBy("SALARY")
```

### func isNotNull(String)

```cangjie
public func isNotNull(field: String): RdbPredicates
```

**功能：** 配置谓词，以匹配数据表的field列中的值不为null的字段。

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
predicates.isNotNull("NAME")
```