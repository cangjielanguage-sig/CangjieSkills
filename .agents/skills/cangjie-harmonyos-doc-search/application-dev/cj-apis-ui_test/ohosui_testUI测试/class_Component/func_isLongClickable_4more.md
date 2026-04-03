### func isLongClickable()

```cangjie
public func isLongClickable(): Bool
```

**功能：** 获取控件对象可长按点击属性。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回控件对象是否可长按点击。true：可长按点击。false：不可长按点击。|

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
    let c1: Bool = button.isLongClickable()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isScrollable()

```cangjie
public func isScrollable(): Bool
```

**功能：** 获取控件对象可滑动属性。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回控件对象是否可滑动。true：可滑动。false：不可滑动。|

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
    let s: Bool = button.isScrollable()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isSelected()

```cangjie
public func isSelected(): Bool
```

**功能：** 获取控件对象被选中状态。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回控件对象被选中状态。true：被选中。false：未被选中。|

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
    let s1: Bool = button.isSelected()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func longClick()

```cangjie
public func longClick(): Unit
```

**功能：** 在目标坐标点长按。

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
    button.longClick()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```