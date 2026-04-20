### func deleteBatch(ArrayList\<String>)

```cangjie
public open func deleteBatch(keys: ArrayList<String>): Unit
```

**功能：** 批量删除SingleKVStore数据库中的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keys|ArrayList\<String>|是|-|表示要批量删除的键值对。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |15100003|Database corrupted.|
  |15100005|Database or result set already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import std.collection.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let opt = KVOptions(
    KVSecurityLevel.S4,
    createIfMissing: true,
    encrypt: false,
    backup: true,
    autoSync: false,
)
let singleKVStore = kvManager.getSingleKVStore("myStoreId", opt)
let entries = ArrayList<Entry>()
let keys = ArrayList<String>()
for (i in 0..10) {
    let key = "batch_test_string_key${i}"
    let entry = Entry(key, KVValueType.STRING("batch_test_string_value"))
    entries.add(entry)
    keys.add(key)
}
singleKVStore.putBatch(entries)
singleKVStore.deleteBatch(keys)
```

### func enableSync(Bool)

```cangjie
public open func enableSync(enabled: Bool): Unit
```

**功能：** 设定是否开启同步。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|设定是否开启同步，true表示开启同步，false表示不启用同步。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import std.collection.ArrayList

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let opt = KVOptions(
    KVSecurityLevel.S4,
    createIfMissing: true,
    encrypt: false,
    backup: true,
    autoSync: false,
)
let singleKVStore = kvManager.getSingleKVStore("myStoreId", opt)
let key = "batch_test_string_key"
let entries = ArrayList<Entry>()
for (i in 0..10) {
    entries.add(Entry("${key}${i}", KVValueType.STRING("batch_test_string_value")))
}
singleKVStore.putBatch(entries)
let query = Query().prefixKey("batch_test_string_key")
let result = singleKVStore.getEntries(query)
```