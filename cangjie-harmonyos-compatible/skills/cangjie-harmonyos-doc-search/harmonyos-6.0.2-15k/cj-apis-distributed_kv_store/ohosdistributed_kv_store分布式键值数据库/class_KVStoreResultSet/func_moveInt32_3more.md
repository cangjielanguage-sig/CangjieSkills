### func move(Int32)

```cangjie
public func move(offset: Int32): Bool
```

**功能：** 将读取位置移动到当前位置的相对偏移量。即当前游标位置向下偏移 offset 行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int32|是|-|表示与当前位置的相对偏移量，负偏移表示向后移动，正偏移表示向前移动。|

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
let moved = resultSet.move(2) // 若当前位置为0，将读取位置从绝对位置为0的位置移动绝对位置为2，行数为3的位置
AppLog.info("moved is ${moved}")
kvStore.closeResultSet(resultSet)
```

### func moveToFirst()

```cangjie
public func moveToFirst(): Bool
```

**功能：** 将读取位置移动到第一行。如果结果集为空，则返回false。

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
let moved = resultSet.moveToFirst()
AppLog.info("moved is ${moved}")
kvStore.closeResultSet(resultSet)
```

### func moveToLast()

```cangjie
public func moveToLast(): Bool
```

**功能：** 将读取位置移动到最后一行。如果结果集为空，则返回false。

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
let moved = resultSet.moveToLast()
AppLog.info("moved is ${moved}")
kvStore.closeResultSet(resultSet)
```