## class CurrentLocationRequest

```cangjie
public class CurrentLocationRequest {
    public var priority: LocationRequestPriority
    public var scenario: LocationRequestScenario
    public var maxAccuracy: Float32
    public var timeoutMs: Int32
    public init(priority!: LocationRequestPriority = LocationRequestPriority.FirstFix,
        scenario!: LocationRequestScenario = LocationRequestScenario.Unset, maxAccuracy!: Float32 = 0.0,
        timeoutMs!: Int32 = 5000)
}
```

**功能：** 当前位置信息请求参数。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var maxAccuracy

```cangjie
public var maxAccuracy: Float32
```

**功能：** 应用向系统请求位置信息时要求的精度值，单位为米。该参数仅在精确位置功能场景（即同时授权了ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（即仅授权了ohos.permission.APPROXIMATELY_LOCATION 权限）下该字段无意义。

该参数生效的情况下，系统会对比GNSS或网络定位服务上报的位置信息与应用的位置信息申请。当位置信息[Location](#class-location)中的精度值（accuracy）小于等于应用要求的精度值（maxAccuracy）时，位置信息会返回给应用；否则系统将丢弃本次收到的位置信息。

当scenario为NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。

当scenario为DAILY_LIFE_SERVICE/NO_POWER或者priority为LOW_POWER/FIRST_FIX时建议设置maxAccuracy为大于100的值。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var priority

```cangjie
public var priority: LocationRequestPriority
```

**功能：** 表示优先级信息。当scenario取值为Unset时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为Unset时，无法发起定位请求。取值范围见[LocationRequestPriority](#enum-locationrequestpriority)的定义。

**类型：** [LocationRequestPriority](#enum-locationrequestpriority)

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var scenario

```cangjie
public var scenario: LocationRequestScenario
```

**功能：** 表示场景信息。当scenario取值为Unset时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为Unset时，无法发起定位请求。取值范围见[LocationRequestScenario](#enum-locationrequestscenario)的定义。

**类型：** [LocationRequestScenario](#enum-locationrequestscenario)

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var timeoutMs

```cangjie
public var timeoutMs: Int32
```

**功能：** 表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22