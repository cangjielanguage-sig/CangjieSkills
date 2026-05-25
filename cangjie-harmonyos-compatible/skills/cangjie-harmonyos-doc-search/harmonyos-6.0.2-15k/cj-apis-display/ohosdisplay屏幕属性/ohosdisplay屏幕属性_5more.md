# ohos.display（屏幕属性）

屏幕属性提供管理显示设备的一些基础能力，包括获取默认显示设备的信息，获取所有显示设备的信息以及监听显示设备的插拔行为。

## 导入模块

```cangjie
import ohos.display.*
```

## func getAllDisplayPhysicalResolution()

```cangjie
public func getAllDisplayPhysicalResolution(): Array<DisplayPhysicalResolution>
```

**功能：** 获取当前折叠设备的显示模式以及对应的物理屏幕分辨率信息对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[DisplayPhysicalResolution](#class-displayphysicalresolution)>|返回当前所有的DisplayPhysicalResolution对象。|

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |120|ERROR: Failed to get all display physical resolution.|

**示例:**

```cangjie
import ohos.display.*

func getAllDisplayPhysicalResolutionExample() {
    try {
        let displayPhysicalResolutions: Array<DisplayPhysicalResolution> = getAllDisplayPhysicalResolution()
        AppLog.info("displayPhysicalResolutions size: ${displayPhysicalResolutions.size}")
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```

## func getAllDisplays()

```cangjie
public func getAllDisplays(): Array<Display>
```

**功能：** 获取当前所有的Display对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array&lt;[Display](#class-display)&gt;|返回当前所有的display对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400003|ERROR: Failed to get all displays.|

**示例:**

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

**功能：** 在当前显示模式下获取折叠折痕区域。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[FoldCreaseRegion](#class-foldcreaseregion)|FoldCreaseRegion对象，返回设备在当前显示模式下的折叠折痕区域。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400003|ERROR: Failed to get current fold crease region.|

**示例:**

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