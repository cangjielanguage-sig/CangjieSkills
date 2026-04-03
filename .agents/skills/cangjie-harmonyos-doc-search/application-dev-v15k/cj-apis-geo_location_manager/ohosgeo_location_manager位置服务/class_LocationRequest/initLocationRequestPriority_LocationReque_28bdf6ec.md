### init(LocationRequestPriority, LocationRequestScenario, Int32, Float64, Float32)

```cangjie
public init(priority!: LocationRequestPriority = FIRST_FIX, scenario!: LocationRequestScenario = UNSET,
    timeInterval!: Int32 = 1, distanceInterval!: Float64 = 0.0, maxAccuracy!: Float32 = 0.0)
```

**功能：** 构造LocationRequest对象。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|priority|[LocationRequestPriority](#enum-locationrequestpriority)|否|FIRST_FIX| **命名参数。** 表示优先级信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见[LocationRequestPriority](#enum-locationrequestpriority)的定义。|
|scenario|[LocationRequestScenario](#enum-locationrequestscenario)|否|UNSET| **命名参数。** 表示场景信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见[LocationRequestScenario](#enum-locationrequestscenario)的定义。|
|timeInterval|Int32|否|1| **命名参数。** 表示上报位置信息的时间间隔，单位是秒。默认值为1，取值范围为大于等于0。等于0时对位置上报时间间隔无限制。|
|distanceInterval|Float64|否|0.0| **命名参数。** 表示上报位置信息的距离间隔。单位是米，默认值为0，取值范围为大于等于0。等于0时对位置上报距离间隔无限制。|
|maxAccuracy|Float32|否|0.0| **命名参数。** 表示精度信息，单位是米。<br/>仅在精确位置功能场景（同时授予了ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（仅授予了ohos.permission.APPROXIMATELY_LOCATION 权限）下该字段无意义。<br/>默认值为0，取值范围为大于等于0。<br/>当scenario为NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。<br/>当scenario为DAILY_LIFE_SERVICE/NO_POWER或者priority为LOW_POWER/FIRST_FIX时建议设置maxAccuracy为大于100的值。|