### func isLongClickable()

```cangjie
public func isLongClickable(): Bool
```

**功能：** 判断控件对象是否可长按点击。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|控件对象是否可长按点击，true：可长按点击，false：不可长按点击。|

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
if (button.isLongClickable()) {
    Hilog.info(0, "", "This button can be longClick")
} else {
    Hilog.info(0, "", "This button can not be longClick")
}
```

### func isScrollable()

```cangjie
public func isScrollable(): Bool
```

**功能：** 判断控件对象是否可滑动。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|控件对象是否可滑动，true：可滑动，false：不可滑动。|

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
let scrollBar: UIComponent = driver.findComponent(On().scrollable())
if (scrollBar.isScrollable()) {
    Hilog.info(0, "", "This scrollBar can be operated")
} else {
    Hilog.info(0, "", "This scrollBar can not be operated")
}
```

### func isSelected()

```cangjie
public func isSelected(): Bool
```

**功能：** 获取控件对象被选中状态。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|控件对象被选中状态，true：被选中，false：未被选中。|

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
if (button.isSelected()) {
    Hilog.info(0, "", "This button is selected")
} else {
    Hilog.info(0, "", "This button is not selected")
}
```

### func longClick()

```cangjie
public func longClick(): Unit
```

**功能：** 对控件对象进行长按操作。

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
button.longClick()
```