### func put(String, KVValueType)

```cangjie
public open func put(key: String, value: KVValueType): Unit
```

**功能：** 添加指定类型键值对到数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要添加数据的Key，不能为空且长度不大于[MAX_KEY_LENGTH](#static-let-max_key_length)。|
|value|[KVValueType](#enum-kvvaluetype)|是|-|要添加数据的value，支持Array\<UInt8>、Int32、Float32、Float64、String、Bool，Array\<UInt8>、String 的长度不大于[MAX_VALUE_LENGTH](#static-let-max_value_length)。|

**异常：**

- BusinessException：对应错误码如下表，详见[分布式键值数据库错误码](./cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15100003 | Database corrupted.|
  | 15100005 | Database or result set already closed.|
  | 14800047 | The WAL file size exceeds the default limit.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

let kvManager = DistributedKVStore.createKVManager(
    KVManagerConfig(Global.abilityContext, "test_kvstore")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
let kvStore = (kvManager.getKVStore<DeviceKVStore>("test", KVOptions(KVSecurityLevel.S1)) as DeviceKVStore).getOrThrow()
try {
    kvStore.put("myKey", StringValue("myValue"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "put failed.", "")
}
```

### func putBatch(Array\<Entry>)

```cangjie
public open func putBatch(entries: Array<Entry>): Unit
```

**功能：** 批量插入键值对到SingleKVStore数据库中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|entries|Array\<[Entry](#class-entry)>|是|-|表示要批量插入的键值对。一个entries对象中允许的最大数据量为512M。|

**异常：**

- BusinessException：对应错误码如下表，详见[分布式键值数据库错误码](./cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15100003 | Database corrupted.|
  | 15100005 | Database or result set already closed.|
  | 14800047 | The WAL file size exceeds the default limit.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import std.collection.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let kvManager = DistributedKVStore.createKVManager(
        KVManagerConfig(Global.abilityContext, "test_kvstore")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let opt = KVOptions(
        KVSecurityLevel.S4,
        createIfMissing: true,
        encrypt: false,
        backup: true,
        autoSync: false,
    )
    let singleKVStore = kvManager.getKVStore("myStoreId", opt)
    let entries = ArrayList<Entry>()
    for (i in 0..10) {
        let entry = Entry("batch_test_string_key${i}", StringValue("batch_test_string_value"))
        entries.add(entry)
    }
    singleKVStore.putBatch(entries.toArray())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```