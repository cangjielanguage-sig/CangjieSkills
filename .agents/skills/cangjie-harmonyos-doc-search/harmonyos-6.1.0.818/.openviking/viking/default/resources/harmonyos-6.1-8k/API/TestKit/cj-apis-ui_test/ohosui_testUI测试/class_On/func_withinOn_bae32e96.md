### func within(On)

```cangjie
public func within(on: On): On
```

**功能：** 指定目标控件位于给出的特征属性控件之内，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|[On](#class-on)|是|-|特征控件的属性要求。<!--RP3--><!--RP3End-->|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件位于给出的特征属性控件内的[On](#class-on)对象。|

**示例：**

<!-- compile -->

```cangjie
//example_test.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let on1: On = On().onType("Scroll") // 指定特征属性控件
    let on2: On = On().text("123").within(on1) // 查找Scroller里面的text为123的子组件
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```