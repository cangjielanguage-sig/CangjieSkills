### func waitForComponent(On, Int32)

```cangjie
public func waitForComponent(on: On, time: Int32): ?Component
```

**功能：** 在用户给定的时间内，持续查找满足控件属性要求的目标控件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|目标控件的属性要求。|
|time|Int32|是|-|查找目标控件的持续时间。单位ms，取值范围：大于等于0的整数。|

**返回值：**

|类型|说明|
|:----|:----|
|?[Component](#class-component)|返回控件对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let button: Option<Component> = driver.waitForComponent(On().text("next page"), 500)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func waitForIdle(Int32, Int32)

```cangjie
public func waitForIdle(idleTime: Int32, timeout: Int32): Bool
```

**功能：** 判断当前界面的所有控件是否已经空闲。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|idleTime|Int32|是|-|空闲时间的阈值。在这个时间段控件不发生变化，视为该控件空闲，单位：毫秒，取值范围：大于等于0的整数。|
|timeout|Int32|是|-|等待空闲的最大时间，单位：毫秒，取值范围：大于等于0的整数。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回当前界面的所有控件是否已经空闲。true：已经空闲，false：不空闲。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let idled = driver.waitForIdle(4000, 5000)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func wakeUpDisplay()

```cangjie
public func wakeUpDisplay(): Unit
```

**功能：** 唤醒当前设备即设备亮屏。

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
    driver.wakeUpDisplay()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```