### func scrollToBottom(Int64)

```cangjie
public func scrollToBottom(speed!: Int64 = 600): Unit
```

**功能：** 在控件上滑动到底部（适用支持滑动的控件）。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|speed|Int64|否|600| **命名参数。** 滑动速率，取值范围为200-40000的整数，默认值为600，不在范围内设为默认值为600，单位：px/s。|

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
    scrollBar.scrollToBottom()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func scrollToTop(Int64)

```cangjie
public func scrollToTop(speed!: Int64 = 600): Unit
```

**功能：** 在控件上滑动到顶部（适用支持滑动的控件）。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|speed|Int64|否|600| **命名参数。** 滑动速率，取值范围为200-40000的整数，默认值为600，不在范围内设为默认值为600，单位：px/s。|

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
    scrollBar.scrollToTop()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```