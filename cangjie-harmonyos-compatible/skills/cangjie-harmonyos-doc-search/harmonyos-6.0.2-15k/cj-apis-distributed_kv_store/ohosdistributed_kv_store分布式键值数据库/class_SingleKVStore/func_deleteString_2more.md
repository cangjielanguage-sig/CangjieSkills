### func delete(String)

```cangjie
public open func delete(key: String): Unit
```

**功能：** 从数据库中删除指定键值的数据。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要删除数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#let-max_key_length)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |15100003|Database corrupted.|
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
singleKVStore.delete("myKey")
```

### func deleteBackup(ArrayList\<String>)

```cangjie
public open func deleteBackup(files: ArrayList<String>): ArrayList<(String, Int32)>
```

**功能：** 根据指定名称删除备份文件。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|files|ArrayList\<String>|是|-|删除备份文件所指定的名称，不能为空且长度不大于[MAX_KEY_LENGTH](#let-max_key_length)。|

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<(String, Int32)>|返回删除备份的文件名及其处理结果。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*
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
let results = singleKVStore.deleteBackup(ArrayList<String>(["myBackupfile", "BK002"]))
for (result in results) {
    AppLog.info("${result[0]}的删除结果是: ${result[1]}")
}
```