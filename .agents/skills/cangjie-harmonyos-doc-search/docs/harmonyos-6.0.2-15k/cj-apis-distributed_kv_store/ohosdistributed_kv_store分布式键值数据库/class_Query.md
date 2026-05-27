## class Query

```cangjie
public class Query {
    public init()
}
```

**功能：** 使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。一个Query对象中谓词数量上限为256个。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

### init()

```cangjie
public init()
```

**功能：** 用于创建Query实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let query = Query()
```

### func getSqlLike()

```cangjie
public func getSqlLike(): String
```

**功能：** 获取Query对象的查询语句。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回一个字段列中包含对应子串的结果。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

let query = Query()
AppLog.info("query is ${query.getSqlLike()}")
```

### func prefixKey(String)

```cangjie
public func prefixKey(prefix: String): Query
```

**功能：** 创建具有指定键前缀的查询条件。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|prefix|String|是|-|表示指定的键前缀。|

**返回值：**

|类型|说明|
|:----|:----|
|[Query](#class-query)|返回Query对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

let query = Query()
query.prefixKey("$.name")
query.prefixKey("0")
AppLog.info("query is ${query.getSqlLike()}")
query.reset()
```