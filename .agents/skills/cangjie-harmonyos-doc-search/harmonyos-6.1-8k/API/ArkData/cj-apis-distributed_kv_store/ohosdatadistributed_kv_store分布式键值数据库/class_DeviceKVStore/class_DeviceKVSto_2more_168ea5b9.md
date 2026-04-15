## class DeviceKVStore

```cangjie
public class DeviceKVStore <: SingleKVStore {}
```

**功能：** 设备协同数据库，继承自SingleKVStore，提供查询数据和端端同步数据的方法，可以使用SingleKVStore的方法例如：put、putBatch等。

设备协同数据库，以设备维度对数据进行区分，每台设备仅能写入和修改本设备的数据，其它设备的数据对其是只读的，无法修改其它设备的数据。

比如，可以使用设备协同数据库实现设备间的图片分享，可以查看其他设备的图片，但无法修改和删除其他设备的图片。

在调用DeviceKVStore的方法前，需要先通过[getKVStore](#func-getkvstoretstring-kvoptions-where-t--singlekvstore)构建一个DeviceKVStore实例。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

**父类型：**

- [SingleKVStore](#class-singlekvstore)

### func get(String)

```cangjie
public func get(key: String): KVValueType
```

**功能：** 获取本设备指定键的值。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要查询数据的key，不能为空且长度不大于[MAX_KEY_LENGTH_DEVICE](#static-let-max_key_length_device)。|

**返回值：**

|类型|说明|
|:----|:----|
|[KVValueType](#enum-kvvaluetype)|返回查询获取的值。|

**异常：**

- BusinessException：对应错误码如下表，详见[分布式键值数据库错误码](./cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15100003 | Database corrupted. |
  | 15100004 | Not found. |
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
    store.get("key")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```