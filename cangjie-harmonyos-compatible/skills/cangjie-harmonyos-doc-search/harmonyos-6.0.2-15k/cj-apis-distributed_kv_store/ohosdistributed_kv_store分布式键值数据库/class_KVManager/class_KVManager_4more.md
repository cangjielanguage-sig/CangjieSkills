## class KVManager

```cangjie
public class KVManager {}
```

**功能：** 分布式键值数据库管理实例，用于获取分布式键值数据库的相关信息。在调用KVManager的方法前，需要先通过[createKVManager](#static-func-createkvmanagerkvmanagerconfig)构建一个KVManager实例。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

### func closeKVStore(String, String)

```cangjie
public func closeKVStore(appId: String, storeId: String): Unit
```

**功能：** 通过storeId的值关闭指定的分布式键值数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appId|String|是|-|所调用数据库方的包名。|
|storeId|String|是|-|要关闭的数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#let-max_store_id_length)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "com.example.myapplication")) // 需获取Context应用上下文，详见本文使用说明
kvManager.closeKVStore("com.example.myapplication", "myStore")
```

### func deleteKVStore(String, String)

```cangjie
public func deleteKVStore(appId: String, storeId: String): Unit
```

**功能：** 通过storeId的值删除指定的分布式键值数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appId|String|是|-|所调用数据库方的包名。|
|storeId|String|是|-|要删除的数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#let-max_store_id_length)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |15100004|Not found.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "com.example.myapplication")) // 需获取Context应用上下文，详见本文使用说明
kvManager.deleteKVStore("com.example.myapplication", "myStore")
```

### func getAllKVStoreId(String)

```cangjie
public func getAllKVStoreId(appId: String): Array<String>
```

**功能：** 获取所有通过[getSingleKVStore](#func-getsinglekvstorestring-kvoptions)或者[getDeviceKVStore](#func-getdevicekvstorestring-kvoptions)方法创建、且未调用[deleteKVStore](#func-deletekvstorestring-string)方法删除的分布式键值数据库的storeId。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appId|String|是|-|所调用数据库方的包名。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回所有创建的分布式键值数据库的storeId。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "com.example.myapplication")) // 需获取Context应用上下文，详见本文使用说明
kvManager.getAllKVStoreId("com.example.myapplication")
```