### func pinchIn(Float32)

```cangjie
public func pinchIn(scale: Float32): Unit
```

**功能：** 将控件按指定的比例进行捏合缩小。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scale|Float32|是|-|指定缩小的比例。|

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
let image: UIComponent = driver.findComponent(On().onType("Image"))
image.pinchIn(1.5)
```

### func pinchOut(Float32)

```cangjie
public func pinchOut(scale: Float32): Unit
```

**功能：** 将控件按指定的比例进行捏合放大。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scale|Float32|是|-|指定放大的比例。|

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
let image: UIComponent = driver.findComponent(On().onType("Image"))
image.pinchOut(1.5)
```

### func scrollSearch(On)

```cangjie
public func scrollSearch(on: On): UIComponent
```

**功能：** 在控件上滑动查找目标控件，适用支持滑动的控件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|目标控件的属性要求。|

**返回值：**

|类型|说明|
|:----|:----|
|[UIComponent](#class-uicomponent)|找到的目标控件对象。|

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
let scrollBar: UIComponent = driver.findComponent(On().onType("Scroll"))
let button = scrollBar.scrollSearch(On().text("next page"))
```

### func scrollToBottom(Int64)

```cangjie
public func scrollToBottom(speed!: Int64 = 600): Unit
```

**功能：** 在控件上滑动到底部，适用支持滑动的控件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|speed|Int64|否|600| **命名参数。** 滑动速率，范围：200-15000，不在范围内设为默认值为600，单位：像素点/秒。|

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
let scrollBar: UIComponent = driver.findComponent(On().onType("Scroll"))
scrollBar.scrollToBottom()
```