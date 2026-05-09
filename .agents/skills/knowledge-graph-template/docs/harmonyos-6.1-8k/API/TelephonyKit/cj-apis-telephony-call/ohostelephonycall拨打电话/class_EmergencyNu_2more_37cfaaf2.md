## class EmergencyNumberOptions

```cangjie
public class EmergencyNumberOptions {
    public var slotId: Int32
    public init(slotId!: Int32 = 0)
}
```

**功能：** 判断是否是紧急电话号码的可选参数。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

### var slotId

```cangjie
public var slotId: Int32
```

**功能：** 卡槽ID：

- 卡槽1：`0`。

- 卡槽2：`1`。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

### init(Int32)

```cangjie
public init(slotId!: Int32 = 0)
```

**功能：** EmergencyNumberOptions构造器。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|否|0|**命名参数。** 卡槽ID。|

## class NumberFormatOptions

```cangjie
public class NumberFormatOptions {
    public var countryCode: String
    public init(countryCode!: String = "CN")
}
```

**功能：** 格式化号码的可选参数。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

### var countryCode

```cangjie
public var countryCode: String
```

**功能：** 国家码，支持所有国家的国家码，如：CN（中国）。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

### init(String)

```cangjie
public init(countryCode!: String = "CN")
```

**功能：** 用于创建NumberFormatOptions实例的构造函数。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|countryCode|String|否|"CN"|**命名参数。** 国家码，支持所有国家的国家码，如：CN（中国）。默认为："CN"。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TelephonyKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let op = NumberFormatOptions(countryCode: "CN")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```