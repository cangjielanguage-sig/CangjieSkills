## class UiWindow

```cangjie
public class UiWindow {}
```

**功能：** [UiWindow](#class-uiwindow)代表了UI界面上的一个窗口，提供获取窗口属性、拖动窗口、调整窗口大小等能力。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### func close()

```cangjie
public func close(): Unit
```

**功能：** 将窗口关闭。

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
window.close()
```

### func focus()

```cangjie
public func focus(): Unit
```

**功能：** 让窗口获焦。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

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
window.focus()
```

### func getBounds()

```cangjie
public func getBounds(): Rect
```

**功能：** 获取窗口的边框信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[Rect](#class-rect)|返回窗口的边框信息。|

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
let rect = window.getBounds()
```

### func getBundleName()

```cangjie
public func getBundleName(): String
```

**功能：** 获取窗口归属应用的包名信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回窗口归属应用的包名信息。|

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
let name: String = window.getBundleName()
```

### func getTitle()

```cangjie
public func getTitle(): String
```

**功能：** 获取窗口的标题信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回窗口的标题信息。|

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
let title: String = window.getTitle()
```