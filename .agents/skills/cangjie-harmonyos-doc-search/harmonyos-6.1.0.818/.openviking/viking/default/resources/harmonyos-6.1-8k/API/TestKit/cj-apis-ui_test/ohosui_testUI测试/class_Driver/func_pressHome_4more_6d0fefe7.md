### func pressHome()

```cangjie
public func pressHome(): Unit
```

**功能：** 设备注入返回桌面操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.pressHome()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func screenCap(String)

```cangjie
public func screenCap(savePath: String): Bool
```

**功能：** 捕获当前屏幕，并保存为PNG格式的图片至给出的保存路径中。适用于支持截屏的场景。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|savePath|String|是|-|文件保存路径。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回截图操作是否成功完成。true：完成，false：未完成。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let result = driver.screenCap("/data/storage/el2/base/cache/1.png")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func screenCapture(String, Rect)

```cangjie
public func screenCapture(savePath: String, rect!: Rect = Rect(0,0,0,0)): Bool
```

**功能：** 捕获当前屏幕的指定区域，并保存为PNG格式的图片至给出的保存路径中。适用于支持截屏的场景。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|savePath|String|是|-|文件保存路径。|
|rect|[Rect](#class-rect)|否|Rect(0, 0, 0, 0)|**命名参数。** 截图区域，默认为全屏。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回截图操作是否成功完成。true：成功完成，false：未成功完成。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let result = driver.screenCapture("/data/storage/el2/base/cache/1.png", rect: Rect(0, 0, 100, 100))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func setDisplayRotation(DisplayRotation)

```cangjie
public func setDisplayRotation(rotation: DisplayRotation): Unit
```

**功能：** 将当前场景的显示方向设置为指定的显示方向。适用于可旋转的应用场景。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotation|[DisplayRotation](#enum-displayrotation)|是|-|设备的显示方向。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.setDisplayRotation(DisplayRotation.Rotation180)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```