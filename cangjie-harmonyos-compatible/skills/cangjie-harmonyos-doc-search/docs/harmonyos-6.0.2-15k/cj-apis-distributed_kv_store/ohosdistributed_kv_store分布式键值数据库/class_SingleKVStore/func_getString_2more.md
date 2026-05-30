### func get(String)

```cangjie
public open func get(key: String): KVValueType
```

**功能：** 获取指定键的值。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要查询数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#let-max_key_length)。|

**返回值：**

|类型|说明|
|:----|:----|
|[KVValueType](#enum-kvvaluetype)|返回获取查询的值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |15100003|Database corrupted.|
  |15100004|Not found.|
  |15100005|Database or result set already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let kvStore = kvManager.getDeviceKVStore("test", KVOptions(KVSecurityLevel.S1))
try {
    let value = kvStore.get("myKey")
    match (value) {
        case STRING(v) => AppLog.info("The obtained value is a String: ${v}")
        case INTEGER(v) => AppLog.info("The obtained value is a Int32: ${v}")
        case DOUBLE(v) => AppLog.info("The obtained value is a Float64: ${v}")
        case _ => AppLog.info("The obtained value is of another type.")
    }
} catch (e: BusinessException) {
    AppLog.info("get failed.")
}
```

### func getEntries(String)

```cangjie
public open func getEntries(keyPrefix: String): ArrayList<Entry>
```

**功能：** 获取与指定Query对象匹配的键值对列表。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keyPrefix|String|是|-|表示要匹配的键前缀。|

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<[Entry](#struct-entry)>|返回匹配指定前缀的键值对列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息                           |
  | :----------- | :------------------------------------- |
  | 15100003     | Database corrupted.                    |
  | 15100005     | Database or result set already closed. |

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
let key = "batch_test_string_key"
let entries = ArrayList<Entry>()
for (i in 0..10) {
    entries.add(Entry("${key}${i}", KVValueType.STRING("batch_test_string_value")))
}
singleKVStore.putBatch(entries)
let result = singleKVStore.getEntries(key)
```