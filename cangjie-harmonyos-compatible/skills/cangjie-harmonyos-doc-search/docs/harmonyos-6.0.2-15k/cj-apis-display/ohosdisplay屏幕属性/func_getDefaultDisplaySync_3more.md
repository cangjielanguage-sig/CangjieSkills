## func getDefaultDisplaySync()

```cangjie
public func getDefaultDisplaySync(): Display
```

**功能：** 获取当前默认的Display对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[Display](#class-display)|返回默认的Display对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400001|ERROR: Failed to get default display.|
  |1400003|ERROR: Failed to get default display.|

**示例:**

```cangjie
import ohos.display.*

func getDefaultDisplaySyncExample() {
    try {
        let displayClass: Display = getDefaultDisplaySync()
        println(displayClass.name)
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```

## func getFoldDisplayMode()

```cangjie
public func getFoldDisplayMode(): FoldDisplayMode
```

**功能：** 获取可折叠设备的显示模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[FoldDisplayMode](#enum-folddisplaymode)|FoldDisplayMode对象，返回当前可折叠设备的显示模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400003|This display manager service works abnormally.|

**示例:**

```cangjie
import ohos.display.*

func getFoldDisplayModeExample() {
    try {
        let mode = getFoldDisplayMode()
        match (mode) {
            case FoldDisplayMode.FOLD_DISPLAY_MODE_UNKNOWN => AppLog.info("Unkown mode.")
            case FoldDisplayMode.FOLD_DISPLAY_MODE_FULL => AppLog.info("Full mode.")
            case FoldDisplayMode.FOLD_DISPLAY_MODE_MAIN => AppLog.info("Main mode.")
            case FoldDisplayMode.FOLD_DISPLAY_MODE_SUB => AppLog.info("Sub mode.")
            case FoldDisplayMode.FOLD_DISPLAY_MODE_COORDINATION => AppLog.info("Coordination mode.")
            case _ => throw Exception("can not get display mode.")
        }
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```

## func getFoldStatus()

```cangjie
public func getFoldStatus(): FoldStatus
```

**功能：** 获取可折叠设备的当前折叠状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[FoldStatus](#enum-foldstatus)|FoldStatus对象，返回当前可折叠设备的折叠状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400003|This display manager service works abnormally.|

**示例:**

```cangjie
import ohos.display.*

func getFoldStatusExample() {
    try {
        let status = getFoldStatus()
        match (status) {
            case FoldStatus.FOLD_STATUS_UNKNOWN => AppLog.info("Unkown status.")
            case FoldStatus.FOLD_STATUS_EXPANDED => AppLog.info("Expanded.")
            case FoldStatus.FOLD_STATUS_FOLDED => AppLog.info("Folded.")
            case FoldStatus.FOLD_STATUS_HALF_FOLDED => AppLog.info("Half folded.")
            case _ => throw Exception("can not get fold status.")
        }
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```