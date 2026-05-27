### func moveTo(IntNative, IntNative)

```cangjie
public func moveTo(x: IntNative, y: IntNative): Unit
```

**功能：** 将窗口移动到目标点。适用于支持移动的窗口。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|IntNative|是|-|以IntNative的形式传入目标点的横坐标信息。|
|y|IntNative|是|-|以IntNative的形式传入目标点的纵坐标信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000004|if the window is invisible or destroyed.|
  |17000005|if the action is not supported on this window.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let window: UiWindow = driver.findWindow(WindowFilter(active: true))
window.moveTo(100, 100)
```

### func resize(IntNative, IntNative, ResizeDirection)

```cangjie
public func resize(wide: IntNative, height: IntNative, direction: ResizeDirection): Unit
```

**功能：** 根据传入的宽、高和调整方向来调整窗口的大小。适用于支持调整大小的窗口。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|wide|IntNative|是|-|以IntNative的形式传入调整后窗口的宽度。|
|height|IntNative|是|-|以IntNative的形式传入调整后窗口的高度。|
|direction|[ResizeDirection](#enum-resizedirection)|是|-|以ResizeDirection的形式传入窗口调整的方向。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000004|if the window is invisible or destroyed.|
  |17000005|if the action is not supported on this window.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let window: UiWindow = driver.findWindow(WindowFilter(active: true))
window.resize(100, 100, ResizeDirection.LEFT)
```

### func resume()

```cangjie
public func resume(): Unit
```

**功能：** 将窗口恢复到之前的窗口模式。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000004|if the window is invisible or destroyed.|
  |17000005|if the action is not supported on this window.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let window: UiWindow = driver.findWindow(WindowFilter(active: true))
window.resume()
```

### func split()

```cangjie
public func split(): Unit
```

**功能：** 将窗口模式切换成分屏模式。适用于支持切换分屏模式的窗口。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000004|if the window is invisible or destroyed.|
  |17000005|if the action is not supported on this window.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let window: UiWindow = driver.findWindow(WindowFilter(active: true))
window.split()
```