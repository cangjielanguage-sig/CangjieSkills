## class Component

```cangjie
public class Component {}
```

**功能：** [Component](#class-component)类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### func clearText()

```cangjie
public func clearText(): Unit
```

**功能：** 清除控件的文本信息，仅针对可编辑的文本组件生效。

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
    let txt: Component = driver.findComponent(On().text("cangjie")).getOrThrow()
    txt.clearText()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func click()

```cangjie
public func click(): Unit
```

**功能：** 对控件对象进行点击操作。

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
    let button: Component = driver.findComponent(On().id("button")).getOrThrow()
    button.click()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func doubleClick()

```cangjie
public func doubleClick(): Unit
```

**功能：** 控件对象进行双击操作。

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
    let button: Component = driver.findComponent(On().id("button")).getOrThrow()
    button.doubleClick()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func dragTo(Component)

```cangjie
public func dragTo(target: Component): Unit
```

**功能：** 将控件拖拽至目标控件处。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Component](#class-component)|是|-|目标控件。|

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
    let button: Component = driver.findComponent(On().id("button")).getOrThrow()
    let drag: Component = driver.findComponent(On().text("ohos")).getOrThrow()
    button.dragTo(drag)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```