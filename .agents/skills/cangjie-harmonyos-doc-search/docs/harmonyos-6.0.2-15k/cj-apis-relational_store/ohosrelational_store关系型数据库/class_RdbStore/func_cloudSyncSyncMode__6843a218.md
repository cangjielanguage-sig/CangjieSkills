### func cloudSync(SyncMode, Callback1Argument\<ProgressDetails>)

```cangjie
public func cloudSync(mode: SyncMode, callback: Callback1Argument<ProgressDetails>): Unit
```

**功能：** 手动执行对所有分布式表的端云同步，使用该接口需要实现云服务功能。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[SyncMode](#enum-syncmode)|是|-|指定同步的表名。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[ProgressDetails](#struct-progressdetails)>|是|-|用来处理数据库同步详细信息的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息    |
  |:-----------|:------------------|
  | 401       | Parameter error. Possible causes: 1. Need 2 - 4  parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The progress must be a callback type. |
  | 801       | Capability not supported.   |
  | 14800014  | Already closed.           |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*
import ohos.relational_store.SyncMode as RSyncMode

// 此处代码可添加在依赖项定义中
class TestCallback <: Callback1Argument<ProgressDetails> {
    public init() {}
    public open func invoke(detail: ProgressDetails): Unit {
        AppLog.info("Call invoke.")
    }
}

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(), StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let testCallback = TestCallback()
rdbStore.cloudSync(RSyncMode.SYNC_MODE_CLOUD_FIRST, ["EMPLOYEE"], testCallback)
```