### func setDistributedTables(Array\<String>, DistributedType, DistributedConfig)

```cangjie
public func setDistributedTables(tables: Array<String>, `type`: DistributedType, config: DistributedConfig): Unit
```

**功能：** 设置分布式数据库表。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tables|Array\<String>|是|-|要设置的分布式数据库表表名。|
|\`type\`|[DistributedType](#enum-distributedtype)|是|-|表的分布式类型。|
|config|[DistributedConfig](#struct-distributedconfig)|是|-|表的分布式配置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  | 错误码ID | 错误信息                                                 |
  |:-----------| :------------------------------------------------------------ |
  | 401       | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
  | 801       | Capability not supported. |
  | 14800000  | Inner error. |
  | 14800014  | Already closed. |
  | 14800051  | The type of the distributed table does not match. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
var arrStr=["EMPLOYEE", "EMPLOYER"]
rdbStore.setDistributedTables(arrStr, DistributedType.DISTRIBUTED_CLOUD, DistributedConfig(true))
```

### func sync(SyncMode, RdbPredicates)

```cangjie
public func sync(mode: SyncMode, predicates: RdbPredicates): Array<(String, Int32)>
```

**功能：** 在设备之间同步数据。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[SyncMode](#enum-syncmode)|是|-|指同步模式。该值可以是SyncMode.SYNC_MODE_PUSH、SyncMode.SYNC_MODE_PULL。|
|predicates|[RdbPredicates](#class-rdbpredicates)|是|-|约束同步数据和设备。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<(String, Int32)>|String：设备ID；Int32：每个设备同步状态，0表示成功，其他值表示失败。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |801|Capability not supported.|
  |14800000|Inner error.|
  |14800014|Already closed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.relational_store.SyncMode as RSyncMode

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let predicates = RdbPredicates("EMPLOYEE")
predicates.inAllDevices()
rdbStore.sync(RSyncMode.SYNC_MODE_PULL, predicates)
```