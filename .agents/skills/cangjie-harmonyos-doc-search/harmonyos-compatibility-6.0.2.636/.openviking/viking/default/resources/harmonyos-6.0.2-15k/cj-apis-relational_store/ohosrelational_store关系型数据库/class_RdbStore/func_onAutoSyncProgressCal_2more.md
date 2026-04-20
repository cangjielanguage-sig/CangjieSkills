### func onAutoSyncProgress(Callback1Argument\<ProgressDetails>)

```cangjie
public func onAutoSyncProgress(callback: Callback1Argument<ProgressDetails>): Unit
```

**功能：** 在已打开端云同步，并且网络状态正常的条件下，注册自动同步进度通知，自动同步进行时调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[ProgressDetails](#struct-progressdetails)>|是|-|回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Need 2 - 3  parameter(s)! 2. The RdbStore must be valid. 3. The event must be a not empty string. 4. The progress must be function.|
  |801|Capability not supported.|
  |14800014|Already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TestCallback <: Callback1Argument<ProgressDetails> {
    public init() {}
    public open func invoke(detail: ProgressDetails): Unit {
        AppLog.info("Call invoke.")
    }
}

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let testCallback = TestCallback()
rdbStore.onAutoSyncProgress(testCallback)
```

### func onDataChange(SubscribeType, Callback1Argument\<Array\<String>>)

```cangjie
public func onDataChange(`type`: SubscribeType, callback: Callback1Argument<Array<String>>): Unit
```

**功能：** 注册数据库的数据变更的事件监听。当分布式数据库中的数据发生更改时，将调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[SubscribeType](#enum-subscribetype)|是|-|订阅类型。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<String>>|是|-|回调函数。当type为SUBSCRIBE_TYPE_REMOTE，callback中的Array&lt;String&gt;为数据库中的数据发生改变的对端设备ID。当type为SUBSCRIBE_TYPE_CLOUD，callback中的Array&lt;String&gt;为数据库中的数据发生改变的云端账号。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息        |
  |:-----------|:-------------|
  | 401       | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
  | 801       | Capability not supported. |
  | 14800014  | Already closed.    |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*
import ohos.relational_store.SubscribeType as RSubscribeType

// 此处代码可添加在依赖项定义中
class TestCallback <: Callback1Argument<Array<String>> {
    public init() {}
    public open func invoke(arr: Array<String>): Unit {
        AppLog.info("Call invoke: ${arr}")
    }
}

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let testCallback = TestCallback()
rdbStore.onDataChange(RSubscribeType.SUBSCRIBE_TYPE_REMOTE, testCallback)
```