## class DistributedKVStore

```cangjie
public class DistributedKVStore {}
```

**功能：** 用于创建KVManager类。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

### static func createKVManager(KVManagerConfig)

```cangjie
public static func createKVManager(config: KVManagerConfig): KVManager
```

**功能：** 创建一个KVManager对象实例，用于管理数据库对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[KVManagerConfig](#struct-kvmanagerconfig)|是|-|提供KVManager实例的配置信息，包括调用方的包名和用户信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[KVManager](#class-kvmanager)|返回创建的KVManager对象实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(
    KVManagerConfig(Global.getStageContext(), "com.example.myapplication")) // 需获取Context应用上下文，详见本文使用说明
```