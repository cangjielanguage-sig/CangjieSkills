## class KVStoreResultSet

```cangjie
public class KVStoreResultSet {}
```

**功能：** 提供获取数据库结果集的相关方法，包括查询和移动数据读取位置等。允许打开的结果集最大数量为8个。

在调用KVStoreResultSet的方法前，需要先通过[getSingleKVStore](#func-getsinglekvstorestring-kvoptions)或者[getDeviceKVStore](#func-getdevicekvstorestring-kvoptions)构建一个SingleKVStore或者DeviceKVStore实例。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

### func getCount()

```cangjie
public func getCount(): Int32
```

**功能：** 获取结果集的总行数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回数据的总行数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let store = kvManager.getDeviceKVStore("test", KVOptions(KVSecurityLevel.S1))
store.put("key", KVValueType.STRING("value"))
var resultSet = store.getResultSet("key")
resultSet.getCount()
```

### func getEntry()

```cangjie
public func getEntry(): Entry
```

**功能：** 从当前位置获取对应的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Entry](#struct-entry)|返回键值对。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let kvStore = kvManager.getDeviceKVStore("test", KVOptions(KVSecurityLevel.S1))
kvStore.put("key", KVValueType.STRING("value"))
let resultSet = kvStore.getResultSet("batch_test_string_key")
resultSet.moveToFirst()
let entry = resultSet.getEntry()
AppLog.info("entry: Key is ${entry.key}. Value is ${entry.value}.")
kvStore.closeResultSet(resultSet)
```

### func getPosition()

```cangjie
public func getPosition(): Int32
```

**功能：** 获取结果集中当前的读取位置。读取位置会因[moveToFirst](#func-movetofirst)、[moveToLast](#func-movetolast)等操作而发生变化。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回当前读取位置。取值范围 >= -1，值为 -1 时表示还未开始读取，值为 0 时表示第一行。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let kvStore = kvManager.getDeviceKVStore("test", KVOptions(KVSecurityLevel.S1))
kvStore.put("key", KVValueType.STRING("value"))
let resultSet = kvStore.getResultSet("batch_test_string_key")
let position = resultSet.getPosition()
AppLog.info("position is ${position}")
kvStore.closeResultSet(resultSet)
```