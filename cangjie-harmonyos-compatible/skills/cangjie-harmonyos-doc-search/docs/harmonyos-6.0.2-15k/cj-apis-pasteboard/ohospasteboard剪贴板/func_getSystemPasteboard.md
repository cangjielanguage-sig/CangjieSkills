## func getSystemPasteboard()

```cangjie
public func getSystemPasteboard(): SystemPasteboard
```

**功能：** 获取系统剪贴板对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[SystemPasteboard](#class-systempasteboard)|系统剪贴板对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let sysBoard = getSystemPasteboard()
```