### func groupBy(Array\<String>)

```cangjie
public func groupBy(fields: Array<String>): RdbPredicates
```

**功能：** 配置谓词按指定列分组查询结果。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

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
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.groupBy(["AGE", "NAME"])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func inAllDevices()

```cangjie
public func inAllDevices(): RdbPredicates
```

**功能：** 同步分布式数据库时连接到组网内所有的远程设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

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
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.inAllDevices()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isNotNull(String)

```cangjie
public func isNotNull(field: String): RdbPredicates
```

**功能：** 配置谓词以匹配数据表的field列中值不为null的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

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
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.isNotNull("NAME")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isNull(String)

```cangjie
public func isNull(field: String): RdbPredicates
```

**功能：** 配置谓词以匹配数据表的field列中的值为null的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

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
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let predicates = RdbPredicates("EMPLOYEE")
    predicates.isNull("NAME")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```