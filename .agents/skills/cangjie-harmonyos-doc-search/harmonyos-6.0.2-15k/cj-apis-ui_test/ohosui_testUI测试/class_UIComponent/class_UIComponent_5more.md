## class UIComponent

```cangjie
public class UIComponent {}
```

**功能：** [UIComponentComponent](#class-uicomponent)类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。

需要注意：

- 要显示app页面，必须先调用[abilityDelegator](./cj-apis-ability_delegator_registry.md)的[startAbility](./cj-apis-ability_delegator_registry.md#func-startabilitywant)。
- 查找[UIComponent](#class-uicomponent)对象时，必须保证组件已经显示在页面上，且设备亮屏。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### func clearText()

```cangjie
public func clearText(): Unit
```

**功能：** 清除控件的文本信息，适用于文本框控件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000002|if the async function was not called with await.|
  |17000004|if the component is invisible or destroyed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let text: UIComponent = driver.findComponent(On().text("hello world"))
text.clearText()
```

### func click()

```cangjie
public func click(): Unit
```

**功能：** 对控件对象进行点击操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000002|if the async function was not called with await.|
  |17000004|if the component is invisible or destroyed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let button: UIComponent = driver.findComponent(On().onType("Button"))
button.click()
```

### func doubleClick()

```cangjie
public func doubleClick(): Unit
```

**功能：** 对控件对象进行双击操作。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000002|if the async function was not called with await.|
  |17000004|if the component is invisible or destroyed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let button: UIComponent = driver.findComponent(On().onType("Button"))
button.doubleClick()
```

### func dragTo(UIComponent)

```cangjie
public func dragTo(target: UIComponent): Unit
```

**功能：** 将控件拖拽至目标控件处。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[UIComponent](#class-uicomponent)|是|-|目标控件。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[uitest错误码](../../errorcodes/cj-errorcode-uitest.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17000002|if the async function was not called with await.|
  |17000004|if the component is invisible or destroyed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let driver: Driver = Driver.create()
let button: UIComponent = driver.findComponent(On().onType("Button"))
let text: UIComponent = driver.findComponent(On().text("hello world"))
button.dragTo(text)
```