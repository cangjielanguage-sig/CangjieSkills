### func maximize()

```cangjie
public func maximize(): Unit
```

**功能：** 将窗口最大化。适用于支持窗口最大化操作的窗口。

**说明** 该接口在Tablet设备中可正常调用，在手机设备中返回17000005错误码。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |
  | 17000005 | This operation is not supported. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let window: Option<UiWindow> = driver.findWindow(WindowFilter(active: true))
    window?.maximize()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func minimize()

```cangjie
public func minimize(): Unit
```

**功能：** 将窗口最小化。适用于支持窗口最小化操作的窗口。

**说明** 该接口在Tablet设备中可正常调用，在手机设备中返回17000005错误码。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |
  | 17000005 | This operation is not supported. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let window: Option<UiWindow> = driver.findWindow(WindowFilter(active: true))
    window?.minimize()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func moveTo(Int32, Int32)

```cangjie
public func moveTo(x: Int32, y: Int32): Unit
```

**功能：** 将窗口移动到目标点。适用于支持移动的窗口。

**说明** 该接口在Tablet设备中可正常调用，在手机设备中返回17000005错误码。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int32|是|-|以Int32的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。|
|y|Int32|是|-|以Int32的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。|

**异常：**

- BusinessException：对应错误码如下表，详见[uitest错误码](./cj-errorcode-uitest.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17000004 | The window or component is invisible or destroyed. |
  | 17000005 | This operation is not supported. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let driver: Driver = Driver.create()
    let window: Option<UiWindow> = driver.findWindow(WindowFilter(active: true))
    window?.moveTo(100, 100)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```