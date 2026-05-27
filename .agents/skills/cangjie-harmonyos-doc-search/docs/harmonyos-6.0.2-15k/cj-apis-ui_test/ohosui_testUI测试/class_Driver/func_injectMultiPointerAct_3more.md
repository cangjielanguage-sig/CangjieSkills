### func injectMultiPointerAction(PointerMatrix, Int32)

```cangjie
public func injectMultiPointerAction(pointers: PointerMatrix, speed!: Int32 = 600): Bool
```

**功能：** 向设备注入多指操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pointers|[PointerMatrix](#class-pointermatrix)|是|-|滑动轨迹，包括操作手指个数和滑动坐标序列。|
|speed|Int32|否|600| **命名参数。** 滑动速率，范围：200-15000，不在范围内设为默认值为600，单位：像素点/秒。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回操作是否成功完成。成功返回true，否则返回false。|

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
let pointers: PointerMatrix = PointerMatrix.create(2, 3)
pointers.setPoint(0, 0, Point(230, 480))
pointers.setPoint(0, 1, Point(250, 380))
pointers.setPoint(0, 2, Point(270, 280))
pointers.setPoint(1, 0, Point(230, 680))
pointers.setPoint(1, 1, Point(240, 580))
pointers.setPoint(1, 2, Point(250, 480))
driver.injectMultiPointerAction(pointers)
```

### func inputText(Point, String)

```cangjie
public func inputText(p: Point, text: String): Unit
```

**功能：** 在指定坐标点输入文本。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|p|[Point](#class-point)|是|-|输入文本的坐标点。|
|text|String|是|-|输入的文本信息。|

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
let text: UIComponent = driver.findComponent(On().onType("TextInput"))
let point = text.getBoundsCenter()
driver.inputText(point, "123")
```

### func longClick(Int32, Int32)

```cangjie
public func longClick(x: Int32, y: Int32): Unit
```

**功能：** [Driver](#class-driver)对象执行目标坐标点的长按操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int32|是|-|以Int32的形式传入目标点的横坐标信息。|
|y|Int32|是|-|以Int32的形式传入目标点的纵坐标信息。|

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
driver.longClick(100, 100)
```