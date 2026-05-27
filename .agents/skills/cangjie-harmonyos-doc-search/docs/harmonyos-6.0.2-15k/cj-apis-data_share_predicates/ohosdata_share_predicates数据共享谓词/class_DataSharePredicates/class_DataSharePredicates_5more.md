## class DataSharePredicates

```cangjie
public class DataSharePredicates {
    public init()
}
```

**功能：** 提供用于不同实现不同查询方法的数据共享谓词。

> **说明：**
>
> 该类不是多线程安全的，如果应用中存在多线程同时操作该类派生出的实例，注意加锁保护。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** DataSharePredicates的初始化构造函数。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 19

### func \`in\`(String, Array\<VBValueType>)

```cangjie
public func `in`(field: String, values: Array<VBValueType>): DataSharePredicates
```

**功能：** 用于配置谓词以匹配值在指范围内的字段。目前仅RDB及KVDB(schema)支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|values|Array\<[VBValueType](cj-apis-values_bucket.md#enum-VBValueType)>|是|-|以ValueType数组形式指定的要匹配的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataSharePredicates](#class-datasharepredicates)|返回与指定字段匹配的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let predicates = DataSharePredicates()
predicates.`in`("AGE", [VBValueType.Integer(18), VBValueType.Integer(20)])
```

### func and()

```cangjie
public func and(): DataSharePredicates
```

**功能：** 用于将和条件添加到谓词中。目前仅RDB及KVDB(schema)支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataSharePredicates](#class-datasharepredicates)|返回与指定字段匹配的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let predicates = DataSharePredicates()
predicates.equalTo("NAME", VBValueType.Str("lisi"))
        .and()
        .equalTo("SALARY", VBValueType.Double(200.5))
```

### func equalTo(String, ValueType)

```cangjie
public func equalTo(field: String, value: VBValueType): DataSharePredicates
```

**功能：** 用于配置谓词以匹配值等于指定值的字段。目前仅RDB及KVDB(schema)支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|数据库表中的列名。|
|value|[VBValueType](cj-apis-values_bucket.md#enum-VBValueType)|是|-|指示要与谓词匹配的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataSharePredicates](#class-datasharepredicates)|返回与指定字段匹配的谓词。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let predicates = DataSharePredicates()
predicates.equalTo("NAME", VBValueType.Str("Rose"))
```