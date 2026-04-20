### func findComponents(On)

```cangjie
public func findComponents(on: On): ?Array<Component>
```

**功能：** 根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|目标控件的属性要求。|

**返回值：**

|类型|说明|
|:----|:----|
|?Array\<[Component](#class-component)>|返回控件对象的列表。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let buttonList: Option<Array<Component>> = driver.findComponents(On().text("next page"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func findWindow(WindowFilter)

```cangjie
public func findWindow(filter: WindowFilter): ?UiWindow
```

**功能：** 通过指定窗口的属性来查找目标窗口。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filter|[WindowFilter](#class-windowfilter)|是|-|目标窗口的属性。|

**返回值：**

|类型|说明|
|:----|:----|
|?[UiWindow](#class-uiwindow)|返回目标窗口对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let window: Option<UiWindow> = driver.findWindow(WindowFilter(active: true))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func fling(Point, Point, Int32, Int32)

```cangjie
public func fling(from: Point, to: Point, stepLen: Int32, speed: Int32): Unit
```

**功能：** 模拟手指滑动后脱离屏幕的快速滑动操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|from|[Point](#class-point)|是|-|手指接触屏幕的起始点坐标。|
|to|[Point](#class-point)|是|-|手指离开屏幕时的坐标点。|
|stepLen|Int32|是|-|间隔距离，取值大于等于0的整数，单位：px。|
|speed|Int32|是|-|滑动速率，取值范围为200-40000的整数，不在范围内设为600，单位：px/s。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.fling(UiDirection.Down, 10000)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func fling(UiDirection, Int32)

```cangjie
public func fling(direction: UiDirection, speed: Int32): Unit
```

**功能：** 指定方向和滑动速率，模拟手指滑动后脱离屏幕的快速滑动操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|direction|[UiDirection](#enum-uidirection)|是|-|进行抛滑的方向。|
|speed|Int32|是|-|滑动速率，取值范围为200-40000的整数，不在范围内设为600，单位：px/s。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.fling(UiDirection.Down, 10000)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```