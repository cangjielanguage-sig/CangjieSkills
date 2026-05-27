## class Driver

```cangjie
public class Driver {}
```

**功能：** [Driver](#class-driver)类为uitest测试框架的总入口，提供控件匹配、查找、按键注入，坐标点击或滑动，截图等能力。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### static func create()

```cangjie
public static func create(): Driver
```

**功能：** 静态方法，构造一个[Driver](#class-driver)对象，并返回该对象。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[Driver](#class-driver)|返回构造的[Driver](#class-driver)对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000001|if the test framework failed to initialize.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
```

### func assertComponentExist(On)

```cangjie
public func assertComponentExist(on: On): Unit
```

**功能：** 断言API，用于断言当前界面是否存在满足给出的目标属性的控件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|目标控件的属性要求。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000002|if the async function was not called with await.|
  |17000003|if the assertion failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
driver.assertComponentExist(On().text("next page"))
```

### func click(Int32, Int32)

```cangjie
public func click(x: Int32, y: Int32): Unit
```

**功能：** [Driver](#class-driver)对象执行目标坐标点的点击操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int32|是|-|以Int32的形式传入目标点的横坐标信息。|
|y|Int32|是|-|以Int32的形式传入目标点的纵坐标信息。|

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
driver.click(100, 100)
```

### func createUIEventObserver()

```cangjie
public func createUIEventObserver(): UIEventObserver
```

**功能：** 创建一个UI事件监听器。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[UIEventObserver](#class-uieventobserver)|返回找到的目标窗口对象。|

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
let observer: UIEventObserver = driver.createUIEventObserver()
```