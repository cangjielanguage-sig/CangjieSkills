### func setSyncParam(UInt32)

```cangjie
public open func setSyncParam(defaultAllowedDelayMs: UInt32): Unit
```

**功能：** 设置数据库同步允许的默认延迟。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|defaultAllowedDelayMs|UInt32|是|-|表示数据库同步允许的默认延迟，以毫秒为单位。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(
    KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let opt = KVOptions(
    KVSecurityLevel.S4,
    createIfMissing: true,
    encrypt: false,
    backup: true,
    autoSync: false,
)
let singleKVStore = kvManager.getSingleKVStore("myStoreId", opt)
singleKVStore.setSyncParam(500)
```

### func setSyncRange(ArrayList\<String>, ArrayList\<String>)

```cangjie
public open func setSyncRange(localLabels: ArrayList<String>, remoteSupportLabels: ArrayList<String>): Unit
```

**功能：** 设置同步范围标签。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|localLabels|ArrayList\<String>|是|-|表示本地设备的同步标签。|
|remoteSupportLabels|ArrayList\<String>|是|-|表示要同步数据的设备的同步标签。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import std.collection.*

let kvManager = DistributedKVStore.createKVManager(
    KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let opt = KVOptions(
    KVSecurityLevel.S4,
    createIfMissing: true,
    encrypt: false,
    backup: true,
    autoSync: false,
)
let singleKVStore = kvManager.getSingleKVStore("myStoreId", opt)
let localLabels = ArrayList<String>(["A", "B"])
let remoteSupportLabels = ArrayList<String>(["C", "D"])
singleKVStore.setSyncRange(localLabels, remoteSupportLabels)
```

### func startTransaction()

```cangjie
public open func startTransaction(): Unit
```

**功能：** 启动SingleKVStore数据库中的事务。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |15100005|Database or result set already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(
    KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let opt = KVOptions(
    KVSecurityLevel.S4,
    createIfMissing: true,
    encrypt: false,
    backup: true,
    autoSync: false,
)
let singleKVStore = kvManager.getSingleKVStore("myStoreId", opt)
singleKVStore.startTransaction()
```