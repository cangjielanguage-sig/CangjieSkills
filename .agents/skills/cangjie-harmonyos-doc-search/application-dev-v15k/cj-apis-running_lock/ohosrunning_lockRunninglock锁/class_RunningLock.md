## class RunningLock

```cangjie
public class RunningLock {}
```

**功能：** 阻止系统休眠的锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

下列API示例中都需先使用[create()](#func-createstring-runninglocktype)获取到RunningLock实例，再通过此实例调用对应方法。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let lock = create("running_lock_test_hold", RunningLockType.PROXIMITY_SCREEN_CONTROL)
```

### func hold(Int32)

```cangjie
public func hold(timeout: Int32): Unit
```

**功能：** 锁定和持有RunningLock。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeout|Int32|是|-|锁定和持有RunningLock的时长，单位：毫秒。timeout = -1 表示永久持锁，需要主动释放；timeout = 0 表示3s后超时释放; timeout > 0 表示按传入值超时释放。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RunningLock锁错误码](../../errorcodes/cj-errorcode-running-lock.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |4900101|Failed to connect to the service.|
  |201|If the permission is denied.|
  |401|Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let lock = create("running_lock_test_hold", RunningLockType.PROXIMITY_SCREEN_CONTROL)
    lock.hold(500)
    AppLog.info("test_runninglock_hold success.")
} catch (e: Exception) {
    AppLog.error("test_runninglock_hold failed, err: ${e.message.toString()}")
}
```

### func isHolding()

```cangjie
public func isHolding(): Bool
```

**功能：** 查询当前RunningLock是持有状态还是释放状态。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示当前RunningLock是持有状态，返回false表示当前RunningLock是释放状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RunningLock锁错误码](../../errorcodes/cj-errorcode-running-lock.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |4900101|Failed to connect to the service.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let lock = create("running_lock_test_isHolding", RunningLockType.PROXIMITY_SCREEN_CONTROL)
    let isHolding = lock.isHolding()
    AppLog.info("test_runninglock_isHolding : ${isHolding}")
} catch (e: Exception) {
    AppLog.error("test_runninglock_isHolding failed, err: ${e.message.toString()}")
}
```

### func unhold()

```cangjie
public func unhold(): Unit
```

**功能：** 释放RunningLock锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RunningLock锁错误码](../../errorcodes/cj-errorcode-running-lock.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |4900101|Failed to connect to the service.|
  |201|If the permission is denied.|