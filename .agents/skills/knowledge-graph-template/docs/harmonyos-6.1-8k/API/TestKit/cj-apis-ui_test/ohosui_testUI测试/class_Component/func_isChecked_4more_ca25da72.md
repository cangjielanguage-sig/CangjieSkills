### func isChecked()

```cangjie
public func isChecked(): Bool
```

**功能：** 获取控件对象被勾选状态。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回控件对象被勾选状态。true：被勾选。false：未被勾选。|

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
    let c2: Bool = button.isChecked()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isClickable()

```cangjie
public func isClickable(): Bool
```

**功能：** 获取控件对象可点击属性。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回控件对象是否可点击。true：可点击。false：不可点击。|

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
    let c: Bool = button.isClickable()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isEnabled()

```cangjie
public func isEnabled(): Bool
```

**功能：** 获取控件使能状态。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回控件使能状态。true：使能。false：未使能。|

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
    let e: Bool = button.isEnabled()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isFocused()

```cangjie
public func isFocused(): Bool
```

**功能：** 判断控件对象获焦状态。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回控件对象获焦状态。true：获焦。false：未获焦。|

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
    let f: Bool = button.isFocused()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```