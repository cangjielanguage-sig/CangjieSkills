### func offDataChange(SubscribeType, Callback1Argument\<Array\<String>>)

```cangjie
public func offDataChange(`type`: SubscribeType, callback: Callback1Argument<Array<String>>): Unit
```

**功能：** 取消数据变更的事件监听。

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
rdbStore.offDataChange(RSubscribeType.SUBSCRIBE_TYPE_REMOTE, testCallback)
```