### func putBatch(ArrayList\<Entry>)

```cangjie
public open func putBatch(entries: ArrayList<Entry>): Unit
```

**功能：** 批量插入键值对到SingleKVStore数据库中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|entries|ArrayList\<[Entry](#struct-entry)>|是|-|表示要批量插入的键值对。一个entries对象中允许的最大数据量为512M。|

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
let entries = ArrayList<Entry>()
for (i in 0..10) {
    let entry = Entry("batch_test_string_key${i}", KVValueType.("batch_test_string_value")
    )
    entries.add(entry)
}
singleKVStore.putBatch(entries)
```

### func restore(String)

```cangjie
public open func restore(file: String): Unit
```

**功能：** 从指定的数据库文件恢复数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|String|是|-|指定的数据库文件名称，不能为空且长度不大于[MAX_KEY_LENGTH](#let-max_key_length)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
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
singleKVStore.restore("myBackupfile")
```

### func rollback()

```cangjie
public open func rollback(): Unit
```

**功能：** 在SingleKVStore数据库中回滚事务。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |15100004|Not found.|
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
singleKVStore.rollback()
```