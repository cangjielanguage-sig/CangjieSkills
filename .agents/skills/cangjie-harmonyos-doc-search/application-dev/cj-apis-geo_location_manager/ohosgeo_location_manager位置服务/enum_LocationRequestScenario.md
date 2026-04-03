## enum LocationRequestScenario

```cangjie
public enum LocationRequestScenario {
    | Unset
    | Navigation
    | TrajectoryTracking
    | CarHailing
    | DailyLifeService
    | NoPower
    | ...
}
```

**功能：** 位置请求中定位场景类型。

> **说明：**
>
> 当使用NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING场景进行单次定位或持续定位时，会在GNSS提供稳定位置结果之前使用网络定位技术提供服务；在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### CarHailing

```cangjie
CarHailing
```

**功能：** 表示打车场景。

适用于用户出行打车时定位当前位置的场景，如网约车类应用。

主要使用GNSS定位技术提供定位服务，功耗较高。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### DailyLifeService

```cangjie
DailyLifeService
```

**功能：** 表示日常服务使用场景。

适用于不需要定位用户精确位置的使用场景，如新闻资讯、网购、点餐类应用。

该场景仅使用网络定位技术提供定位服务，功耗较低。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### Navigation

```cangjie
Navigation
```

**功能：** 表示导航场景。

适用于在户外获取设备实时位置的场景，如车载、步行导航。

主要使用GNSS定位技术提供定位服务，功耗较高。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### NoPower

```cangjie
NoPower
```

**功能：** 表示无功耗功场景，这种场景下不会主动触发定位，会在其他应用定位时，才给当前应用返回位置。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### TrajectoryTracking

```cangjie
TrajectoryTracking
```

**功能：** 表示运动轨迹记录场景。

适用于记录用户位置轨迹的场景，如运动类应用记录轨迹功能。

主要使用GNSS定位技术提供定位服务，功耗较高。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### Unset

```cangjie
Unset
```

**功能：** 表示未设置场景信息。

表示[LocationRequestScenario](#enum-locationrequestscenario)字段无效。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22