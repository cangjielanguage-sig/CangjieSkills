### init(LocationRequestPriority, LocationRequestScenario, Float32, Int32)

```cangjie
public init(priority!: LocationRequestPriority = LocationRequestPriority.FirstFix,
    scenario!: LocationRequestScenario = LocationRequestScenario.Unset, maxAccuracy!: Float32 = 0.0,
    timeoutMs!: Int32 = 5000)
```

**功能：** 构造CurrentLocationRequest对象。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|priority|[LocationRequestPriority](#enum-locationrequestpriority)|否|LocationRequestPriority.FirstFix|**命名参数。** 表示优先级信息。当scenario取值为Unset时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为Unset时，无法发起定位请求。取值范围见[LocationRequestPriority](#enum-locationrequestpriority)的定义。默认值为LocationRequestPriority.FirstFix。|
|scenario|[LocationRequestScenario](#enum-locationrequestscenario)|否|LocationRequestScenario.Unset|**命名参数。** 表示场景信息。当scenario取值为Unset时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为Unset时，无法发起定位请求。取值范围见[LocationRequestScenario](#enum-locationrequestscenario)的定义。默认值为LocationRequestScenario.Unset。|
|maxAccuracy|Float32|否|0.0|**命名参数。** 应用向系统请求位置信息时要求的精度值，单位为米。默认值为0，表示不限制位置信息的精度，取值范围为大于等于0。|
|timeoutMs|Int32|否|5000|**命名参数。** 表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。|