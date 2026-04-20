### func startTransaction()

```cangjie
public open func startTransaction(): Unit
```

**功能：** 启动SingleKVStore数据库中的事务。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[分布式键值数据库错误码](./cj-errorcode-distributed_kv_store.md)和[关系型数据库错误码](./cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15100005 | Database or result set already closed.|
  | 14800047 | The WAL file size exceeds the default limit.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let kvManager = DistributedKVStore.createKVManager(
        KVManagerConfig(Global.abilityContext, "test_kvstore")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let opt = KVOptions(
        KVSecurityLevel.S4,
        createIfMissing: true,
        encrypt: false,
        backup: true,
        autoSync: false,
    )
    let singleKVStore = kvManager.getKVStore("myStoreId", opt)
    singleKVStore.startTransaction()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```