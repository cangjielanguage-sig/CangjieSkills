## class KVManager

```cangjie
public class KVManager {}
```

**功能：** 分布式键值数据库管理实例，用于获取分布式键值数据库的相关信息。在调用KVManager的方法前，需要先通过[createKVManager](#static-func-createkvmanagerkvmanagerconfig)构建一个KVManager实例。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### func closeKVStore(String, String)

```cangjie
public func closeKVStore(appId: String, storeId: String): Unit
```

**功能：** 通过storeId的值关闭指定的分布式键值数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appId|String|是|-|应用的BundleName，不可为空且长度不大于256。|
|storeId|String|是|-|要关闭的数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#static-let-max_store_id_length)，且只能包含字母数字或下划线_。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "com.example.myapplication")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    kvManager.closeKVStore("com.example.myapplication", "myStore")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func deleteKVStore(String, String)

```cangjie
public func deleteKVStore(appId: String, storeId: String): Unit
```

**功能：** 通过storeId的值删除指定的分布式键值数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appId|String|是|-|应用的BundleName，不可为空且长度不大于256。|
|storeId|String|是|-|要删除的数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#static-let-max_store_id_length)，且只能包含字母数字或下划线_。|

**异常：**

- BusinessException：对应错误码如下表，详见[分布式键值数据库错误码](./cj-errorcode-distributed_kv_store.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15100004 | Not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let kvManager = DistributedKVStore.createKVManager(KVManagerConfig(Global.abilityContext, "com.example.myapplication")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    kvManager.deleteKVStore("com.example.myapplication", "myStore")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```