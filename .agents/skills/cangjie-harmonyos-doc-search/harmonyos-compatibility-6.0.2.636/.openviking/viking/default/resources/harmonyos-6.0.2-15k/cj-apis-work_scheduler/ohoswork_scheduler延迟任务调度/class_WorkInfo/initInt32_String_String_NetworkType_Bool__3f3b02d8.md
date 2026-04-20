### init(Int32, String, String, ?NetworkType, ?Bool, ?ChargingType, ?Int32, ?BatteryStatus, ?StorageRequest, ?Bool, ?Int32, ?Int32, ?Bool, ?Bool, ?Int32)

```cangjie
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
```

**功能：** 构造延迟任务的具体信息的对象。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|workId|Int32|是|-|延迟任务ID。|
|bundleName|String|是|-|延迟任务包名。|
|abilityName|String|是|-|延迟任务回调通知的组件名。|
|netWorkType|?NetworkType|否|None| **命名参数。** 网络类型。|
|isCharging|?Bool|否|None| **命名参数。** 是否充电。<br>- true表示充电触发延迟回调。<br>- false表示不充电触发延迟回调。|
|chargerType|?[ChargingType](#enum-chargingtype)|否|None| **命名参数。** 充电类型。|
|batteryLevel|?Int32|否|None| **命名参数。** 电量。|
|batteryStatus|?[BatteryStatus](#enum-batterystatus)|否|None| **命名参数。** 电池状态。|
|storageRequest|?[StorageRequest](#enum-storagerequest)|否|None| **命名参数。** 存储状态。|
|isRepeat|?Bool|否|None| **命名参数。** 是否循环任务。<br>- true表示循环任务。<br>- false表示非循环任务。|
|repeatCycleTime|?Int32|否|None| **命名参数。** 循环间隔，单位为毫秒。|
|repeatCount|?Int32|否|None| **命名参数。** 循环次数。|
|isPersisted|?Bool|否|None| **命名参数。** 是否持久化保存工作。<br>- true表示持久化保存工作。<br>- false表示非持久化保存工作。|
|isDeepIdle|?Bool|否|None| **命名参数。** 是否要求设备进入空闲状态。<br>- true表示需要。<br>- false表示不需要。|
|idleWaitTime|?Int32|否|None| **命名参数。** 空闲等待时间，单位为毫秒。|