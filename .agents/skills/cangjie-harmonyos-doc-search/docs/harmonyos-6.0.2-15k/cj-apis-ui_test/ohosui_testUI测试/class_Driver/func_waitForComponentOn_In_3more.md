### func waitForComponent(On, Int32)

```cangjie
public func waitForComponent(on: On, time: Int32): UIComponent
```

**功能：** 在[Driver](#class-driver)对象中，在用户给定的时间内，持续查找满足控件属性要求的目标控件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|目标控件的属性要求。|
|time|Int32|是|-|查找目标控件的持续时间。单位ms。|

**返回值：**

|类型|说明|
|:----|:----|
|[UIComponent](#class-uicomponent)|找到的控件对象。|

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
let button: UIComponent = driver.waitForComponent(On().text("next page"), 500)
```

### func waitForIdle(Int32, Int32)

```cangjie
public func waitForIdle(idleTime: Int32, timeout: Int32): Bool
```

**功能：** 判断当前界面的所有控件是否已经空闲。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|idleTime|Int32|是|-|空闲时间的阈值。在这个时间段控件不发生变化，视为该控件空闲，单位：毫秒。|
|timeout|Int32|是|-|等待空闲的最大时间，单位：毫秒。|

**返回值：**

| 类型              | 说明                                                |
| :----------------- | :--------------------------------------------------- |
| Bool | 返回当前界面的所有控件是否已经空闲。 |

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
let idled = driver.waitForIdle(4000, 5000)
```

### func wakeUpDisplay()

```cangjie
public func wakeUpDisplay(): Unit
```

**功能：** 唤醒当前设备即设备亮屏。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

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
driver.wakeUpDisplay()
```