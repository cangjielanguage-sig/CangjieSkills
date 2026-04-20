## class UiElementInfo

```cangjie
public class UiElementInfo {
    public let bundleName: String
    public let componentType: String
    public let text: String
}
```

**功能：** UI事件的相关信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### let bundleName

```cangjie
public let bundleName: String
```

**功能：** 应用包名。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### let componentType

```cangjie
public let componentType: String
```

**功能：** 控件/窗口类型。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### let text

```cangjie
public let text: String
```

**功能：** 控件/窗口的文本信息。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

## class UiEventObserver

```cangjie
public class UiEventObserver {}
```

**功能：** UI事件监听器。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### func once(OnceType, Callback\<UiElementInfo>)

```cangjie
public func once(onceType: OnceType, callback: Callback<UiElementInfo>): Unit
```

**功能：** 开始监听指定控件出现的事件。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onceType|[OnceType](#enum-oncetype)|是|-|订阅的事件类型。|
|callback|[Callback](../../reference/arkui-cj/cj-common-types.md#type-callbackt-v)\<[UiElementInfo](#class-uielementinfo)>|是|-|事件发生时执行的回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let driver: Driver = Driver.create()
    let observer: UiEventObserver = driver.createUiEventObserver()
    observer.once(
        OnceType.DialogShow,
        {
            element =>
            Hilog.info(0, "", "onceDialogShow")
            Hilog.info(0, "", element.bundleName)
            Hilog.info(0, "", element.componentType)
            Hilog.info(0, "", element.text)
        }
    )
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```