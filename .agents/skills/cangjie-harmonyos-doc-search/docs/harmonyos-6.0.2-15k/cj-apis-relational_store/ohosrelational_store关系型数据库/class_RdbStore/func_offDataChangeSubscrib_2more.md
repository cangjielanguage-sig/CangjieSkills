### func offDataChange(SubscribeType)

```cangjie
public func offDataChange(`type`: SubscribeType): Unit
```

**功能：** 取消当前type类型下所有数据变更的事件监听。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[SubscribeType](#enum-subscribetype)|是|-|订阅类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息        |
  |:-----------|:-------------|
  | 202       | Permission verification failed, application which is not a system application uses system API. |
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
class TestCallback <: Callback1Argument<Array<ChangeInfo>> {
    public init() {}
    public open func invoke(arr: Array<ChangeInfo>): Unit {
        AppLog.info("Call invoke.")
    }
}

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let testCallback = TestCallback()
rdbStore.onDataChange(RSubscribeType.SUBSCRIBE_TYPE_CLOUD_DETAILS, testCallback)
rdbStore.offDataChange(RSubscribeType.SUBSCRIBE_TYPE_CLOUD_DETAILS)
```

### func on(String, Bool, Callback0Argument)

```cangjie
public func on(event: String, interProcess: Bool, callback: Callback0Argument): Unit
```

**功能：** 注册数据库的进程内或者进程间事件监听。当调用[emit](#func-emitstring)接口时，将调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|订阅事件名称。|
|interProcess|Bool|是|-|指定是进程间还是本进程订阅。<br/> true：进程间。<br/> false：本进程。|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-|回调函数对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |801|Capability not supported.|
  |14800000|Inner error.|
  |14800014|Already closed.|
  |14800050|Failed to obtain subscription service.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TestCallback <: Callback0Argument {
    public init() {}
    public open func invoke(): Unit {
        AppLog.info("Call invoke.")
    }
}

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let testCallback = TestCallback()
rdbStore.on("PRINT", false, testCallback)
```