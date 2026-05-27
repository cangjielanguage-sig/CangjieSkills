### func emit(String)

```cangjie
public func emit(event: String): Unit
```

**功能：** 通知通过[on](#func-onstring-bool-callback0argument)注册的进程间或者进程内监听事件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|通知订阅事件的名称。|

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

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(), StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let testCallback = TestCallback()
rdbStore.on("PRINT", false, testCallback)
rdbStore.emit("PRINT")
```

### func executeSql(String)

```cangjie
public func executeSql(sql: String): Unit
```

**功能：** 提供管理关系数据库(RDB)方法的接口。在使用以下相关接口前，请使用[executeSql](#func-executesqlstring)接口初始化数据库表结构和相关数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sql|String|是|-|设置和获取数据库版本，值为大于等于0的整数。|