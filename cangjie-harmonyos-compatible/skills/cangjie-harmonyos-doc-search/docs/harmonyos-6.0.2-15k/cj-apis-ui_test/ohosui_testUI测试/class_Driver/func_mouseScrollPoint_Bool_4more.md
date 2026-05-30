### func mouseScroll(Point, Bool, Int32, Option\<Int32>, Option\<Int32>, Int32)

```cangjie
public func mouseScroll(p: Point, down: Bool, d: Int32, key1!: Option<Int32> = None, key2!: Option<Int32> = None,
 speed!: Int32 = 20): Unit
```

**功能：** 在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键并且指定滑动速度。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|p|[Point](#class-point)|是|-|鼠标点击的坐标。|
|down|Bool|是|-|滚轮滑动方向是否向下，true表示向下滑动，false表示向上滑动。|
|d|Int32|是|-|鼠标滚轮滑动的格数，每格对应目标点位移120个像素点。|
|key1|Option\<Int32>|否|None| **命名参数。** 指定的第一个key值。|
|key2|Option\<Int32>|否|None| **命名参数。** 指定的第二个key值。|
|speed|Int32|否|20| **命名参数。** 鼠标滚轮滑动的速度，范围：1-500，不在范围内设为默认值为20，单位：格/秒。|

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
driver.mouseScroll(Point(360, 640), true, 30, key1: 2072)
```

### func pressBack()

```cangjie
public func pressBack(): Unit
```

**功能：** [Driver](#class-driver)对象进行点击BACK键的操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

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
driver.pressBack()
```

### func pressHome()

```cangjie
public func pressHome(): Unit
```

**功能：** 设备返回到桌面。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

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
driver.pressHome()
```

### func screenCap(String)

```cangjie
public func screenCap(savePath: String): Bool
```

**功能：** [Driver](#class-driver)对象捕获当前屏幕，并将其保存为PNG格式的图片，保存至参数传入的路径中。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|savePath|String|是|-|文件保存路径。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|截图操作是否成功完成。成功完成为true，否则为false。|

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
driver.screenCap("/data/storage/el2/base/cache/1.png")
```