### func getWindowMode()

```cangjie
public func getWindowMode(): WindowMode
```

**功能：** 获取窗口的窗口模式信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[WindowMode](#enum-windowmode)|返回窗口的窗口模式信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000004|if the window is invisible or destroyed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let window: UiWindow = driver.findWindow(WindowFilter(active: true))
let mode = window.getWindowMode()
```

### func isActive()

```cangjie
public func isActive(): Bool
```

**功能：** 判断窗口是否为用户正在交互的窗口。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回窗口对象交互状态，true：交互窗口，false：非交互窗口。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000004|if the window is invisible or destroyed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let window: UiWindow = driver.findWindow(WindowFilter(active: true))
let active = window.isActive()
```

### func isFocused()

```cangjie
public func isFocused(): Bool
```

**功能：** 判断窗口是否处于获焦状态。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回窗口对象是否处于获焦状态，true：获焦，false：未获焦。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000004|if the window is invisible or destroyed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let window: UiWindow = driver.findWindow(WindowFilter(active: true))
let focused = window.isFocused()
```

### func maximize()

```cangjie
public func maximize(): Unit
```

**功能：** 将窗口最大化。适用于支持窗口最大化操作的窗口。

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
window.maximize()
```

### func minimize()

```cangjie
public func minimize(): Unit
```

**功能：** 将窗口最小化。适用于支持窗口最小化操作的窗口。

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
window.minimize()
```