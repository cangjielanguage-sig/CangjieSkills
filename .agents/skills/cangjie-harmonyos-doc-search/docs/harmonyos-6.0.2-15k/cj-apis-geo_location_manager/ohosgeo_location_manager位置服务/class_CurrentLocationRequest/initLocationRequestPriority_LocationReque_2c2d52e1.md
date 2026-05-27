### init(LocationRequestPriority, LocationRequestScenario, Float32, Int32)

```cangjie
public init(priority!: LocationRequestPriority = LocationRequestPriority.FIRST_FIX,
    scenario!: LocationRequestScenario = LocationRequestScenario.UNSET,
    maxAccuracy!: Float32 = 0.0, timeoutMs!: Int32 = 5000)
```

**功能：** 构造CurrentLocationRequest对象。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|priority|[LocationRequestPriority](#enum-locationrequestpriority)|否|LocationRequestPriority.FIRST_FIX| **命名参数。** 表示优先级信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见[LocationRequestPriority](#enum-locationrequestpriority)的定义。|
|scenario|[LocationRequestScenario](#enum-locationrequestscenario)|否|LocationRequestScenario.UNSET| **命名参数。** 表示场景信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见[LocationRequestScenario](#enum-locationrequestscenario)的定义。|
|maxAccuracy|Float32|否|0.0| **命名参数。** 表示精度信息，单位是米。<br/>仅在精确位置功能场景（同时授予了ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（仅授予了ohos.permission.APPROXIMATELY_LOCATION 权限）下该字段无意义。<br/>默认值为0，取值范围为大于等于0。<br/>当scenario为NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。<br/>当scenario为DAILY_LIFE_SERVICE/NO_POWER或者priority为LOW_POWER/FIRST_FIX时建议设置maxAccuracy为大于100的值。|
|timeoutMs|Int32|否|5000| **命名参数。** 表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。|