## class BatteryInfo

```cangjie
public class BatteryInfo {}
```

**功能：** 描述电池信息的类。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### static prop batteryCapacityLevel

```cangjie
public static prop batteryCapacityLevel: BatteryCapacityLevel
```

**功能：** 表示当前设备电池电量的等级。

**类型：** [BatteryCapacityLevel](#enum-batterycapacitylevel)

**读写能力：** 只读

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### static prop batterySoc

```cangjie
public static prop batterySoc: Int32
```

**功能：** 表示当前设备剩余电池电量百分比。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### static prop batteryTemperature

```cangjie
public static prop batteryTemperature: Int32
```

**功能：** 表示当前设备电池的温度，单位0.1摄氏度。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### static prop chargingStatus

```cangjie
public static prop chargingStatus: BatteryChargeState
```

**功能：** 表示当前设备电池的充电状态。

**类型：** [BatteryChargeState](#enum-batterychargestate)

**读写能力：** 只读

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### static prop healthStatus

```cangjie
public static prop healthStatus: BatteryHealthState
```

**功能：** 表示当前设备电池的健康状态。

**类型：** [BatteryHealthState](#enum-batteryhealthstate)

**读写能力：** 只读

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### static prop isBatteryPresent

```cangjie
public static prop isBatteryPresent: Bool
```

**功能：** 表示当前设备是否支持电池或者电池是否在位。true表示支持电池或电池在位，false表示不支持电池或电池不在位，默认为false。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### static prop nowCurrent

```cangjie
public static prop nowCurrent: Int32
```

**功能：** 表示当前设备电池的电流，单位毫安。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### static prop pluggedType

```cangjie
public static prop pluggedType: BatteryPluggedType
```

**功能：** 表示当前设备连接的充电器类型。

**类型：** [BatteryPluggedType](#enum-batterypluggedtype)

**读写能力：** 只读

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### static prop technology

```cangjie
public static prop technology: String
```

**功能：** 表示当前设备电池的技术型号。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### static prop voltage

```cangjie
public static prop voltage: Int32
```

**功能：** 表示当前设备电池的电压，单位微伏。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22