### func resize(Int32, Int32, ResizeDirection)

```cangjie
public func resize(wide: Int32, height: Int32, direction: ResizeDirection): Unit
```

**功能：** 根据传入的宽、高和调整方向来调整窗口的大小。适用于支持调整大小的窗口。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|wide|Int32|是|-|以Int32的形式传入调整后窗口的宽度，取值范围：大于等于0的整数。|
|height|Int32|是|-|以Int32的形式传入调整后窗口的高度，取值范围：大于等于0的整数。|
|direction|[ResizeDirection](#enum-resizedirection)|是|-|以ResizeDirection的形式传入窗口调整的方向。|

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
    window?.resize(100, 100, ResizeDirection.Left)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func resume()

```cangjie
public func resume(): Unit
```

**功能：** 将窗口恢复到之前的窗口模式。

> **说明：**
>
> 该接口在Tablet设备中可正常调用，在手机设备中返回17000005错误码。

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
    window?.resume()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func split()

```cangjie
public func split(): Unit
```

**功能：** 将窗口模式切换成分屏模式。适用于支持切换分屏模式的窗口。

> **说明：**
>
> 该接口在Tablet设备中可正常调用，在手机设备中返回17000005错误码。

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
    window?.split()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```