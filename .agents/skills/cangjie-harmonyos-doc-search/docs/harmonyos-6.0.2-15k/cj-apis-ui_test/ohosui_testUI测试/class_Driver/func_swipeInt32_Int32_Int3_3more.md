### func swipe(Int32, Int32, Int32, Int32, Int32)

```cangjie
public func swipe(startx: Int32, starty: Int32, endx: Int32, endy: Int32, speed!: Int32 = 600): Unit
```

**功能：** [Driver](#class-driver)对象执行从起始坐标到目标坐标的滑动操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startx|Int32|是|-|以Int32的形式传入起始点的横坐标信息。|
|starty|Int32|是|-|以Int32的形式传入起始点的纵坐标信息。|
|endx|Int32|是|-|以Int32的形式传入目的点的横坐标信息。|
|endy|Int32|是|-|以Int32的形式传入目的点的纵坐标信息。|
|speed|Int32|否|600| **命名参数。** 滑动速率，范围：200-15000，不在范围内设为默认值为600，单位：像素点/秒。|

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
driver.swipe(100, 100, 200, 200, speed: 600)
```

### func triggerCombineKeys(Int32, Int32, Option\<Int32>)

```cangjie
public func triggerCombineKeys(key0: Int32, key1: Int32, key2!: Option<Int32> = None): Unit
```

**功能：** [Driver](#class-driver)对象通过给定的key值，找到对应组合键并点击。例如，Key值为(2072, 2019)时，[Driver](#class-driver)对象找到key值对应的组合键并点击，如CTRL+C。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key0|Int32|是|-|指定的第一个key值。|
|key1|Int32|是|-|指定的第二个key值。|
|key2|Option\<Int32>|否|None| **命名参数。** 指定的第三个key值。|

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
driver.triggerCombineKeys(2072, 2047, key2: 2035)
```

### func triggerKey(Int32)

```cangjie
public func triggerKey(keyCode: Int32): Unit
```

**功能：** [Driver](#class-driver)对象通过传入 key 值模拟点击对应按键。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keyCode|Int32|是|-|指定的key值。|

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
driver.triggerKey(123)
```