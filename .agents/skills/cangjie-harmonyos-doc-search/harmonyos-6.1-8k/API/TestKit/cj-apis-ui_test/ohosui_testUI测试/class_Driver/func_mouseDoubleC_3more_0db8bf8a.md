### func mouseDoubleClick(Point, MouseButton, Int32, Int32)

```cangjie
public func mouseDoubleClick(p: Point, btnId: MouseButton, key1!: Int32 = 0, key2!: Int32 = 0): Unit
```

**功能：** 在指定坐标点注入鼠标双击动作，支持同时按下对应键盘组合键。例如，Key值为2072时，按下Ctrl并进行鼠标双击动作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|p|[Point](#class-point)|是|-|鼠标双击的坐标。|
|btnId|[MouseButton](#enum-mousebutton)|是|-|按下的鼠标按键。|
|key1|Int32|否|0|**命名参数。** 指定的第一个key值，取值大于等于0的整数，默认值0。|
|key2|Int32|否|0|**命名参数。** 指定的第二个key值，取值大于等于0的整数，默认值0。|

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
    driver.mouseDoubleClick(PT(248, 194), MouseButton.MouseButtonLeft, key1: 2072)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func mouseDrag(Point, Point, Int32)

```cangjie
public func mouseDrag(from: Point, to: Point, speed!: Int32 = 600): Unit
```

**功能：** 按住鼠标左键从起始坐标点拖拽至终点坐标点。

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
    driver.mouseDrag(PT(100, 100), PT(200, 200))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func mouseLongClick(Point, MouseButton, Int32, Int32)

```cangjie
public func mouseLongClick(p: Point, btnId: MouseButton, key1!: Int32 = 0, key2!: Int32 = 0): Unit
```

**功能：** 在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键，支持指定长按时长。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|p|[Point](#class-point)|是|-|鼠标长按的坐标。|
|btnId|[MouseButton](#enum-mousebutton)|是|-|按下的鼠标按键。|
|key1|Int32|否|0|**命名参数。** 指定的第一个key值，取值大于等于0的整数，默认值为0。|
|key2|Int32|否|0|**命名参数。** 指定的第二个key值，取值大于等于0的整数，默认值为0。|

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
    driver.mouseLongClick(PT(248, 194), MouseButton.MouseButtonLeft, key1: 2072)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```