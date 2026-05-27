## func hasSmsCapability()

```cangjie
public func hasSmsCapability(): Bool
```

**功能：** 检查当前设备是否具备短信发送和接收能力。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|- true：设备具备短信发送和接收能力。<br/>- false：设备不具备短信发送和接收能力。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

hasSmsCapability()
```