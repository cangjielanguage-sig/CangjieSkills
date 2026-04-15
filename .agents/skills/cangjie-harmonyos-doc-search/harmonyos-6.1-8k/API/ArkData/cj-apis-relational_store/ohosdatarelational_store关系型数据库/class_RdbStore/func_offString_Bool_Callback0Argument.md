### func off(String, Bool, ?Callback0Argument)

```cangjie
public func off(event: String, interProcess: Bool, observer!: ?Callback0Argument = None): Unit
```

**功能：** 取消数据变更的事件监听。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|取消订阅事件名称。事件名称与on接口调用时订阅事件的名称一致。|
|interProcess|Bool|是|-|指定是进程间还是本进程取消订阅。<br/> true：进程间。<br/> false：本进程。|
|observer|?[Callback0Argument](../arkinterop/cj-api-callback_invoke.md#class-callback0argument)|否|None|**命名参数。** 该参数存在，则取消指定Callback监听回调，否则取消该event事件的所有监听回调。|

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
class TestCallback1 <: Callback0Argument {
    public init() {}
    public func invoke(err: ?BusinessException): Unit {
        Hilog.info(0, "test", "Call invoke.", "")
    }
}

try {
    var rdbStore: RdbStore = getRdbStore(Global.abilityContext, StoreConfig(RelationalStoreSecurityLevel.S1, name: "RdbTest.db")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let testCallback = TestCallback1()
    rdbStore.on("PRINT", false, testCallback)
    rdbStore.off("PRINT", false, observer: testCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```