## enum ScanReportMode

```cangjie
public enum ScanReportMode <: Equatable<ScanReportMode> & ToString {
    | Normal
    | Batch
    | FenceSensitivityLow
    | FenceSensitivityHigh
    | ...
}
```

**功能：** 枚举，扫描结果上报模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<ScanReportMode>
- ToString

### Batch

```cangjie
Batch
```

**功能：** 批量扫描上报模式。

- 该模式可通过降低蓝牙芯片上报扫描结果频率，使系统更长时间地保持在休眠状态，从而降低整机功耗。

- 该模式下，扫描到符合过滤条件的BLE广播报文后不会立刻上报，需要缓存一段时间（[ScanOptions](#class-scanoptions)中的interval字段）后上报。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### FenceSensitivityHigh

```cangjie
FenceSensitivityHigh
```

**功能：** 高灵敏度围栏上报模式。

- 围栏模式表示只在广播进入或离开围栏时上报。

- 扫描到的广播信号强度低且广播数量少时，可进入高灵敏度围栏。

- 首次扫描到广播即进入围栏，触发一次上报。

- 一段时间内扫描不到广播即离开围栏，触发一次上报。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### FenceSensitivityLow

```cangjie
FenceSensitivityLow
```

**功能：** 低灵敏度围栏上报模式。

- 围栏模式表示只在广播进入或离开围栏时上报。

- 扫描到的广播信号强度高且广播数量多时，可进入低灵敏度围栏。

- 首次扫描到广播即进入围栏，触发一次上报。

- 一段时间内扫描不到广播即离开围栏，触发一次上报。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### Normal

```cangjie
Normal
```

**功能：** 常规扫描上报模式，扫描到符合过滤条件的BLE广播报文后就会立刻上报。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(ScanReportMode)

```cangjie
public operator func !=(other: ScanReportMode): Bool
```

**功能：** 对扫描上报模式进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScanReportMode](#enum-scanreportmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果扫描结果数据上报模式不同，返回true，否则返回false。|

### func ==(ScanReportMode)

```cangjie
public operator func ==(other: ScanReportMode): Bool
```

**功能：** 对扫描上报模式进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScanReportMode](#enum-scanreportmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果扫描结果数据上报模式相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取扫描结果数据上报模式的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|扫描结果数据上报模式的字符串表示。|