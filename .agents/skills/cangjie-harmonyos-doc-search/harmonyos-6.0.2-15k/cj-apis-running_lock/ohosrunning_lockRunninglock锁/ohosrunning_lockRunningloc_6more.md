# ohos.running_lock（Runninglock锁）

该模块主要提供RunningLock锁相关操作的接口，包括创建、查询、持锁、释放锁等操作。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 权限列表

ohos.permission.RUNNING_LOCK

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func create(String, RunningLockType)

```cangjie
public func create(name: String, `type`: RunningLockType): RunningLock
```

**功能：** 创建RunningLock锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|锁的名字。|
|\`type`|[RunningLockType](#enum-runninglocktype)|是|-|要创建的锁的类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[RunningLock](#class-runninglock)|返回RunningLock锁对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|If the permission is denied.|
  |401|Parameter error. Possible causes: 1.Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let ret = create("running_lock_test", RunningLockType.PROXIMITY_SCREEN_CONTROL)
    AppLog.info("test_runninglock_create success.")
} catch (e: Exception) {
    AppLog.error("test_runninglock_create failed, err: ${e.message.toString()}")
}
```

## func isSupported(RunningLockType)

```cangjie
public func isSupported(`type`: RunningLockType): Bool
```

**功能：** 查询系统是否支持该类型的锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[RunningLockType](#enum-runninglocktype)|是|-|需要查询的锁的类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示支持，返回false表示不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RunningLock锁错误码](../../errorcodes/cj-errorcode-running-lock.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |4900101|Failed to connect to the service.|
  |401|Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let ret = isSupported(RunningLockType.PROXIMITY_SCREEN_CONTROL)
    AppLog.info("test_runninglock_isSupported is : ${ret}")
} catch (e: Exception) {
    AppLog.error("test_runninglock_isSupported failed, err: ${e.message.toString()}")
}
```