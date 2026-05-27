### func offDistributedDataServiceDie(Callback0Argument)

```cangjie
public func offDistributedDataServiceDie(callback: Callback0Argument): Unit
```

**功能：** 取消指定的订阅服务状态变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-|指定的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "com.example.myapplication")) // 需获取Context应用上下文，详见本文使用说明
kvManager.offDistributedDataServiceDie()
```

### func offDistributedDataServiceDie()

```cangjie
public func offDistributedDataServiceDie(): Unit
```

**功能：** 取消所有订阅服务状态变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "com.example.myapplication")) // 需获取Context应用上下文，详见本文使用说明
kvManager.offDistributedDataServiceDie()
```

### func onDistributedDataServiceDie(Callback0Argument)

```cangjie
public func onDistributedDataServiceDie(callback: Callback0Argument): Unit
```

**功能：** 订阅服务状态变更通知。如果服务终止，需要重新注册数据变更通知和同步完成事件回调通知，并且同步操作会返回失败。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-|回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.|

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

let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.getStageContext(), "com.example.myapplication")) // 需获取Context应用上下文，详见本文使用说明
let testCallback = TestCallback()
kvManager.onDistributedDataServiceDie(testCallback)
```