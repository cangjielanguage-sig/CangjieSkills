### func isAfterLast()

```cangjie
public func isAfterLast(): Bool
```

**功能：** 检查读取位置是否在最后一行之后。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示读取位置在最后一行之后；返回false表示读取位置不在最后一行之后。|

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
let isAfterLast = resultSet.isAfterLast()
AppLog.info("isAfterLast is ${isAfterLast}")
kvStore.closeResultSet(resultSet)
```

### func isBeforeFirst()

```cangjie
public func isBeforeFirst(): Bool
```

**功能：** 检查读取位置是否在第一行之前。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示读取位置在第一行之前；返回false表示读取位置不在第一行之前。|

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
let isBeforeFirst = resultSet.isBeforeFirst()
AppLog.info("isBeforeFirst is ${isBeforeFirst}")
kvStore.closeResultSet(resultSet)
```

### func isFirst()

```cangjie
public func isFirst(): Bool
```

**功能：** 检查读取位置是否为第一行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示读取位置为第一行；返回false表示读取位置不是第一行。|

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
let isFirst = resultSet.isFirst()
AppLog.info("isFirst is ${isFirst}")
kvStore.closeResultSet(resultSet)
```

### func isLast()

```cangjie
public func isLast(): Bool
```

**功能：** 检查读取位置是否为最后一行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示读取位置为最后一行；返回false表示读取位置不是最后一行。|

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
let isLast = resultSet.isLast()
AppLog.info("isLast is ${isLast}")
kvStore.closeResultSet(resultSet)
```