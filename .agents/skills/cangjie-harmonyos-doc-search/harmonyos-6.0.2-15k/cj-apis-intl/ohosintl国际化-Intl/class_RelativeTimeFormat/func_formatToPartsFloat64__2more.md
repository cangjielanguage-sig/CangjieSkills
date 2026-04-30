### func formatToParts(Float64, String)

```cangjie
public func formatToParts(value: Float64, unit: String): Array<Array<String>>
```

**功能：** 自定义区域的相对时间格式。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|相对时间格式化的数值。|
|unit|String|是|-|相对时间格式化的单位，取值包括："year", "quarter", "month", "week", "day", "hour", "minute", "second"。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Array\<String>>|相对时间格式的对象数组。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用en locale创建RelativeTimeFormat对象，numeric设置为auto
let r = RelativeTimeFormatInputOptions(numeric: "auto")
let relativetimefmt = RelativeTimeFormat("en", options: r)
let parts = relativetimefmt.formatToParts(10.0, "seconds") // parts = [ ["literal", "in"], ["integer", "10","seconds"], ["literal", "seconds"] ]
```

### func resolvedOptions()

```cangjie
public func resolvedOptions(): RelativeTimeFormatResolvedOptions
```

**功能：** 获取RelativeTimeFormat对象的格式化选项。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[RelativeTimeFormatResolvedOptions](#struct-relativetimeformatresolvedoptions)|RelativeTimeFormat对象的格式化选项。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用en-GB locale创建RelativeTimeFormat对象
let r = RelativeTimeFormatInputOptions(style: "short")
let relativetimefmt = RelativeTimeFormat("en-GB", options: r)
// 获取RelativeTimeFormat对象配置项
let options = relativetimefmt.resolvedOptions()
let style = options.style // style = "short"
```