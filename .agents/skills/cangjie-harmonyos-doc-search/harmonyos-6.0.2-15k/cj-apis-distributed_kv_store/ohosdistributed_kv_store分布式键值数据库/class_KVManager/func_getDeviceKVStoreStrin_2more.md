### func getDeviceKVStore(String, KVOptions)

```cangjie
public func getDeviceKVStore(storeId: String, options: KVOptions): DeviceKVStore
```

**功能：** 通过指定Options和storeId，创建并获取分布式键值数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|storeId|String|是|-|数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#let-max_store_id_length)。|
|options|[KVOptions](#class-kvoptions)|是|-|创建分布式键值实例的配置信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[DeviceKVStore](#class-devicekvstore)|DeviceKVStore对象。多设备协同数据库，数据以设备的维度管理，不存在冲突，支持查询数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |15100002|Open existed database with changed options.|
  |15100003|Database corrupted.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(
    KVManagerConfig(Global.getStageContext(), "com.example.myapplication")) // 需获取Context应用上下文，详见本文使用说明
let opt = KVOptions(
    KVSecurityLevel.S4,
    createIfMissing: true,
    encrypt: false,
    backup: true,
    autoSync: false,
)
let kvStore = kvManager.getDeviceKVStore("myStoreId", opt)
```

### func getSingleKVStore(String, KVOptions)

```cangjie
public func getSingleKVStore(storeId: String, options: KVOptions): SingleKVStore
```

**功能：** 通过指定Options和storeId，创建并获取分布式键值数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|storeId|String|是|-|数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#let-max_store_id_length)。|
|options|[KVOptions](#class-kvoptions)|是|-|创建分布式键值实例的配置信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[SingleKVStore](#class-singlekvstore)|SingleKVStore对象。单版本分布式键值数据库，不对数据所属设备进行区分，提供查询数据和同步数据的方法。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |15100002|Open existed database with changed options.|
  |15100003|Database corrupted.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(
    KVManagerConfig(Global.getStageContext(), "com.example.myapplication")) // 需获取Context应用上下文，详见本文使用说明
let opt = KVOptions(
    KVSecurityLevel.S4,
    createIfMissing: true,
    encrypt: false,
    backup: true,
    autoSync: false,
)
let kvStore = kvManager.getSingleKVStore("myStoreId", opt)
```