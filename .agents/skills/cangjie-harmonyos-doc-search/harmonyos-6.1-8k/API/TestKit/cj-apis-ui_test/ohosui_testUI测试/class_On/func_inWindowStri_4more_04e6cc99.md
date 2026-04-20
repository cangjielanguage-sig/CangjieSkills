### func inWindow(String)

```cangjie
public func inWindow(bundleName: String): On
```

**功能：** 指定目标控件位于给出的应用窗口内，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName|String|是|-|应用窗口的包名。<!--RP2--><!--RP2End-->|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件位于给出的应用窗口内的[On](#class-on)对象。|

**示例：**

<!-- compile -->

```cangjie
//example_test.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let on: On = On().inWindow("com.uitestScene.acts") // 指定目标控件位于给出的应用窗口内。
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isAfter(On)

```cangjie
public func isAfter(on: On): On
```

**功能：** 指定目标控件位于给出的特征属性控件之后，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|特征控件的属性要求。<!--RP3--><!--RP3End-->|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件位于给出的特征属性控件之后的[On](#class-on)对象。|

**示例：**

<!-- compile -->

```cangjie
//example_test.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let on1: On = On().text("123") // 指定特征属性控件
    let on2: On = On().onType("Text").isAfter(on1)  // 查找text为123之后的第一个Text组件
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isBefore(On)

```cangjie
public func isBefore(on: On): On
```

**功能：** 指定目标控件位于给出的特征属性控件之前，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|特征控件的属性要求。<!--RP3--><!--RP3End-->|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件位于给出的特征属性控件之前的[On](#class-on)对象。|

**示例：**

<!-- compile -->

```cangjie
//example_test.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let on1: On = On().text("123") // 指定特征属性控件
    let on2: On = On().onType("Button").isBefore(on1)  // 查找text为123之前的第一个Button组件
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func longClickable(Bool)

```cangjie
public func longClickable(b!: Bool = true): On
```

**功能：** 指定目标控件的可长按点击状态属性，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|b|Bool|否|true|**命名参数。** 指定控件可长按点击状态，true：可长按点击，false：不可长按点击。默认为true。<!--RP2--><!--RP2End-->|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件的可长按点击状态属性的[On](#class-on)对象。|

**示例：**

<!-- compile -->

```cangjie
//example_test.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let on: On = On().longClickable(b: true) // 指定目标控件的可长按点击状态属性。
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```