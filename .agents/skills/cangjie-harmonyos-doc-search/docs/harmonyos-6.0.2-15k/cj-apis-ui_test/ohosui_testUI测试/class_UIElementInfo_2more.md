## class UIElementInfo

```cangjie
public class UIElementInfo {
    public UIElementInfo(
        public let bundleName: String,
        public let componentType: String,
        public let text: String
    )
}
```

**功能：** UI事件的相关信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### let bundleName

```cangjie
public let bundleName: String
```

**功能：** 归属应用的包名。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let componentType

```cangjie
public let componentType: String
```

**功能：** 控件或窗口类型。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let text

```cangjie
public let text: String
```

**功能：** 控件或窗口的文本信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### UIElementInfo(String, String, String)

```cangjie
public UIElementInfo(
    public let bundleName: String,
    public let componentType: String,
    public let text: String
)
```

**功能：** 创建[UIElementInfo](#class-uielementinfo)实例。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName|String|是|-|归属应用的包名。|
|componentType|String|是|-|控件或窗口类型。|
|text|String|是|-|控件或窗口的文本信息。|

## class UIEventObserver

```cangjie
public class UIEventObserver {}
```

**功能：** UI事件监听器。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### func onceDialogShow((UIElementInfo) -> Unit)

```cangjie
public func onceDialogShow(callback: (UIElementInfo) -> Unit): Unit
```

**功能：** 监听dialog控件出现的事件，使用callback的形式返回结果。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([UIElementInfo](#class-uielementinfo)) -> Unit|是|-|事件发生时执行的回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*
import kit.PerformanceAnalysisKit.*

let driver: Driver = Driver.create()
let observer: UIEventObserver = driver.createUIEventObserver()
observer.onceDialogShow({element =>
    Hilog.info(0, "", element.bundleName)
    Hilog.info(0, "", element.componentType)
    Hilog.info(0, "", element.text)
})
```

### func onceToastShow((UIElementInfo) -> Unit)

```cangjie
public func onceToastShow(callback: (UIElementInfo) -> Unit): Unit
```

**功能：** 监听toast控件出现的事件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([UIElementInfo](#class-uielementinfo)) -> Unit|是|-|事件发生时执行的回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*
import kit.PerformanceAnalysisKit.*

let driver: Driver = Driver.create()
let observer: UIEventObserver = driver.createUIEventObserver()
observer.onceToastShow({element =>
    Hilog.info(0, "", element.bundleName)
    Hilog.info(0, "", element.componentType)
    Hilog.info(0, "", element.text)
})
```