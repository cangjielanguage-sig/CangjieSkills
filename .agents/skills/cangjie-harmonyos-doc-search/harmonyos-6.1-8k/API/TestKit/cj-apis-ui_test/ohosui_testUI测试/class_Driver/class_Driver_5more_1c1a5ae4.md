## class Driver

```cangjie
public class Driver {}
```

**功能：** Driver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### static func create()

```cangjie
public static func create(): Driver
```

**功能：** 静态方法，构造一个[Driver](#class-driver)对象，并返回该对象。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Driver](#class-driver)|返回构造的[Driver](#class-driver)对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000001 | Initialization failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func assertComponentExist(On)

```cangjie
public func assertComponentExist(on: On): Unit
```

**功能：** 断言API，用于断言当前界面是否存在满足给出的目标属性的控件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|目标控件的属性要求。|

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000003 | Assertion failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import kit.TestKit.*
import ohos.business_exception.BusinessException

let driver: Driver = Driver.create()
try {
    driver.assertComponentExist(On().text("next page"))
} catch (e: BusinessException) {
    Hilog.error(0, "UITest", "The component `text(\"next page\")` does not exist")
}
```

### func click(Int32, Int32)

```cangjie
public func click(x: Int32, y: Int32): Unit
```

**功能：** 在目标坐标点单击。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int32|是|-|以Int32的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。|
|y|Int32|是|-|以Int32的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.click(100, 100)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func createUiEventObserver()

```cangjie
public func createUiEventObserver(): UiEventObserver
```

**功能：** 创建一个UI事件监听器。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[UiEventObserver](#class-uieventobserver)|返回找到的目标窗口对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let observer: UiEventObserver = driver.createUiEventObserver()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```