## enum LocationSourceType

```cangjie
public enum LocationSourceType {
    | GNSS
    | NETWORK
    | INDOOR
    | RTK
    | ...
}
```

**功能：** 定位结果的来源。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### GNSS

```cangjie
GNSS
```

**功能：** 表示定位结果来自于GNSS定位技术。

**起始版本：** 19

### INDOOR

```cangjie
INDOOR
```

**功能：** 表示定位结果来自于室内高精度定位技术。

**起始版本：** 19

### NETWORK

```cangjie
NETWORK
```

**功能：** 表示定位结果来自于网络定位技术。

**起始版本：** 19

### RTK

```cangjie
RTK
```

**功能：** 表示定位结果来自于室外高精度定位技术。

**起始版本：** 19

## enum PowerConsumptionScenario

```cangjie
public enum PowerConsumptionScenario {
    | HIGH_POWER_CONSUMPTION
    | LOW_POWER_CONSUMPTION
    | NO_POWER_CONSUMPTION
    | ...
}
```

**功能：** 位置请求中的功耗场景类型。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### HIGH_POWER_CONSUMPTION

```cangjie
HIGH_POWER_CONSUMPTION
```

**功能：** 高功耗。

以GNSS定位技术为主。我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务；在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。对设备的硬件资源消耗较大，功耗较大。

**起始版本：** 19

### LOW_POWER_CONSUMPTION

```cangjie
LOW_POWER_CONSUMPTION
```

**功能：** 低功耗。

适用于对用户位置精度要求不高的使用场景，如新闻资讯、网购、点餐类应用。

该场景仅使用网络定位技术提供定位服务，功耗较低。

**起始版本：** 19

### NO_POWER_CONSUMPTION

```cangjie
NO_POWER_CONSUMPTION
```

**功能：** 无功耗。

这种场景下不会主动触发定位，会在其他应用定位时，才给当前应用返回位置。

**起始版本：** 19

## enum SatelliteAdditionalInfo

```cangjie
public enum SatelliteAdditionalInfo {
    | SATELLITES_ADDITIONAL_INFO_NULL
    | SATELLITES_ADDITIONAL_INFO_EPHEMERIS_DATA_EXIST
    | SATELLITES_ADDITIONAL_INFO_ALMANAC_DATA_EXIST
    | SATELLITES_ADDITIONAL_INFO_USED_IN_FIX
    | SATELLITES_ADDITIONAL_INFO_CARRIER_FREQUENCY_EXIST
    | ...
}
```

**功能：** 卫星附加信息类型。

**系统能力：** SystemCapability.Location.Location.Gnss

**起始版本：** 19

### SATELLITES_ADDITIONAL_INFO_ALMANAC_DATA_EXIST

```cangjie
SATELLITES_ADDITIONAL_INFO_ALMANAC_DATA_EXIST
```

**功能：** 表示本卫星具有年历数据。

**起始版本：** 19

### SATELLITES_ADDITIONAL_INFO_CARRIER_FREQUENCY_EXIST

```cangjie
SATELLITES_ADDITIONAL_INFO_CARRIER_FREQUENCY_EXIST
```

**功能：** 表示本卫星具有载波频率。

**起始版本：** 19

### SATELLITES_ADDITIONAL_INFO_EPHEMERIS_DATA_EXIST

```cangjie
SATELLITES_ADDITIONAL_INFO_EPHEMERIS_DATA_EXIST
```

**功能：** 表示本卫星具有星历数据。

**起始版本：** 19

### SATELLITES_ADDITIONAL_INFO_NULL

```cangjie
SATELLITES_ADDITIONAL_INFO_NULL
```

**功能：** 默认值。

**起始版本：** 19

### SATELLITES_ADDITIONAL_INFO_USED_IN_FIX

```cangjie
SATELLITES_ADDITIONAL_INFO_USED_IN_FIX
```

**功能：** 表示在最新的位置解算中使用了本卫星。

**起始版本：** 19