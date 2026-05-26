### func mouseClick(Point, MouseButton, Option\<Int32>, Option\<Int32>)

```cangjie
public func mouseClick(p: Point, btnId: MouseButton, key1!: Option<Int32> = None, key2!: Option<Int32> = None): Unit
```

**功能：** 在指定坐标点注入鼠标点击动作，支持同时按下对应键盘组合键。例如，Key值为2072时，按下CTRL并进行鼠标点击动作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|p|[Point](#class-point)|是|-|鼠标点击的坐标。|
|btnId|[MouseButton](#enum-mousebutton)|是|-|按下的鼠标按钮。|
|key1|Option\<Int32>|否|None| **命名参数。** 指定的第一个key值。|
|key2|Option\<Int32>|否|None| **命名参数。** 指定的第二个key值。|

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
driver.mouseClick(Point(248, 194), MouseButton.MOUSE_BUTTON_LEFT, key1: 2072)
```

### func mouseDoubleClick(Point, MouseButton, Option\<Int32>, Option\<Int32>)

```cangjie
public func mouseDoubleClick(p: Point, btnId: MouseButton, key1!: Option<Int32> = None, key2!: Option<Int32> = None): Unit
```

**功能：** 在指定坐标点注入鼠标双击动作，支持同时按下对应键盘组合键。例如，Key值为2072时，按下CTRL并进行鼠标双击动作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|p|[Point](#class-point)|是|-|鼠标双击的坐标。|
|btnId|[MouseButton](#enum-mousebutton)|是|-|按下的鼠标按钮。|
|key1|Option\<Int32>|否|None| **命名参数。** 指定的第一个key值。|
|key2|Option\<Int32>|否|None| **命名参数。** 指定的第二个key值。|

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
driver.mouseDoubleClick(Point(248, 194), MouseButton.MOUSE_BUTTON_LEFT, key1: 2072)
```

### func mouseDrag(Point, Point, Int32)

```cangjie
public func mouseDrag(fromP: Point, to: Point, speed!: Int32 = 600): Unit
```

**功能：** 鼠标按住左键从起始点拖拽至终点。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fromP|[Point](#class-point)|是|-|起始点坐标。|
|to|[Point](#class-point)|是|-|终点坐标。|
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
driver.mouseDrag(Point(100, 100), Point(200, 200))
```