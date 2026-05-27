# ohos.geo_location_manager（位置服务）

位置服务提供GNSS定位、网络定位（蜂窝基站、WLAN、蓝牙定位技术）、地理编码、逆地理编码、国家码和地理围栏等基本功能。

> **说明：**
>
> 本模块能力仅支持WGS-84坐标系。

## 导入模块

```cangjie
import kit.LocationKit.*
```

## 权限列表

应用在使用Location Kit系统能力前，需要检查是否已经获取用户授权访问设备位置信息。如未获得授权，可以向用户申请需要的位置权限。

系统提供的定位权限有：

ohos.permission.APPROXIMATELY_LOCATION：用于获取模糊位置，精确度为5公里。

ohos.permission.LOCATION：用于获取精准位置，精准度在米级别。

ohos.permission.LOCATION_IN_BACKGROUND：用于应用切换到后台仍然需要获取定位信息的场景。

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class CachedGnssLocationsRequest

```cangjie
public class CachedGnssLocationsRequest {
    public var reportingPeriodSec: Int32
    public var wakeUpCacheQueueFull: Bool
    public init(reportingPeriodSec: Int32, wakeUpCacheQueueFull: Bool)
}
```

**功能：** 请求订阅GNSS缓存位置上报功能接口的配置参数。

**系统能力：** SystemCapability.Location.Location.Gnss

**起始版本：** 19

### var reportingPeriodSec

```cangjie
public var reportingPeriodSec: Int32
```

**功能：** 表示GNSS缓存位置上报的周期，单位是毫秒。取值范围为大于0。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var wakeUpCacheQueueFull

```cangjie
public var wakeUpCacheQueueFull: Bool
```

**功能：** true表示GNSS芯片底层缓存队列满之后会主动唤醒AP芯片，并把缓存位置上报给应用。

false表示GNSS芯片底层缓存队列满之后不会主动唤醒AP芯片，会把缓存位置直接丢弃。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### init(Int32, Bool)

```cangjie
public init(reportingPeriodSec: Int32, wakeUpCacheQueueFull: Bool)
```

**功能：** 构造CachedGnssLocationsRequest对象。

**系统能力：** SystemCapability.Location.Location.Gnss

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|reportingPeriodSec|Int32|是|-|表示GNSS缓存位置上报的周期，单位是毫秒。取值范围为大于0。|
|wakeUpCacheQueueFull|Bool|是|-|true表示GNSS芯片底层缓存队列满之后会主动唤醒AP芯片，并把缓存位置上报给应用；<br/>false表示GNSS芯片底层缓存队列满之后不会主动唤醒AP芯片，会把缓存位置直接丢弃。|