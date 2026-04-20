## class DeviceKVStore

```cangjie
public class DeviceKVStore <: SingleKVStore {}
```

**功能：** 设备协同数据库，继承自SingleKVStore，提供查询数据和同步数据的方法。

设备协同数据库，以设备维度对数据进行区分，每台设备仅能写入和修改本设备的数据，其它设备的数据对其是只读的，无法修改其它设备的数据。

比如，可以使用设备协同数据库实现设备间的图片分享，可以查看其他设备的图片，但无法修改和删除其他设备的图片。

在调用DeviceKVStore的方法前，需要先通过[getDeviceKVStore](#func-getdevicekvstorestring-kvoptions)构建一个DeviceKVStore实例。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**父类型：**

- [SingleKVStore](#class-singlekvstore)

### func get(String)

```cangjie
public func get(key: String): KVValueType
```

**功能：** 获取本设备指定键的值。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要查询数据的key，不能为空且长度不大于[MAX_KEY_LENGTH_DEVICE](#let-max_key_length_device)。|

**返回值：**

|类型|说明|
|:----|:----|
|[KVValueType](#enum-kvvaluetype)|返回查询获取的值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |15100003|Database corrupted.|
  |15100004|Not found.|
  |15100005|Database or result set already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let manager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let store = manager.getDeviceKVStore("test", KVOptions(KVSecurityLevel.S1))
store.put("key", KVValueType.STRING("value"))
store.get("key")
```

### func getEntries(String)

```cangjie
public func getEntries(keyPrefix: String): ArrayList<Entry>
```

**功能：** 获取本设备与指定Query对象匹配的键值对列表。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

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
store.getEntries("key")
```