## func hasPrivateWindow(UInt32)

```cangjie
public func hasPrivateWindow(displayId: UInt32): Bool
```

**功能：** 查询指定Display对象上是否有可见的隐私窗口。可通过[setWindowPrivacyMode()](cj-apis-window.md#func-setwindowprivacymodebool)接口设置隐私窗口。隐私窗口内容将无法被截屏或录屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|UInt32|是|-|显示设备的id，该参数仅支持整数输入。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|查询的Display对象上是否有可见的隐私窗口。<br>true表示此Display对象上有可见的隐私窗口，false表示此Display对象上没有可见的隐私窗口。</br> |

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400003|This display manager service works abnormally.|

**示例:**

```cangjie
import ohos.display.*

func hasPrivateWindowExample() {
    try {
        let displayClass = getDefaultDisplaySync()
        var ret: Bool = true
        try {
            ret = hasPrivateWindow(displayClass.id)
        } catch (exception: Exception) {
            AppLog.error(exception.toString())
        }
        if (ret) {
            AppLog.info("There has privateWindow.")
        } else {
            AppLog.info("There has no privateWindow.")
        }
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```

## func isCaptured()

```cangjie
public func isCaptured(): Bool
```

**功能：** 检查设备是否正在截屏、投屏、录屏。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|boolean值，返回当前设备是否有截屏、投屏或者录屏。true表示有截屏、投屏、录屏，否则返回false。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400003|This display manager service works abnormally.|

**示例:**

```cangjie
import ohos.display.*

func isCapturedExample() {
    try {
        var ret: Bool = false
        try {
            ret = isCaptured()
        } catch (exception: Exception) {
            AppLog.error(exception.toString())
        }
        if (ret) {
            AppLog.info("The device is foldable.")
        } else {
            AppLog.info("The device is not foldable.")
        }
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```

## func isFoldable()

```cangjie
public func isFoldable(): Bool
```

**功能：** 检查设备是否可折叠。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|Bool对象，返回当前设备是否可折叠的结果。true表示可折叠，false表示不可折叠。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400003|This display manager service works abnormally.|

**示例:**

```cangjie
import ohos.display.*

func isFoldableExample() {
    try {
        let displayClass = getDefaultDisplaySync()
        var ret: Bool = false
        try {
            ret = isFoldable()
        } catch (exception: Exception) {
            AppLog.error(exception.toString())
        }
        if (ret) {
            AppLog.info("The device is foldable.")
        } else {
            AppLog.info("The device is not foldable.")
        }
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```