### func delayMs(Int32)

```cangjie
public func delayMs(delayMs: Int32): Unit
```

**功能：** [Driver](#class-driver)对象在给定的时间内延时。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|delayMs|Int32|是|-|给定的时间，单位：ms。|

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
driver.delayMs(1000)
```

### func doubleClick(Int32, Int32)

```cangjie
public func doubleClick(x: Int32, y: Int32): Unit
```

**功能：** [Driver](#class-driver) 对象执行目标坐标点的双击操作。

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
driver.doubleClick(100, 100)
```

### func drag(Int32, Int32, Int32, Int32, Int32)

```cangjie
public func drag(startx: Int32, starty: Int32, endx: Int32, endy: Int32, speed!: Int32 = 600): Unit
```

**功能：** [Driver](#class-driver)对象执行从起始坐标到目标坐标的拖拽操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startx|Int32|是|-|以Int32的形式传入起始点的横坐标信息。|
|starty|Int32|是|-|以Int32的形式传入起始点的纵坐标信息。|
|endx|Int32|是|-|以Int32的形式传入目的点的横坐标信息。|
|endy|Int32|是|-|以Int32的形式传入目的点的纵坐标信息。|
|speed|Int32|否|600| **命名参数。** 滑动速率，范围：200-15000，不在范围内设为默认值为600，单位：像素点/秒。|

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
driver.drag(100, 100, 200, 200, speed: 600)
```

### func findComponent(On)

```cangjie
public func findComponent(on: On): UIComponent
```

**功能：** 在[Driver](#class-driver)对象中，根据给出的目标控件属性要求查找目标控件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|目标控件的属性要求。|

**返回值：**

|类型|说明|
|:----|:----|
|[UIComponent](#class-uicomponent)|找到的控件对象。|

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
let button: UIComponent = driver.findComponent(On().text("next page"))
```