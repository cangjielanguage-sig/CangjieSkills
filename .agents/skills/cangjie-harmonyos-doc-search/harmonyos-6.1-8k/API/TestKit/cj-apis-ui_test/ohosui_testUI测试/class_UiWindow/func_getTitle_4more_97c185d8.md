### func getTitle()

```cangjie
public func getTitle(): String
```

**功能：** 获取窗口的标题信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|返回窗口的标题信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let window: Option<UiWindow> = driver.findWindow(WindowFilter(active: true))
    let title: Option<String> = window?.getTitle()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getWindowMode()

```cangjie
public func getWindowMode(): WindowMode
```

**功能：** 获取窗口的窗口模式信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[WindowMode](#enum-windowmode)|返回窗口的窗口模式信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let window: Option<UiWindow> = driver.findWindow(WindowFilter(active: true))
    let mode = window?.getWindowMode()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isActive()

```cangjie
public func isActive(): Bool
```

**功能：** 判断窗口是否为用户正在交互的窗口。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回窗口对象是否为用户正在交互窗口。true：交互窗口。false：非交互窗口。|

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let window: Option<UiWindow> = driver.findWindow(WindowFilter(active: true))
    let active = window?.isActive()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isFocused()

```cangjie
public func isFocused(): Bool
```

**功能：** 判断窗口是否处于获焦状态。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回窗口对象是否获取获焦状态。true：获焦。false：未获焦。|

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let window: Option<UiWindow> = driver.findWindow(WindowFilter(active: true))
    let focused = window?.isFocused()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```