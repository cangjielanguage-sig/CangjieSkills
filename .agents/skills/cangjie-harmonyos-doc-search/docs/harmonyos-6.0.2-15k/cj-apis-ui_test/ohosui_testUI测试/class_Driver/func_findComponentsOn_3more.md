### func findComponents(On)

```cangjie
public func findComponents(on: On): Array<UIComponent>
```

**功能：** 在[Driver](#class-driver)对象中，根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|目标控件的属性要求。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[UIComponent](#class-uicomponent)>|目标控件的属性要求。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000002|if the async function was not called with await.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let buttonList: Array<UIComponent> = driver.findComponents(On().text("next page"))
```

### func findWindow(WindowFilter)

```cangjie
public func findWindow(filter: WindowFilter): UiWindow
```

**功能：** 通过指定窗口的属性来查找目标窗口。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filter|[WindowFilter](#class-windowfilter)|是|-|目标窗口的属性。|

**返回值：**

|类型|说明|
|:----|:----|
|[UiWindow](#class-uiwindow)|找到的目标窗口对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000002|if the async function was not called with await.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let window: UiWindow = driver.findWindow(WindowFilter(active: true))
```

### func fling(Point, Point, Int32, Int32)

```cangjie
public func fling(fromP: Point, to: Point, stepLen: Int32, speed: Int32): Unit
```

**功能：** 指定方向和速度，模拟手指滑动后脱离屏幕的快速滑动操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fromP|[Point](#class-point)|是|-|手指接触屏幕的起始点坐标。|
|to|[Point](#class-point)|是|-|手指离开屏幕时的坐标点。|
|stepLen|Int32|是|-|间隔距离，单位：像素点。|
|speed|Int32|是|-|滑动速率，范围：200-40000，不在范围内设为默认值为600，单位：像素点/秒。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000002|if the async function was not called with await.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
driver.fling(Point(500, 480), Point(450, 480), 5, 600)
```