## class UiWindow

```cangjie
public class UiWindow {}
```

**功能：** [UiWindow](#class-uiwindow)代表了UI界面上的一个窗口，提供获取窗口属性、拖动窗口、调整窗口大小等能力。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### func close()

```cangjie
public func close(): Unit
```

**功能：** 将窗口关闭。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |
  | 17000005 | This operation is not supported. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let window: Option<UiWindow> = driver.findWindow(WindowFilter(active: true))
    window?.close()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func focus()

```cangjie
public func focus(): Unit
```

**功能：** 让窗口获焦。

**说明** 该接口在Tablet设备中可正常调用，在手机设备中返回17000005错误码。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

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
    window?.focus()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getBounds()

```cangjie
public func getBounds(): Rect
```

**功能：** 获取控件对象的边框信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Rect](#class-rect)|返回控件对象的边框信息。|

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
    let rect = window?.getBounds()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getBundleName()

```cangjie
public func getBundleName(): String
```

**功能：** 获取窗口归属应用的包名信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|返回窗口归属应用的包名信息。|

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
    let rect = window?.getBundleName()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```