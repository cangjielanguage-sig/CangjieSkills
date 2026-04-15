### func setDisplayRotationEnabled(Bool)

```cangjie
public func setDisplayRotationEnabled(enabled: Bool): Unit
```

**功能：** 启用/禁用设备旋转屏幕的功能。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|能否旋转屏幕的标识，true：可以旋转，false：不可以旋转。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.setDisplayRotationEnabled(false)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func swipe(Int32, Int32, Int32, Int32, Int32)

```cangjie
public func swipe(
    startx: Int32,
    starty: Int32,
    endx: Int32,
    endy: Int32,
    speed!: Int32 = 600
): Unit
```

**功能：** 从起始坐标点滑向目的坐标点。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startx|Int32|是|-|以Int32的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。|
|starty|Int32|是|-|以Int32的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。|
|endx|Int32|是|-|以Int32的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。|
|endy|Int32|是|-|以Int32的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。|
|speed|Int32|否|600|**命名参数。** 滑动速率，取值范围为200-40000的整数，默认值为600，不在范围内设为默认值为600，单位：px/s。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.swipe(100, 100, 200, 200, speed: 600)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func triggerCombineKeys(Int32, Int32, Int32)

```cangjie
public func triggerCombineKeys(key0: Int32, key1: Int32, key2!: Int32 = 0): Unit
```

**功能：** 通过给定的key值，找到对应组合键并点击。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key0|Int32|是|-|指定的第一个key值，取值大于等于0的整数。|
|key1|Int32|是|-|指定的第二个key值，取值大于等于0的整数。|
|key2|Int32|否|0|**命名参数。** 指定的第三个key值，取值范围：大于等于0的整数。默认值为0。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.triggerCombineKeys(2072, 2047, key2: 2035)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func triggerKey(Int32)

```cangjie
public func triggerKey(keyCode: Int32): Unit
```

**功能：** 传入key值实现模拟点击对应按键的效果。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keyCode|Int32|是|-|指定的key值，取值范围：大于等于0的整数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.triggerKey(123)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```