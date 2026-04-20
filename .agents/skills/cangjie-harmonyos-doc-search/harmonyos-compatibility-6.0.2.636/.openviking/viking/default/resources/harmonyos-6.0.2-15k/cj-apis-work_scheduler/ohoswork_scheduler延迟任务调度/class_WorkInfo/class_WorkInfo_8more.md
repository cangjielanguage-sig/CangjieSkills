## class WorkInfo

```cangjie
public class WorkInfo {
    public var workId: Int32
    public var bundleName: String
    public var abilityName: String
    public var netWorkType: ?NetworkType = None
    public var isCharging: ?Bool = None
    public var chargerType: ?ChargingType = None
    public var batteryLevel: ?Int32 = None
    public var batteryStatus: ?BatteryStatus = None
    public var storageRequest: ?StorageRequest = None
    public var isRepeat: ?Bool = None
    public var repeatCycleTime: ?Int32 = None
    public var repeatCount: ?Int32 = None
    public var isPersisted: ?Bool = None
    public var isDeepIdle: ?Bool = None
    public var idleWaitTime: ?Int32 = None
    public var parameters: HashMap<String, WorkSchedulerValueType> = HashMap<String, WorkSchedulerValueType>()

    public init(
        workId: Int32,
        bundleName: String,
        abilityName: String,
        netWorkType!: ?NetworkType = None,
        isCharging!: ?Bool = None,
        chargerType!: ?ChargingType = None,
        batteryLevel!: ?Int32 = None,
        batteryStatus!: ?BatteryStatus = None,
        storageRequest!: ?StorageRequest = None,
        isRepeat!: ?Bool = None,
        repeatCycleTime!: ?Int32 = None,
        repeatCount!: ?Int32 = None,
        isPersisted!: ?Bool = None,
        isDeepIdle!: ?Bool = None,
        idleWaitTime!: ?Int32 = None
    )

    public init(
        workId: Int32,
        bundleName: String,
        abilityName: String,
        parameters: HashMap<String, WorkSchedulerValueType>,
        netWorkType!: ?NetworkType = None,
        isCharging!: ?Bool = None,
        chargerType!: ?ChargingType = None,
        batteryLevel!: ?Int32 = None,
        batteryStatus!: ?BatteryStatus = None,
        storageRequest!: ?StorageRequest = None,
        isRepeat!: ?Bool = None,
        repeatCycleTime!: ?Int32 = None,
        repeatCount!: ?Int32 = None,
        isPersisted!: ?Bool = None,
        isDeepIdle!: ?Bool = None,
        idleWaitTime!: ?Int32 = None
    )
}
```

**功能：** 延迟任务具体信息。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### var abilityName

```cangjie
public var abilityName: String
```

**功能：** 包内ability名称。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var batteryLevel

```cangjie
public var batteryLevel: ?Int32 = None
```

**功能：** 电量。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 12

### var batteryStatus

```cangjie
public var batteryStatus: ?BatteryStatus = None
```

**功能：** 电池状态。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** [?BatteryStatus](#enum-batterystatus)

**读写能力：** 可读写

**起始版本：** 12

### var bundleName

```cangjie
public var bundleName: String
```

**功能：** 延迟任务包名。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var chargerType

```cangjie
public var chargerType: ?ChargingType = None
```

**功能：** 充电类型。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** [?ChargingType](#enum-chargingtype)

**读写能力：** 可读写

**起始版本：** 12

### var idleWaitTime

```cangjie
public var idleWaitTime: ?Int32 = None
```

**功能：** 空闲等待时间，单位为毫秒。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 12

### var isCharging

```cangjie
public var isCharging: ?Bool = None
```

**功能：** 是否充电。<br>- true表示充电触发延迟回调。<br>- false表示不充电触发延迟回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 12