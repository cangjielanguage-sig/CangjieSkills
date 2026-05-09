### func getResultSize(Query)

```cangjie
public func getResultSize(query: Query): Int32
```

**功能：** 获取与本设备指定Query对象匹配的结果数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|query|[Query](#class-query)|是|-|表示查询对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回与本设备指定Query对象匹配的结果数。|

**异常：**

- BusinessException：对应错误码如下表，详见[分布式键值数据库错误码](./cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15100003 | Database corrupted. |
  | 15100005 | Database or result set already closed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let manager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "test_kvstore")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let store = (manager.getKVStore<DeviceKVStore>("test", KVOptions(KVSecurityLevel.S1)) as DeviceKVStore).getOrThrow()
    store.put("key", KVValueType.StringValue("value"))
    let result = store.getResultSize(Query())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```