### func getResultSet(String)

```cangjie
public func getResultSet(keyPrefix: String): KVStoreResultSet
```

**功能：** 从DeviceKVStore数据库中获取本设备具有指定前缀的结果集。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keyPrefix|String|是|-|表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。|

**返回值：**

|类型|说明|
|:----|:----|
|[KVStoreResultSet](#class-kvstoreresultset)|返回具有指定前缀的结果集。|

**异常：**

- BusinessException：对应错误码如下表，详见[分布式键值数据库错误码](./cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15100001 | Over max limits. |
  | 15100003 | Database corrupted. |
  | 15100005 | Database or result set already closed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let manager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "test_kvstore")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let store = (manager.getKVStore<DeviceKVStore>("test", KVOptions(KVSecurityLevel.S1)) as DeviceKVStore).getOrThrow()
    store.put("key", KVValueType.StringValue("value"))
    store.getResultSet("key")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getResultSet(Query)

```cangjie
public func getResultSet(query: Query): KVStoreResultSet
```

**功能：** 获取与指定设备ID和Query对象匹配的KVStoreResultSet对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|query|[Query](#class-query)|是|-|表示查询对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[KVStoreResultSet](#class-kvstoreresultset)|获取与本设备指定Query对象匹配的KVStoreResultSet对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[分布式键值数据库错误码](./cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15100001 | Over max limits.|
  | 15100003 | Database corrupted.|
  | 15100005 | Database or result set already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let manager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "test_kvstore")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let store = (manager.getKVStore<DeviceKVStore>("test", KVOptions(KVSecurityLevel.S1)) as DeviceKVStore).getOrThrow()
    store.put("key", KVValueType.StringValue("value"))
    store.getResultSet(Query())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```