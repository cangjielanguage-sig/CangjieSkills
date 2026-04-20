## class SingleLocationRequest

```cangjie
public class SingleLocationRequest {
    public var locatingPriority: LocatingPriority
    public var locatingTimeoutMs: Int32
    public init(locatingPriority: LocatingPriority, locatingTimeoutMs: Int32)
}
```

**功能：** 单次定位的请求参数。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var locatingPriority

```cangjie
public var locatingPriority: LocatingPriority
```

**功能：** 表示优先级信息。取值范围见[LocatingPriority](#enum-locatingpriority)的定义。

**类型：** [LocatingPriority](#enum-locatingpriority)

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var locatingTimeoutMs

```cangjie
public var locatingTimeoutMs: Int32
```

**功能：** 表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### init(LocatingPriority, Int32)

```cangjie
public init(locatingPriority: LocatingPriority, locatingTimeoutMs: Int32)
```

**功能：** 构造SingleLocationRequest对象。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locatingPriority|[LocatingPriority](#enum-locatingpriority)|是|-|表示优先级信息。取值范围见[LocatingPriority](#enum-locatingpriority)的定义。|
|locatingTimeoutMs|Int32|是|-|表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。|

## enum LocatingPriority

```cangjie
public enum LocatingPriority {
    | PriorityAccuracy
    | PriorityLocatingSpeed
    | ...
}
```

**功能：** 单次位置请求中的优先级类型。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### PriorityAccuracy

```cangjie
PriorityAccuracy
```

**功能：** 表示精度优先。

定位精度优先策略会同时使用GNSS定位和网络定位技术，并把一段时间内精度较好的结果返回给应用；这个时间段长度为[SingleLocationRequest](#class-singlelocationrequest).locatingTimeoutMs与“30秒”中的较小者。

对设备的硬件资源消耗较大，功耗较大。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### PriorityLocatingSpeed

```cangjie
PriorityLocatingSpeed
```

**功能：** 表示快速获取位置优先，如果应用希望快速拿到一个位置，可以将优先级设置为该类型。

快速定位优先策略会同时使用GNSS定位和网络定位技术，以便在室内和户外场景下均可以快速获取到位置结果，我们会把最先拿到的定位结果返回给应用。对设备的硬件资源消耗较大，功耗也较大。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22