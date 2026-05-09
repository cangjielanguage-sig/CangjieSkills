## class KVManagerConfig

```cangjie
public class KVManagerConfig {
    public var bundleName: String
    public var context: BaseContext

    public init(context: BaseContext, bundleName: String)
}
```

**功能：** 提供KVManager实例的配置信息，包括调用方的包名和应用的上下文。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### var bundleName

```cangjie
public var bundleName: String
```

**功能：** 调用方的包名。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### var context

```cangjie
public var context: BaseContext
```

**功能：** 应用的上下文。

**类型：** [BaseContext](../AbilityKit/cj-apis-app-ability.md#class-basecontext)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### init(BaseContext, String)

```cangjie
public init(context: BaseContext, bundleName: String)
```

**功能：** 用于创建KVManagerConfig的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[BaseContext](../AbilityKit/cj-apis-app-ability.md#class-basecontext)|是|-|应用的上下文。|
|bundleName|String|是|-|调用方的包名。|

## class KVStoreResultSet

```cangjie
public class KVStoreResultSet {}
```

**功能：** 提供获取数据库结果集的相关方法，包括查询和移动数据读取位置等。同时允许打开的结果集的最大数量为8个。

KVStoreResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。

在调用KVStoreResultSet的方法前，需要先通过[getKVStore](#func-getkvstoretstring-kvoptions-where-t--singlekvstore)构建一个[SingleKVStore](#class-singlekvstore)或者[DeviceKVStore](#class-devicekvstore)实例。

> **说明：**
>
> KVStoreResultSet的游标起始位置为-1。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### func getCount()

```cangjie
public func getCount(): Int32
```

**功能：** 获取结果集的总行数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回数据的总行数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "test_kvstore")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let store = (kvManager.getKVStore<DeviceKVStore>("test", KVOptions(KVSecurityLevel.S1)) as DeviceKVStore).getOrThrow()
    store.put("key", KVValueType.StringValue("value"))
    var resultSet = store.getResultSet("key")
    let count = resultSet.getCount()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```