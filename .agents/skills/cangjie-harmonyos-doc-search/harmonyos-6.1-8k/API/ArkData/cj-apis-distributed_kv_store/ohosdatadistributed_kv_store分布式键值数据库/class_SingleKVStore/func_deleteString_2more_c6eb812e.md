### func delete(String)

```cangjie
public open func delete(key: String): Unit
```

**功能：** 从数据库中删除指定键值的数据。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要删除数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#static-let-max_key_length)。|

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
    singleKVStore.delete("myKey")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func deleteBatch(Array\<String>)

```cangjie
public open func deleteBatch(keys: Array<String>): Unit
```

**功能：** 批量删除SingleKVStore数据库中的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keys|Array\<String>|是|-|表示要批量删除的键值对，不能为空。|

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
    let deviceKVStore = (kvManager.getKVStore<DeviceKVStore>("myStoreId", opt) as DeviceKVStore).getOrThrow()
    deviceKVStore.deleteBatch(["myBackupfile", "BK002"])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```