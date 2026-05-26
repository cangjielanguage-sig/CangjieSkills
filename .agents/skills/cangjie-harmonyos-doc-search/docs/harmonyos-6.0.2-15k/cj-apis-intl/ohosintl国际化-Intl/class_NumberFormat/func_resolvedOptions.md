### func resolvedOptions()

```cangjie
public func resolvedOptions(): NumberOptions
```

**功能：** 获取创建数字格式化对象时设置的配置项。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[NumberOptions](#struct-numberoptions)|创建数字格式化对象时设置的配置项。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let n = NumberOptions(style: 'decimal', notation: "scientific")
let numfmt = NumberFormat(["zh"], options: n)
// 获取NumberFormat对象配置项
let options = numfmt.resolvedOptions()
let style = options.style // style = decimal
let notation = options.notation // notation = scientific
```