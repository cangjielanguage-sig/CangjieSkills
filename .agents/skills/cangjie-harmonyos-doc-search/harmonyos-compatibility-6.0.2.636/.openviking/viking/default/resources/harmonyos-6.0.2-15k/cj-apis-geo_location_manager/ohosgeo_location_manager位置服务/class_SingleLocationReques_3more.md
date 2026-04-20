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

**起始版本：** 19

### var locatingPriority

```cangjie
public var locatingPriority: LocatingPriority
```

**功能：** 表示优先级信息。取值范围见[LocatingPriority](#enum-locatingpriority)的定义。

**类型：** [LocatingPriority](#enum-locatingpriority)

**读写能力：** 可读写

**起始版本：** 19

### var locatingTimeoutMs

```cangjie
public var locatingTimeoutMs: Int32
```

**功能：** 表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### init(LocatingPriority, Int32)

```cangjie
public init(locatingPriority: LocatingPriority, locatingTimeoutMs: Int32)
```

**功能：** 构造SingleLocationRequest对象。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locatingPriority|[LocatingPriority](#enum-locatingpriority)|是|-|表示优先级信息。取值范围见[LocatingPriority](#enum-locatingpriority)的定义。|
|locatingTimeoutMs|Int32|是|-|表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。|

## enum CallbackType

```cangjie
public enum CallbackType {
    | LocationChange
    | LocationErr
    | LocationEnabledChange
    | CachedGnssLocationsChange
    | SatelliteStatusChange
    | NmeaMessage
    | CountryCodeChange
    | ...
}
```

**功能：** 表示事件类型。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### CachedGnssLocationsChange

```cangjie
CachedGnssLocationsChange
```

**功能：** 表示GNSS缓存定位结果上报。

**起始版本：** 19

### CountryCodeChange

```cangjie
CountryCodeChange
```

**功能：** 表示订阅国家码信息变化事件。

**起始版本：** 19

### LocationChange

```cangjie
LocationChange
```

**功能：** 表示位置变化。

**起始版本：** 19

### LocationEnabledChange

```cangjie
LocationEnabledChange
```

**功能：** 表示位置服务状态。

**起始版本：** 19

### LocationErr

```cangjie
LocationErr
```

**功能：** 表示持续定位过程中的错误码变化。

**起始版本：** 19

### NmeaMessage

```cangjie
NmeaMessage
```

**功能：** 表示订阅GNSS NMEA信息上报。

**起始版本：** 19

### SatelliteStatusChange

```cangjie
SatelliteStatusChange
```

**功能：** 表示订阅GNSS卫星状态信息上报。

**起始版本：** 19

## enum CoordinateSystemType

```cangjie
public enum CoordinateSystemType {
    | WGS84
    | GCJ02
    | ...
}
```

**功能：** 坐标系类型。

**系统能力：** SystemCapability.Location.Location.Geofence

**起始版本：** 19

### GCJ02

```cangjie
GCJ02
```

**功能：** GCJ-02是由中国国家测绘局制订的地理信息系统的坐标系统。

**起始版本：** 19

### WGS84

```cangjie
WGS84
```

**功能：** World Geodetic System 1984，是为GPS全球定位系统使用而建立的坐标系统。

**起始版本：** 19