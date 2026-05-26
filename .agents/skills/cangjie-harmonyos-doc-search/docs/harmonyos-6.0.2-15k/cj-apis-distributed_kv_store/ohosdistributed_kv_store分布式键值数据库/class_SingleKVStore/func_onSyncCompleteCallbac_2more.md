### func onSyncComplete(Callback1Argument\<ArrayList\<(String, Int32)>>)

```cangjie
public open func onSyncComplete(callback: Callback1Argument<ArrayList<(String, Int32)>>): Unit
```

**功能：** 订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<ArrayList\<(String, Int32)>>|是|-|回调函数。用于向调用方发送同步结果的回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1. Mandatory parameters are left unspecified;<br>2. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TestCallback <: Callback1Argument<ArrayList<(String, Int32)>> {
    public init() {}
    public open func invoke(detail: ArrayList<(String, Int32)>): Unit {
        AppLog.info("Call invoke.")
    }
}

let kvManager = DistributedKVStore.createKVManager(
    KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let opt = KVOptions(
    KVSecurityLevel.S4,
    createIfMissing: true,
    encrypt: false,
    backup: true,
    autoSync: false,
)
let singleKVStore = kvManager.getSingleKVStore("myStoreId", opt)
let testCallback = TestCallback()
singleKVStore.onSyncComplete(testCallback)
```

### func put(String, KVValueType)

```cangjie
public open func put(key: String, value: KVValueType): Unit
```

**功能：** 添加指定类型键值对到数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要添加数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#let-max_key_length)。|
|value|[KVValueType](#enum-kvvaluetype)|是|-|要添加数据的value，支持Array\<UInt8>、String、Int32、Bool、Float32、Float64 ，Array\<UInt8>、String 的长度不大于[MAX_VALUE_LENGTH](#let-max_value_length)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

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
import ohos.base.*

let kvManager = DistributedKVStore.createKVManager(
    KVManagerConfig(Global.getStageContext(), "test_kvstore")) // 需获取Context应用上下文，详见本文使用说明
let kvStore = kvManager.getDeviceKVStore("test", KVOptions(KVSecurityLevel.S1))
try {
    kvStore.put("myKey", KVValueType.STRING("myValue"))
} catch (e: BusinessException) {
    AppLog.info("put failed.")
}
```