## enum ScanDuty

```cangjie
public enum ScanDuty <: Equatable<ScanDuty> & ToString {
    | SCAN_MODE_LOW_POWER
    | SCAN_MODE_BALANCED
    | SCAN_MODE_LOW_LATENCY
    | ...
}
```

**功能：** 扫描模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<ScanDuty>
- ToString

### SCAN_MODE_BALANCED

```cangjie
SCAN_MODE_BALANCED
```

**功能：** 表示均衡模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### SCAN_MODE_LOW_LATENCY

```cangjie
SCAN_MODE_LOW_LATENCY
```

**功能：** 表示低延迟模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### SCAN_MODE_LOW_POWER

```cangjie
SCAN_MODE_LOW_POWER
```

**功能：** 表示低功耗模式，默认值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(ScanDuty)

```cangjie
public operator func !=(other: ScanDuty): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ScanDuty](#enum-scanduty)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ScanDuty)

```cangjie
public operator func ==(other: ScanDuty): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ScanDuty](#enum-scanduty)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|