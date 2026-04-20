### func inputText(Point, String)

```cangjie
public func inputText(p: Point, text: String): Unit
```

**功能：** 在指定坐标点输入文本，不清空组件内原有文本，直接在坐标处追加输入。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|p|[Point](#class-point)|是|-|输入文本的坐标点。|
|text|String|是|-|输入的文本信息，当前支持英文、中文和特殊字符。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

let driver: Driver = Driver.create()
try {
    let text: Component = driver.findComponent(On().onType("TextInput")).getOrThrow()
    let point = text.getBoundsCenter()
    driver.inputText(point, "123")
} catch (e: BusinessException) {
    Hilog.error(0, "UITest", "The component `TextInput` does not exist")
}
```

### func longClick(Int32, Int32)

```cangjie
public func longClick(x: Int32, y: Int32): Unit
```

**功能：** 在目标坐标点长按。

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
    driver.longClick(100, 100)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func mouseClick(Point, MouseButton, Int32, Int32)

```cangjie
public func mouseClick(p: Point, btnId: MouseButton, key1!: Int32 = 0, key2!: Int32 = 0): Unit
```

**功能：** 在指定坐标点注入鼠标点击动作，支持同时按下对应键盘组合键。例如，Key值为2072时，按下Ctrl并进行鼠标点击动作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|p|[Point](#class-point)|是|-|鼠标点击的坐标。|
|btnId|[MouseButton](#enum-mousebutton)|是|-|按下的鼠标按键。|
|key1|Int32|否|0|**命名参数。** 指定的第一个key值，取值大于等于0的整数，默认值为0。|
|key2|Int32|否|0|**命名参数。** 指定的第二个key值，取值大于等于0的整数，默认值为0。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.ui_test.Point as PT
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    driver.mouseClick(PT(248, 194), MouseButton.MouseButtonLeft, key1: 2072)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```