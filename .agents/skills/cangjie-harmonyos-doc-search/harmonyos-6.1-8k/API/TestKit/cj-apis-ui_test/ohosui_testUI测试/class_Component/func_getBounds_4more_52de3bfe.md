### func getBounds()

```cangjie
public func getBounds(): Rect
```

**功能：** 获取控件对象的边框信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Rect](#class-rect)|返回控件对象的边框信息。|

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
    let button: Component = driver.findComponent(On().id("button")).getOrThrow()
    let rect: Rect = button.getBounds()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getBoundsCenter()

```cangjie
public func getBoundsCenter(): Point
```

**功能：** 获取控件对象所占区域的中心点信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Point](#class-point)|返回控件对象所占区域的中心点信息。|

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
    let button: Component = driver.findComponent(On().id("button")).getOrThrow()
    let point = button.getBoundsCenter()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getDescription()

```cangjie
public func getDescription(): String
```

**功能：** 获取控件对象的描述信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|返回控件的描述信息。|

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
    let button: Component = driver.findComponent(On().id("button")).getOrThrow()
    let des: String = button.getDescription()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getId()

```cangjie
public func getId(): String
```

**功能：** 获取控件对象的id值。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|返回控件的id值。|

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
    let button: Component = driver.findComponent(On().id("button")).getOrThrow()
    let id: String = button.getId()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```