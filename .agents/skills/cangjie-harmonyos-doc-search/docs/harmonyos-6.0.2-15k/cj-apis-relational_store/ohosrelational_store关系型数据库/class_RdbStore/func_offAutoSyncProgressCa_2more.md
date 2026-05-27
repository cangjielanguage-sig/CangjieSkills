### func offAutoSyncProgress(Callback1Argument\<ProgressDetails>)

```cangjie
public func offAutoSyncProgress(callback: Callback1Argument<ProgressDetails>): Unit
```

**功能：** 取消订阅自动同步进度的通知。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[ProgressDetails](#struct-progressdetails)>|是|-|指已注册的自动同步进度观察者。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息         |
  | :------------ |:--------------------|
  | 401       | Parameter error. Possible causes: 1. Need 1 - 3  parameter(s)! 2. The RdbStore must be valid. 3. The event must be a not empty string. 4. The progress must be function. |
  | 801       | Capability not supported.  |
  | 14800014  | Already closed.       |

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
rdbStore.offAutoSyncProgress(testCallback)
```

### func offAutoSyncProgress()

```cangjie
public func offAutoSyncProgress(): Unit
```

**功能：** 取消订阅所有自动同步进度的通知。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息         |
  | :------------ |:--------------------|
  | 401       | Parameter error. Possible causes: 1. Need 1 - 3  parameter(s)! 2. The RdbStore must be valid. 3. The event must be a not empty string. 4. The progress must be function. |
  | 801       | Capability not supported.  |
  | 14800014  | Already closed.       |

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
rdbStore.offAutoSyncProgress()
```