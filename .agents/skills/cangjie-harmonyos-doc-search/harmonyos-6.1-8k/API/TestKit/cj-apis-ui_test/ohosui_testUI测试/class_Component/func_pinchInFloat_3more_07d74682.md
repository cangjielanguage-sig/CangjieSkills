### func pinchIn(Float32)

```cangjie
public func pinchIn(scale: Float32): Unit
```

**功能：** 将控件按指定的比例进行捏合缩小。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scale|Float32|是|-|指定缩小的比例。取值范围为0~1。|

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let image: Component = driver.findComponent(On().id("icon")).getOrThrow()
    image.pinchIn(0.5)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func pinchOut(Float32)

```cangjie
public func pinchOut(scale: Float32): Unit
```

**功能：** 将控件按指定的比例进行捏合放大。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scale|Float32|是|-|指定放大的比例。取值范围大于1。|

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let image: Component = driver.findComponent(On().id("icon")).getOrThrow()
    image.pinchOut(2.5)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func scrollSearch(On)

```cangjie
public func scrollSearch(on: On): ?Component
```

**功能：** 在控件上滑动查找目标控件（适用支持滑动的控件）。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|目标控件的属性要求。|

**返回值：**

|类型|说明|
|:----|:----|
|?[Component](#class-component)|返回目标控件对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let scrollBar: Component = driver.findComponent(On().onType("Scroll")).getOrThrow()
    let button: Option<Component> = scrollBar.scrollSearch(On().text("1"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```