## enum UserActivityScenario

```cangjie
public enum UserActivityScenario {
    | NAVIGATION
    | SPORT
    | TRANSPORT
    | DAILY_LIFE_SERVICE
    | ...
}
```

**功能：** 位置请求中的用户活动场景类型。

> **说明：**
>
> 当使用NAVIGATION/SPORT/TRANSPORT场景进行单次定位或持续定位时，我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务；在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。

**系统能力：** SystemCapability.Location.Location.Core

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

### SPORT

```cangjie
SPORT
```

**功能：** 表示运动场景。

适用于记录用户位置轨迹的场景，如运动类应用记录轨迹功能。

主要使用GNSS定位技术提供定位服务，功耗较高。

**起始版本：** 19

### TRANSPORT

```cangjie
TRANSPORT
```

**功能：** 表示出行场景。

适用于用户出行场景，如打车、乘坐公共交通等场景。

主要使用GNSS定位技术提供定位服务，功耗较高。

**起始版本：** 19