## class DistributedKVStore

```cangjie
public class DistributedKVStore {}
```

**功能：** 用于创建KVManager类。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### static func createKVManager(KVManagerConfig)

```cangjie
public static func createKVManager(config: KVManagerConfig): KVManager
```

**功能：** 创建一个KVManager对象实例，用于管理数据库对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[KVManagerConfig](#class-kvmanagerconfig)|是|-|提供KVManager实例的配置信息，包括调用方的包名（不能为空）和用户信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[KVManager](#class-kvmanager)|返回创建的KVManager对象实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "com.example.myapplication")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## class Entry

```cangjie
public class Entry {
    public var key: String
    public var value: KVValueType

    public init(key: String, value: KVValueType)
}
```

**功能：** 存储在数据库中的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### var key

```cangjie
public var key: String
```

**功能：** 键值。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### var value

```cangjie
public var value: KVValueType
```

**功能：** 值对象。

**类型：** [KVValueType](#enum-kvvaluetype)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### init(String, KVValueType)

```cangjie
public init(key: String, value: KVValueType)
```

**功能：** 用于创建Entry实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|键值。|
|value|[KVValueType](#enum-kvvaluetype)|是|-|值对象。|