### func delayMs(Int32)

```cangjie
public func delayMs(duration: Int32): Unit
```

**功能：** 在给定的时间内延时。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|Int32|是|-|给定的时间，单位：ms，取值范围：大于等于0的整数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.delayMs(1000)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func doubleClick(Int32, Int32)

```cangjie
public func doubleClick(x: Int32, y: Int32): Unit
```

**功能：** 在目标坐标点双击。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int32|是|-|以Int32的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。|
|y|Int32|是|-|以Int32的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.doubleClick(100, 100)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func drag(Int32, Int32, Int32, Int32, Int32)

```cangjie
public func drag(
    startx: Int32,
    starty: Int32,
    endx: Int32,
    endy: Int32,
    speed!: Int32 = 600
): Unit
```

**功能：** 从起始坐标点拖拽至目的坐标点。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startx|Int32|是|-|以Int32的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。|
|starty|Int32|是|-|以Int32的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。|
|endx|Int32|是|-|以Int32的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。
|endy|Int32|是|-|以Int32的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。|
|speed|Int32|否|600|**命名参数。** 滑动速率，取值范围为200-40000的整数，默认值为600，不在范围内设为默认值为600，单位：px/s。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.drag(100, 100, 200, 200, speed: 600)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func findComponent(On)

```cangjie
public func findComponent(on: On): ?Component
```

**功能：** 根据给出的目标控件属性要求查找目标控件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|目标控件的属性要求。|

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
    let button: Option<Component> = driver.findComponent(On().text("next page"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```