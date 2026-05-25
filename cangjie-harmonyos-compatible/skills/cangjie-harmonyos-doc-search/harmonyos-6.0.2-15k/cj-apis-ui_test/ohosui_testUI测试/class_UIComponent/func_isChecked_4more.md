### func isChecked()

```cangjie
public func isChecked(): Bool
```

**功能：** 获取控件对象被勾选状态。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|控件对象被勾选状态，true：被勾选，false：未被勾选。|

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
import kit.PerformanceAnalysisKit.*

let driver: Driver = Driver.create()
let checkbox: UIComponent = driver.findComponent(On().onType("Checkbox"))
if (checkbox.isChecked()) {
    Hilog.info(0, "", "This checkBox is checked")
} else {
    Hilog.info(0, "", "This checkBox is not checked")
}
```

### func isClickable()

```cangjie
public func isClickable(): Bool
```

**功能：** 判断控件对象是否可点击。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|控件对象是否可点击，true：可点击，false：不可点击。|

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
import kit.PerformanceAnalysisKit.*

let driver: Driver = Driver.create()
let button: UIComponent = driver.findComponent(On().onType("Button"))
if (button.isClickable()) {
    Hilog.info(0, "", "This button can be Clicked")
} else {
    Hilog.info(0, "", "This button can not be Clicked")
}
```

### func isEnabled()

```cangjie
public func isEnabled(): Bool
```

**功能：** 获取控件使能状态。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|控件使能状态，true：使能，false：未使能。|

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
import kit.PerformanceAnalysisKit.*

let driver: Driver = Driver.create()
let button: UIComponent = driver.findComponent(On().onType("Button"))
if (button.isEnabled()) {
    Hilog.info(0, "", "This button can be operated")
} else {
    Hilog.info(0, "", "This button can not be operated")
}
```

### func isFocused()

```cangjie
public func isFocused(): Bool
```

**功能：** 判断控件对象获焦状态。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|控件对象获焦状态，true：获焦，false：未获焦。|

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
import kit.PerformanceAnalysisKit.*

let driver: Driver = Driver.create()
let button: UIComponent = driver.findComponent(On().onType("Button"))
if (button.isFocused()) {
    Hilog.info(0, "", "This button is focused")
} else {
    Hilog.info(0, "", "This button is not focused")
}
```