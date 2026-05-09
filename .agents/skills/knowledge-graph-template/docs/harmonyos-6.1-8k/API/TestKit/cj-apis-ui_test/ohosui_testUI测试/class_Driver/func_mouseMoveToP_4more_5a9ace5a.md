### func mouseMoveTo(Point)

```cangjie
public func mouseMoveTo(p: Point): Unit
```

**功能：** 将鼠标光标移到目标点。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|p|[Point](#class-point)|是|-|目标点的坐标。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.ui_test.Point as PT
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.mouseMoveTo(PT(248, 194))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func mouseMoveWithTrack(Point, Point, Int32)

```cangjie
public func mouseMoveWithTrack(from: Point, to: Point, speed!: Int32 = 600): Unit
```

**功能：** 鼠标从起始点坐标滑向终点坐标。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|from|[Point](#class-point)|是|-|起始点坐标。|
|to|[Point](#class-point)|是|-|终点坐标。|
|speed|Int32|否|600|**命名参数。** 滑动速率，取值范围为200-40000的整数，默认值为600，不在范围内设为默认值，单位：px/s。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.ui_test.Point as PT
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.mouseMoveWithTrack(PT(100, 100), PT(200, 200))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func mouseScroll(Point, Bool, Int32, Int32, Int32, Int32)

```cangjie
public func mouseScroll(p: Point, down: Bool, d: Int32, key1!: Int32 = 0, key2!: Int32 = 0, speed!: Int32 = 20): Unit
```

**功能：** 在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键并且指定滑动速度。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|p|[Point](#class-point)|是|-|鼠标点击的坐标。|
|down|Bool|是|-|滚轮滑动方向是否向下。true表示向下滑动。false表示向上滚动。|
|d|Int32|是|-|鼠标滚轮滚动的格数，取值大于等于0的整数，每格对应目标点位移120px。|
|key1|Int32|否|0|**命名参数。** 指定的第一个key值，取值大于等于0的整数，默认值为0。|
|key2|Int32|否|0|**命名参数。** 指定的第二个key值，取值大于等于0的整数，默认值为0。|
|speed|Int32|否|20|**命名参数。** 鼠标滚轮滚动的速度，范围：1-500的整数，不在范围内设为默认值为20，单位：格/秒。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.ui_test.Point as PT
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.mouseScroll(PT(360, 640), true, 30, key1: 2072)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func pressBack()

```cangjie
public func pressBack(): Unit
```

**功能：** 进行点击BACK键的操作。

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
    driver.pressBack()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```