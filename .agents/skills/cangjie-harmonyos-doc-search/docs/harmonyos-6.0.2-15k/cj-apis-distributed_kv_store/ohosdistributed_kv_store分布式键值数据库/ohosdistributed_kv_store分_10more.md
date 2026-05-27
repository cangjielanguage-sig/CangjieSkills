# ohos.distributed_kv_store（分布式键值数据库）

分布式键值数据库为应用程序提供不同设备间数据库的分布式协同能力。通过调用分布式键值数据库各个接口，应用程序可将数据保存到分布式键值数据库中，并可对分布式键值数据库中的数据进行增加、删除、修改、查询、同步等操作。

该模块提供以下分布式键值数据库相关的常用功能：

- [KVManager](#class-kvmanager)：分布式键值数据库管理实例，用于获取数据库的相关信息。
- [KVStoreResultSet](#class-kvstoreresultset)：提供获取数据库结果集的相关方法，包括查询和移动数据读取位置等。
- [Query](#class-query)：使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。
- [SingleKVStore](#class-singlekvstore)：单版本分布式键值数据库，不对数据所属设备进行区分，设备之间修改相同的key会覆盖，提供查询数据和同步数据的方法。
- [DeviceKVStore](#class-devicekvstore)：设备协同数据库，继承自[SingleKVStore](#class-singlekvstore)，以设备维度对数据进行区分，不存在冲突，支持按照设备的维度提供查询数据和同步数据的方法。

## 导入模块

```cangjie
import kit.ArkData.*
```

## 权限列表

ohos.permission.DISTRIBUTED_DATASYNC

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## let MAX_BATCH_SIZE

```cangjie
public let MAX_BATCH_SIZE = 128
```

**功能：** 最大批处理操作数量。

**类型：** Int64

**起始版本：** 12

## let MAX_KEY_LENGTH

```cangjie
public let MAX_KEY_LENGTH = 1024
```

**功能：** 数据库中Key允许的最大长度，单位字节。如果存在重名符号，推荐使用别名：KV_MAX_KEY_LENGTH。

**类型：** Int64

**起始版本：** 12

## let MAX_KEY_LENGTH_DEVICE

```cangjie
public let MAX_KEY_LENGTH_DEVICE = 896
```

**功能：** 设备协同数据库中key允许的最大长度，单位字节。

**类型：** Int64

**起始版本：** 12

## let MAX_QUERY_LENGTH

```cangjie
public let MAX_QUERY_LENGTH = 512000
```

**功能：** 最大查询长度，单位字节。

**类型：** Int64

**起始版本：** 12

## let MAX_STORE_ID_LENGTH

```cangjie
public let MAX_STORE_ID_LENGTH = 128
```

**功能：** 数据库标识符允许的最大长度，单位字节。

**类型：** Int64

**起始版本：** 12

## let MAX_VALUE_LENGTH

```cangjie
public let MAX_VALUE_LENGTH = 4194303
```

**功能：** 数据库中Value允许的最大长度，单位字节。推荐使用别名：KV_MAX_VALUE_LENGTH。

**类型：** Int64

**起始版本：** 12