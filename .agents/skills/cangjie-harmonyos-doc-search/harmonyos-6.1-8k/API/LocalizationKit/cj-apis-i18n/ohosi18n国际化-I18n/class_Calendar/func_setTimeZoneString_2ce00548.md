### func setTimeZone(String)

```cangjie
public func setTimeZone(timeZone: String): Unit
```

**功能：** 设置日历对象的时区。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeZone|String|是|-|合法的时区ID，如“Asia/Shanghai”。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.getCalendar
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("en-US")
    calendar.setTimeZone("Asia/Shanghai")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```