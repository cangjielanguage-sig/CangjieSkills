### func enableSync(Bool)

```cangjie
public open func enableSync(enabled: Bool): Unit
```

**功能：** 设定是否开启同步。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|设定是否开启端端同步，true表示开启端端同步，false表示不启用端端同步。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import std.collection.ArrayList
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "test_kvstore")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let opt = KVOptions(
        KVSecurityLevel.S4,
        createIfMissing: true,
        encrypt: false,
        backup: true,
        autoSync: false,
    )
    let singleKVStore = kvManager.getKVStore("myStoreId", opt)
    singleKVStore.enableSync(true)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func get(String)

```cangjie
public open func get(key: String): KVValueType
```

**功能：** 获取指定键的值。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要查询数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#static-let-max_key_length)。|

**返回值：**

|类型|说明|
|:----|:----|
|[KVValueType](#enum-kvvaluetype)|返回获取查询的值。|

**异常：**

- BusinessException：对应错误码如下表，详见[分布式键值数据库错误码](./cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15100003 | Database corrupted.|
  | 15100004 | Not found.|
  | 15100005 | Database or result set already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "test_kvstore")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
let kvStore = (kvManager.getKVStore<DeviceKVStore>("test", KVOptions(KVSecurityLevel.S1)) as DeviceKVStore).getOrThrow()
try {
    let value = kvStore.get("myKey")
    match (value) {
        case StringValue(v) => Hilog.info(0, "test", "The obtained value is a String: ${v}", "")
        case Integer(v) => Hilog.info(0, "test", "The obtained value is a Int32: ${v}", "")
        case Double(v) => Hilog.info(0, "test", "The obtained value is a Float64: ${v}", "")
        case _ => Hilog.info(0, "test", "The obtained value is of another type.", "")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "get failed.", "")
}
```