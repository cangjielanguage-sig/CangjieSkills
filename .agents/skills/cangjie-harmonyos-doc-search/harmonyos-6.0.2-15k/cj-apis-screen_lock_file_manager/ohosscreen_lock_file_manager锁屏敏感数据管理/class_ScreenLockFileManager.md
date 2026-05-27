## class ScreenLockFileManager

```cangjie
public class ScreenLockFileManager {}
```

**功能：** 锁屏敏感数据管理模块类。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

### static func acquireAccess()

```cangjie
public static func acquireAccess(): AccessStatus
```

**功能：** 以同步方法申请锁屏下应用敏感数据访问权限。锁屏后，敏感数据无法被访问，但可通过调用该方法，访问指定类型的敏感数据。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AccessStatus](#enum-accessstatus)|锁屏下敏感数据访问权限申请的状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[锁屏敏感数据管理错误码](../../errorcodes/cj-errorcode-screen_lock_file_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID  | 错误信息  |
  | :------- | :---------------------------------- |
  | 801 | The specified SystemCapability name was not found. |
  | 29300002 | The system ability work abnormally. |
  | 29300003 | The application is not enabled the data protection under lock screen. |
  | 29300004 | File access is denied. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.base.*

try {
    let status = ScreenLockFileManager.acquireAccess()
    match (status) {
        case ACCESS_DENIED => AppLog.info("ACCESS_DENIED")
        case ACCESS_GRANTED => AppLog.info("ACCESS_GRANTED")
        case _ => throw IllegalArgumentException("The type is not supported.")
    }
} catch (e: BusinessException) {
    AppLog.info("acquireAccess exception: ${e}")
}
```

### static func releaseAccess()

```cangjie
public static func releaseAccess(): ReleaseStatus
```

**功能：** 以同步方法取消锁屏下应用敏感数据访问权限。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[ReleaseStatus](#enum-releasestatus)|锁屏下敏感数据访问权限释放的状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[锁屏敏感数据管理错误码](../../errorcodes/cj-errorcode-screen_lock_file_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID  | 错误信息 |
  | :------- | :---------------------------------- |
  | 801 | The specified SystemCapability name was not found. |
  | 29300002 | The system ability work abnormally. |
  | 29300003 | The application is not enabled the data protection under lock screen. |
  | 29300005 | File access was not acquired. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.base.*

try {
    let status = ScreenLockFileManager.releaseAccess()
    match (status) {
        case RELEASE_DENIED => AppLog.info("RELEASE_DENIED")
        case RELEASE_GRANTED => AppLog.info("RELEASE_GRANTED")
        case _ => throw IllegalArgumentException("The type is not supported.")
    }
    } catch (e: BusinessException ) {
        AppLog.info("releaseAccess exception: ${e}")
    }
```