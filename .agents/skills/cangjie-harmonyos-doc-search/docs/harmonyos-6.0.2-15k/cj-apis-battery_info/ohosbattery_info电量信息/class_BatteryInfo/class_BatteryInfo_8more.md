## class BatteryInfo

```cangjie
public class BatteryInfo {}
```

**功能：** 描述电池信息的类。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.BatteryInfo
import kit.PerformanceAnalysisKit.*

let batterySOCInfo = BatteryInfo.batterySOC
Hilog.info(0, "batteryInfo", "The batterySOCInfo is: {batterySOCInfo}")
let chargingStatusInfo = BatteryInfo.chargingStatus
Hilog.info(0, "batteryInfo", "The chargingStatusInfo is: {chargingStatusInfo}")
let healthStatusInfo = BatteryInfo.healthStatus
Hilog.info(0, "batteryInfo", "The healthStatusInfo is: {healthStatusInfo}")
let pluggedTypeInfo = BatteryInfo.pluggedType
Hilog.info(0, "batteryInfo", "The pluggedTypeInfo is: {pluggedTypeInfo}")
let voltageInfo = BatteryInfo.voltage
Hilog.info(0, "batteryInfo", "The voltageInfo is: {voltageInfo}")
let technologyInfo = BatteryInfo.technology
Hilog.info(0, "batteryInfo", "The technologyInfo is: {technologyInfo}")
let batteryTemperatureInfo = BatteryInfo.batteryTemperature
Hilog.info(0, "batteryInfo", "The batteryTemperatureInfois: ${batteryTemperatureInfo}")
let isBatteryPresentInfo = BatteryInfo.isBatteryPresent
Hilog.info(0, "batteryInfo", "The isBatteryPresentInfo is: {isBatteryPresentInfo}")
let batteryCapacityLevelInfo = BatteryInfobatteryCapacityLevel
Hilog.info(0, "batteryInfo", "The batteryCapacityLevelInfois: ${batteryCapacityLevelInfo}")
let nowCurrentInfo = BatteryInfo.nowCurrent
Hilog.info(0, "batteryInfo", "The nowCurrentInfo is: ${nowCurrentInfo}")
```

### static prop batteryCapacityLevel

```cangjie
public static prop batteryCapacityLevel: BatteryCapacityLevel
```

**功能：** 表示当前设备电池电量的等级。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**类型：** [BatteryCapacityLevel](#enum-batterycapacitylevel)

**读写能力：** 只读

**起始版本：** 19

### static prop batterySOC

```cangjie
public static prop batterySOC: Int32
```

**功能：** 表示当前设备剩余电池电量百分比。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### static prop batteryTemperature

```cangjie
public static prop batteryTemperature: Int32
```

**功能：** 表示当前设备电池的温度。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### static prop chargingStatus

```cangjie
public static prop chargingStatus: BatteryChargeState
```

**功能：** 表示当前设备电池的充电状态。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**类型：** [BatteryChargeState](#enum-batterychargestate)

**读写能力：** 只读

**起始版本：** 19

### static prop healthStatus

```cangjie
public static prop healthStatus: BatteryHealthState
```

**功能：** 表示当前设备电池的健康状态。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**类型：** [BatteryHealthState](#enum-batteryhealthstate)

**读写能力：** 只读

**起始版本：** 19

### static prop isBatteryPresent

```cangjie
public static prop isBatteryPresent: Bool
```

**功能：** 表示当前设备是否支持电池或者电池是否在位。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### static prop nowCurrent

```cangjie
public static prop nowCurrent: Int32
```

**功能：** 表示当前设备电池的电流。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19