## class LocationRequest

```cangjie
public class LocationRequest {
    public var priority: LocationRequestPriority
    public var scenario: LocationRequestScenario
    public var timeInterval: Int32
    public var distanceInterval: Float64
    public var maxAccuracy: Float32
    public init(priority!: LocationRequestPriority = FIRST_FIX, scenario!: LocationRequestScenario = UNSET,
        timeInterval!: Int32 = 1, distanceInterval!: Float64 = 0.0, maxAccuracy!: Float32 = 0.0)
}
```

**功能：** 位置信息请求参数。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### var distanceInterval

```cangjie
public var distanceInterval: Float64
```

**功能：** 表示上报位置信息的距离间隔。单位是米，默认值为0，取值范围为大于等于0。等于0时对位置上报距离间隔无限制。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var maxAccuracy

```cangjie
public var maxAccuracy: Float32
```

**功能：** 表示精度信息，单位是米。

仅在精确位置功能场景（同时授予了ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（仅授予了ohos.permission.APPROXIMATELY_LOCATION 权限）下该字段无意义。

默认值为0，取值范围为大于等于0。

当scenario为NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。

当scenario为DAILY_LIFE_SERVICE/NO_POWER或者priority为LOW_POWER/FIRST_FIX时建议设置maxAccuracy为大于100的值。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var priority

```cangjie
public var priority: LocationRequestPriority
```

**功能：** 表示优先级信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见[LocationRequestPriority](#enum-locationrequestpriority)的定义。

**类型：** [LocationRequestPriority](#enum-locationrequestpriority)

**读写能力：** 可读写

**起始版本：** 19

### var scenario

```cangjie
public var scenario: LocationRequestScenario
```

**功能：** 表示场景信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见[LocationRequestScenario](#enum-locationrequestscenario)的定义。

**类型：** [LocationRequestScenario](#enum-locationrequestscenario)

**读写能力：** 可读写

**起始版本：** 19

### var timeInterval

```cangjie
public var timeInterval: Int32
```

**功能：** 表示上报位置信息的时间间隔，单位是秒。默认值为1，取值范围为大于等于0。等于0时对位置上报时间间隔无限制。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19