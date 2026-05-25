## enum ScanDuty

```cangjie
public enum ScanDuty <: Equatable<ScanDuty> & ToString {
    | ScanModeLowPower
    | ScanModeBalanced
    | ScanModeLowLatency
    | ...
}
```

**功能：** 枚举，扫描模式，表示不同的扫描性能和功耗情况。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<ScanDuty>
- ToString

### ScanModeBalanced

```cangjie
ScanModeBalanced
```

**功能：** 均衡模式，平衡扫描性能和功耗。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### ScanModeLowLatency

```cangjie
ScanModeLowLatency
```

**功能：** 低延迟模式，扫描性能较高，但功耗也较高。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### ScanModeLowPower

```cangjie
ScanModeLowPower
```

**功能：** 低功耗模式，扫描性能较低，功耗也较低。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(ScanDuty)

```cangjie
public operator func !=(other: ScanDuty): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScanDuty](#enum-scanduty)|是|-|另一个枚举值。|

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

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScanDuty](#enum-scanduty)|是|-|另一个枚举值。|

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|