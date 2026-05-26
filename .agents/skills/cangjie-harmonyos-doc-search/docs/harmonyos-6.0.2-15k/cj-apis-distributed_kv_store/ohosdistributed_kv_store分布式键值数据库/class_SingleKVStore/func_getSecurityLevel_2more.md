### func getSecurityLevel()

```cangjie
public open func getSecurityLevel(): KVSecurityLevel
```

**功能：** 获取数据库的安全级别。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[KVSecurityLevel](#enum-kvsecuritylevel)|返回数据库的安全级别。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息                           |
  | :----------- | :------------------------------------- |
  | 15100005     | Database or result set already closed. |

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
let securityLevel = singleKVStore.getSecurityLevel()
```

### func offDataChange(Callback1Argument\<ChangeNotification>)

```cangjie
public open func offDataChange(callback: Callback1Argument<ChangeNotification>): Unit
```

**功能：** 取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[ChangeNotification](#class-changenotification)>|是|-|取消订阅的函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[分布式键值数据库错误码](../../errorcodes/cj-errorcode-distributed_kv_store.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1. Mandatory parameters are left unspecified;<br>2. Parameter verification failed.|
  |15100005|Database or result set already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TestCallback <: Callback1Argument<ChangeNotification> {
    public init() {}
    public open func invoke(detail: ChangeNotification): Unit {
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
let testCallback=TestCallback()
singleKVStore.offDataChange(testCallback)
```