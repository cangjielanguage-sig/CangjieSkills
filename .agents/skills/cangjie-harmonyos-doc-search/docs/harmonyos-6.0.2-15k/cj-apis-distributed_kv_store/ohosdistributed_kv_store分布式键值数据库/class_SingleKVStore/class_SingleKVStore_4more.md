## class SingleKVStore

```cangjie
public open class SingleKVStore {}
```

**功能：** SingleKVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据同步完成的方法。

在调用SingleKVStore的方法前，需要先通过[getSingleKVStore](#func-getsinglekvstorestring-kvoptions)构建一个SingleKVStore实例。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

### func backup(String)

```cangjie
public open func backup(file: String): Unit
```

**功能：** 用指定名称备份数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|String|是|-|备份数据库的指定名称，不能为空且长度不大于[MAX_KEY_LENGTH](#let-max_key_length)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |15100005|Database or result set already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let opt = KVOptions(
    KVSecurityLevel.S4,
    createIfMissing: true,
    encrypt: false,
    backup: true,
    autoSync: false,
)
let singleKVStore = kvManager.getSingleKVStore("myStoreId", opt)
singleKVStore.backup("myBackupfile")
```

### func closeResultSet(KVStoreResultSet)

```cangjie
public open func closeResultSet(resultSet: KVStoreResultSet): Unit
```

**功能：** 关闭由[SingleKVStore.getResultSet](#func-getresultsetstring)返回的KVStoreResultSet对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resultSet|[KVStoreResultSet](#class-kvstoreresultset)|是|-|表示要关闭的KVStoreResultSet对象。|

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
let entries = ArrayList<Entry>()
singleKVStore.putBatch(entries)
let kvStoreResultSet = singleKVStore.getResultSet("batch_test_string_key")
singleKVStore.closeResultSet(kvStoreResultSet)
```

### func commit()

```cangjie
public open func commit(): Unit
```

**功能：** 提交SingleKVStore数据库中的事务。

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

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let opt = KVOptions(
    KVSecurityLevel.S4,
    createIfMissing: true,
    encrypt: false,
    backup: true,
    autoSync: false,
)
let singleKVStore = kvManager.getSingleKVStore("myStoreId", opt)
singleKVStore.commit()
```