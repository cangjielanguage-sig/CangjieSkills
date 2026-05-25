### func moveToNext()

```cangjie
public func moveToNext(): Bool
```

**功能：** 将读取位置移动到下一行。如果结果集为空，则返回false。适用于全量获取数据库结果集的场景。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示操作成功；返回false则表示操作失败。|

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
let moved = resultSet.moveToNext()
AppLog.info("moved is ${moved}")
kvStore.closeResultSet(resultSet)
```

### func moveToPosition(Int32)

```cangjie
public func moveToPosition(position: Int32): Bool
```

**功能：** 将读取位置从0移动到指定的绝对位置。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|position|Int32|是|-|表示绝对位置。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示操作成功；返回false则表示操作失败。|

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
let moved = resultSet.moveToPosition(1)
AppLog.info("moved is ${moved}")
kvStore.closeResultSet(resultSet)
```

### func moveToPrevious()

```cangjie
public func moveToPrevious(): Bool
```

**功能：** 将读取位置移动到上一行。如果结果集为空，则返回false。适用于全量获取数据库结果集的场景。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示操作成功；返回false则表示操作失败。|

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
let moved = resultSet.moveToPrevious()
AppLog.info("moved is ${moved}")
kvStore.closeResultSet(resultSet)
```