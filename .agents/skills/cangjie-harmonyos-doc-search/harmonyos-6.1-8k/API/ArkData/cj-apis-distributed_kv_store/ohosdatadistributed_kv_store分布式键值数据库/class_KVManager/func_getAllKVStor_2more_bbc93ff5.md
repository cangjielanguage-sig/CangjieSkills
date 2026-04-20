### func getAllKVStoreId(String)

```cangjie
public func getAllKVStoreId(appId: String): Array<String>
```

**功能：** 获取所有通过[getKVStore](#func-getkvstoretstring-kvoptions-where-t--singlekvstore)方法创建的且没有调用[deleteKVStore](#func-deletekvstorestring-string)方法删除的分布式键值数据库的storeId。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appId|String|是|-|应用的BundleName，不可为空且长度不大于256。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回所有创建的分布式键值数据库的storeId。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "com.example.myapplication")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    kvManager.getAllKVStoreId("com.example.myapplication")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getKVStore\<T>(String, KVOptions) where T \<: SingleKVStore

```cangjie
public func getKVStore<T>(storeId: String, options: KVOptions): T where T <: SingleKVStore
```

**功能：** 指定options和storeId，创建并获取分布式键值数据库。

> 注意：
>
> 获取已有的分布式键值数据库时，如果数据库文件无法打开（如文件头损坏），将触发自动重建逻辑，并返回新创建的分布式键值数据库实例。建议对重要且无法重新生成的数据使用备份恢复功能，防止数据丢失。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|storeId|String|是|-|数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#static-let-max_store_id_length)，且只能包含字母数字或下划线_。|
|options|[KVOptions](#class-kvoptions)|是|-|创建分布式键值实例的配置信息。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回创建的分布式键值数据库实例（根据kvStoreType的不同，可以创建SingleKVStore实例和DeviceKVStore实例）。|

**异常：**

- BusinessException：对应错误码如下表，详见[分布式键值数据库错误码](./cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15100002 | Open existed database with changed options. |
  | 15100003 | Database corrupted. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "com.example.myapplication")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let opt = KVOptions(
        KVSecurityLevel.S4,
        createIfMissing: true,
        encrypt: false,
        backup: true,
        autoSync: false,
    )
    let kvStore = kvManager.getKVStore("myStoreId", opt)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```