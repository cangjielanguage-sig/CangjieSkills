### func getText()

```cangjie
public func getText(): String
```

**功能：** 获取控件对象的文本信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|返回控件的文本信息。|

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
    let text: String = button.getText()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getType()

```cangjie
public func getType(): String
```

**功能：** 获取控件对象的控件类型。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|返回控件的类型。|

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
    let btype: String = button.getType()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func inputText(String)

```cangjie
public func inputText(text: String): Unit
```

**功能：** 清空组件内原有文本并输入指定文本内容，仅针对可编辑的文本组件生效。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|输入的文本信息，当前支持英文、中文和特殊字符。|

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
    let txt: Component = driver.findComponent(On().text("cangjie")).getOrThrow()
    txt.inputText("111")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isCheckable()

```cangjie
public func isCheckable(): Bool
```

**功能：** 判断控件对象能否被勾选。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回控件对象能否可被勾选属性。true：可被勾选。false：不可被勾选。|

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
    let c: Bool = button.isCheckable()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```