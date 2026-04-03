# ohos.display（屏幕属性）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

提供屏幕属性相关功能。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func getAllDisplays()

```cangjie
public func getAllDisplays(): Array<Display>
```

**功能：** 获取所有显示屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Display](#class-display)>|返回所有显示屏的结果。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1400001|Invalid display or screen.|
  |1400003|This display manager service works abnormally.|

**示例：**

<!-- code_check_manual -->

```cangjie
import ohos.display.*

func getAllDisplaysExample() {
    try {
        let displayClass: Array<Display> = getAllDisplays()
        if (displayClass.size > 0) {
            println(displayClass[0].name)
        }
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```

## func getCurrentFoldCreaseRegion()

```cangjie
public func getCurrentFoldCreaseRegion(): FoldCreaseRegion
```

**功能：** 获取当前显示模式下的折叠 crease 区域。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[FoldCreaseRegion](#class-foldcreaseregion)|返回当前显示模式下的折叠 crease 区域。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1400003|This display manager service works abnormally.|

**示例：**

<!-- code_check_manual -->

```cangjie
import ohos.display.*
func getCurrentFoldCreaseRegionExample() {
    try {
        let region = getCurrentFoldCreaseRegion()
        println(region.displayId)
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```

## func getDefaultDisplaySync()

```cangjie
public func getDefaultDisplaySync(): Display
```

**功能：** 获取默认显示屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Display](#class-display)|返回显示屏的结果。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1400001|Invalid display or screen.|
  |1400003|This display manager service works abnormally.|

**示例：**

<!-- code_check_manual -->

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

**功能：** 获取折叠设备的显示模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[FoldDisplayMode](#enum-folddisplaymode)|返回折叠设备的显示模式。|

## func getFoldStatus()

```cangjie
public func getFoldStatus(): FoldStatus
```

**功能：** 获取折叠设备的当前折叠状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[FoldStatus](#enum-foldstatus)|返回设备的折叠状态。|

## func isFoldable()

```cangjie
public func isFoldable(): Bool
```

**功能：** 检查设备是否可折叠。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true表示设备可折叠。|