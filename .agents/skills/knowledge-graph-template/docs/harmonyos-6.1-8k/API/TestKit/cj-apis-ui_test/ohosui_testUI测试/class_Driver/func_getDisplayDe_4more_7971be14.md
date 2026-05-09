### func getDisplayDensity()

```cangjie
public func getDisplayDensity(): Point
```

**功能：** 获取当前设备屏幕的分辨率。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Point](#class-point)|返回Point对象，当前设备屏幕的分辨率为Point.x*Point.y。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let density = driver.getDisplayDensity()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getDisplayRotation()

```cangjie
public func getDisplayRotation(): DisplayRotation
```

**功能：** 获取当前设备的屏幕显示方向。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[DisplayRotation](#enum-displayrotation)|返回当前设备的显示方向。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let rotation: DisplayRotation = driver.getDisplayRotation()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getDisplaySize()

```cangjie
public func getDisplaySize(): Point
```

**功能：** 获取当前设备的屏幕大小。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Point](#class-point)|返回Point对象，当前设备屏幕的大小为Point.x * Point.y。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let size = driver.getDisplaySize()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func injectMultiPointerAction(PointerMatrix, Int32)

```cangjie
public func injectMultiPointerAction(pointers: PointerMatrix, speed!: Int32 = 600): Bool
```

**功能：** 向设备注入多指操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pointers|[PointerMatrix](#class-pointermatrix)|是|-|滑动轨迹，包括操作手指个数和滑动坐标序列。|
|speed|Int32|否|600|**命名参数。** 滑动速率，取值范围为200-40000的整数，默认值为600，不在范围内设为默认值为600，单位：px/s。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回操作是否成功完成。true：完成，false：未完成。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.ui_test.Point as PT
import ohos.ui_test.Driver
import ohos.ui_test.PointerMatrix
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let pointers: PointerMatrix = PointerMatrix.create(2, 3)
    pointers.setPoint(0, 0, PT(230, 480))
    pointers.setPoint(0, 1, PT(250, 380))
    pointers.setPoint(0, 2, PT(270, 280))
    pointers.setPoint(1, 0, PT(230, 680))
    pointers.setPoint(1, 1, PT(240, 580))
    pointers.setPoint(1, 2, PT(250, 480))
    let result = driver.injectMultiPointerAction(pointers)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```