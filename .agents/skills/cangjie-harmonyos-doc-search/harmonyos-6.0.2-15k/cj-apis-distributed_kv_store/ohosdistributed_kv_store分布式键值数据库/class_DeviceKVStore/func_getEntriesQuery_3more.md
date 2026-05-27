### func getEntries(Query)

```cangjie
public func getEntries(query: Query): ArrayList<Entry>
```

**功能：** 获取本设备与指定Query对象匹配的键值对列表。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|query|[Query](#class-query)|是|-|表示要匹配的键前缀。|

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<[Entry](#struct-entry)>|返回与指定Query对象匹配的键值对列表。|

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

let manager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let store = manager.getDeviceKVStore("test", KVOptions(KVSecurityLevel.S1))
store.put("key", KVValueType.STRING("value"))
store.getEntries(Query())
```

### func getResultSet(String)

```cangjie
public func getResultSet(keyPrefix: String): KVStoreResultSet
```

**功能：** 获取与本设备指定Query对象匹配的KVStoreResultSet对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keyPrefix|String|是|-|表示要匹配的键前缀。|

**返回值：**

|类型|说明|
|:----|:----|
|[KVStoreResultSet](#class-kvstoreresultset)|获取与本设备指定Query对象匹配的KVStoreResultSet对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |15100001|Over max  limits.|
  |15100003|Database corrupted.|
  |15100005|Database or result set already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let manager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let store = manager.getDeviceKVStore("test", KVOptions(KVSecurityLevel.S1))
store.put("key", KVValueType.STRING("value"))
store.getResultSet("key")
```

### func getResultSet(Query)

```cangjie
public func getResultSet(query: Query): KVStoreResultSet
```

**功能：** 获取与本设备指定Query对象匹配的KVStoreResultSet对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|query|[Query](#class-query)|是|-|表示查询对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[KVStoreResultSet](#class-kvstoreresultset)|获取与本设备指定Query对象匹配的KVStoreResultSet对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |15100001|Over max  limits.|
  |15100003|Database corrupted.|
  |15100005|Database or result set already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let manager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let store = manager.getDeviceKVStore("test", KVOptions(KVSecurityLevel.S1))
store.put("key", KVValueType.STRING("value"))
store.getResultSet(Query())
```