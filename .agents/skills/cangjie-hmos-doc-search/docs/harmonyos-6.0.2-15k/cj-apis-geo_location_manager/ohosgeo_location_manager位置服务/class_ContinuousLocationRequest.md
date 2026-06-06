## class ContinuousLocationRequest

```cangjie
public class ContinuousLocationRequest {
    public var interval: Int32
    public init(interval: Int32, locationScenario: UserActivityScenario)
    public init(interval: Int32, locationScenario: PowerConsumptionScenario)
}
```

**功能：** 持续定位的请求参数。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### prop locationScenario

```cangjie
public mut prop locationScenario: Int32
```

**功能：** 表示定位的场景信息。取值范围见[UserActivityScenario](#enum-useractivityscenario)和[PowerConsumptionScenario](#enum-powerconsumptionscenario)的定义。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var interval

```cangjie
public var interval: Int32
```

**功能：** 表示上报位置信息的时间间隔，单位是秒。默认值为1，取值范围为大于等于0。等于0时对位置上报时间间隔无限制。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### init(Int32, UserActivityScenario)

```cangjie
public init(interval: Int32, locationScenario: UserActivityScenario)
```

**功能：** 构造ContinuousLocationRequest对象。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|interval|Int32|是|-|表示上报位置信息的时间间隔，单位是秒。默认值为1，取值范围为大于等于0。等于0时对位置上报时间间隔无限制。|
|locationScenario|[UserActivityScenario](#enum-useractivityscenario)|是|-| 表示定位的场景信息。|

### init(Int32, PowerConsumptionScenario)

```cangjie
public init(interval: Int32, locationScenario: PowerConsumptionScenario)
```

**功能：** 构造ContinuousLocationRequest对象。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|interval|Int32|是|-|表示上报位置信息的时间间隔，单位是秒。默认值为1，取值范围为大于等于0。等于0时对位置上报时间间隔无限制。|
|locationScenario|[PowerConsumptionScenario](#enum-powerconsumptionscenario)|是|-|表示定位的场景信息。|