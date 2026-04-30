## enum LocationRequestPriority

```cangjie
public enum LocationRequestPriority {
    | UNSET
    | ACCURACY
    | LOW_POWER
    | FIRST_FIX
    | ...
}
```

**功能：** 位置请求中位置信息优先级类型。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### ACCURACY

```cangjie
ACCURACY
```

**功能：** 表示精度优先。

定位精度优先策略主要以GNSS定位技术为主。我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务。在持续定位过程中，如果超过30秒无法获取GNSS定位结果则使用网络定位技术。对设备的硬件资源消耗较大，功耗较大。

**起始版本：** 19

### FIRST_FIX

```cangjie
FIRST_FIX
```

**功能：** 表示快速获取位置优先，如果应用希望快速拿到一个位置，可以将优先级设置为该字段。

快速定位优先策略会同时使用GNSS定位和网络定位技术，以便在室内和户外场景下均可以快速获取到位置结果；当各种定位技术都有提供位置结果时，系统会选择其中精度较好的结果返回给应用。因为对各种定位技术同时使用，对设备的硬件资源消耗较大，功耗也较大。

**起始版本：** 19

### LOW_POWER

```cangjie
LOW_POWER
```

**功能：** 表示低功耗优先。

低功耗定位优先策略仅使用网络定位技术，在室内和户外场景均可提供定位服务，因为其依赖周边基站、可见WLAN、蓝牙设备的分布情况，定位结果的精度波动范围较大，推荐在对定位结果精度要求不高的场景下使用该策略，可以有效节省设备功耗。

**起始版本：** 19

### UNSET

```cangjie
UNSET
```

**功能：** 表示未设置优先级，表示[LocationRequestPriority](#enum-locationrequestpriority)无效。

**起始版本：** 19

## enum LocationRequestScenario

```cangjie
public enum LocationRequestScenario {
    | UNSET
    | NAVIGATION
    | TRAJECTORY_TRACKING
    | CAR_HAILING
    | DAILY_LIFE_SERVICE
    | NO_POWER
    | ...
}
```

**功能：** 位置请求中定位场景类型。

> **说明：**
>
> 当使用NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING场景进行单次定位或持续定位时，我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务；在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### CAR_HAILING

```cangjie
CAR_HAILING
```

**功能：** 表示打车场景。

适用于用户出行打车时定位当前位置的场景，如网约车类应用。

主要使用GNSS定位技术提供定位服务，功耗较高。

**起始版本：** 19

### DAILY_LIFE_SERVICE

```cangjie
DAILY_LIFE_SERVICE
```

**功能：** 表示日常服务使用场景。

适用于不需要定位用户精确位置的使用场景，如新闻资讯、网购、点餐类应用。

该场景仅使用网络定位技术提供定位服务，功耗较低。

**起始版本：** 19

### NAVIGATION

```cangjie
NAVIGATION
```

**功能：** 表示导航场景。

适用于在户外获取设备实时位置的场景，如车载、步行导航。

主要使用GNSS定位技术提供定位服务，功耗较高。

**起始版本：** 19

### NO_POWER

```cangjie
NO_POWER
```

**功能：** 表示无功耗功场景，这种场景下不会主动触发定位，会在其他应用定位时，才给当前应用返回位置。

**起始版本：** 19

### TRAJECTORY_TRACKING

```cangjie
TRAJECTORY_TRACKING
```

**功能：** 表示运动轨迹记录场景。

适用于记录用户位置轨迹的场景，如运动类应用记录轨迹功能。

主要使用GNSS定位技术提供定位服务，功耗较高。

**起始版本：** 19

### UNSET

```cangjie
UNSET
```

**功能：** 表示未设置场景信息。

表示[LocationRequestScenario](#enum-locationrequestscenario)字段无效。

**起始版本：** 19