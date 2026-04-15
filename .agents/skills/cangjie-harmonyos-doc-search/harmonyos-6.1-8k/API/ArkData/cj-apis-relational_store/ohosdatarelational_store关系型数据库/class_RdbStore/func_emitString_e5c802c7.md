### func emit(String)

```cangjie
public func emit(event: String): Unit
```

**功能：** 通知通过[on](#func-onstring-bool-callback0argument)注册的进程间或者进程内监听事件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|通知订阅事件的名称，可自定义事件名称，不能与系统已有事件dataChange，autoSyncProgress，statistics名称重复。|

**异常：**

- BusinessException：对应错误码如下表，详见[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported. |
  | 14800000 | Inner error. |
  | 14800014 | The RdbStore or ResultSet is already closed. |
  | 14800050 | Failed to obtain the subscription service. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import kit.PerformanceAnalysisKit.*
import ohos.callback_invoke.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class TestCallback <: Callback0Argument {
    public init() {}
    public open func invoke(err: ?BusinessException): Unit {
        Hilog.info(0, "test", "Call invoke.", "")
    }
}

try {
    var rdbStore: RdbStore = getRdbStore(Global.abilityContext, StoreConfig(RelationalStoreSecurityLevel.S1, name: "RdbTest.db")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let testCallback = TestCallback()
    rdbStore.on("PRINT", false, testCallback)
    rdbStore.emit("PRINT")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```