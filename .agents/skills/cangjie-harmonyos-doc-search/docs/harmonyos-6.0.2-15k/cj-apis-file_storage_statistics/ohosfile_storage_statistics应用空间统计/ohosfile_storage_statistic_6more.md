# ohos.file_storage_statistics（应用空间统计）

该模块提供空间查询相关的常用功能：包括对内外卡的空间查询、对应用分类数据统计的查询、对应用数据的查询等。

## 导入模块

```cangjie
import kit.CoreFileKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getCurrentBundleStats()

```cangjie
public func getCurrentBundleStats(): BundleStats
```

**功能：** 应用获取当前应用存储空间大小（单位为Byte）。

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[BundleStats](#class-bundlestats)|获取指定卷上的应用存储空间大小。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 13600001 | IPC error. |
  | 13900042 | Unknown error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let stats = getCurrentBundleStats()
Hilog.info(0, "storageManager", "app size is: {stats.appSize}")
Hilog.info(0, "storageManager", "cache size is: {stats.cacheSize}")
Hilog.info(0, "storageManager", "data size is: {stats.dataSize}")
```

## func getFreeSize()

```cangjie
public func getFreeSize(): Int64
```

**功能：** 获取内置存储的可用空间大小（单位为Byte）

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回内置存储的可用空间大小（单位为Byte）。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

  | 错误码ID | 错误信息       |
  | :-------- | :-------- |
  | 13600001 | IPC error.     |
  | 13900042 | Unknown error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let size = getFreeSize()
Hilog.info(0, "storageManager", "The total size is: {size}")
```

## func getTotalSize()

```cangjie
public func getTotalSize(): Int64
```

**功能：** 获取内置存储的总空间大小（单位为Byte）。

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回内置存储的总空间大小（单位为Byte）。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

  | 错误码ID | 错误信息       |
  | :-------- | :-------- |
  | 13600001 | IPC error.     |
  | 13900042 | Unknown error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let size = getTotalSize()
Hilog.info(0, "storageManager", "The total size is: {size}")
```