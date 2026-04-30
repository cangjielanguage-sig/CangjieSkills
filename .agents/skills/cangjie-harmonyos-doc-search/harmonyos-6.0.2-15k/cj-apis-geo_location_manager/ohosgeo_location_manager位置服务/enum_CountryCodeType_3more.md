## enum CountryCodeType

```cangjie
public enum CountryCodeType {
    | COUNTRY_CODE_FROM_LOCALE
    | COUNTRY_CODE_FROM_SIM
    | COUNTRY_CODE_FROM_LOCATION
    | COUNTRY_CODE_FROM_NETWORK
    | ...
}
```

**功能：** 国家码来源类型。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### COUNTRY_CODE_FROM_LOCALE

```cangjie
COUNTRY_CODE_FROM_LOCALE
```

**功能：** 从全球化模块的语言配置信息中获取到的国家码。

**起始版本：** 19

### COUNTRY_CODE_FROM_LOCATION

```cangjie
COUNTRY_CODE_FROM_LOCATION
```

**功能：** 基于用户的位置信息，通过逆地理编码查询到的国家码。

**起始版本：** 19

### COUNTRY_CODE_FROM_NETWORK

```cangjie
COUNTRY_CODE_FROM_NETWORK
```

**功能：** 从蜂窝网络注册信息中获取到的国家码。

**起始版本：** 19

### COUNTRY_CODE_FROM_SIM

```cangjie
COUNTRY_CODE_FROM_SIM
```

**功能：** 从SIM卡中获取到的国家码。

**起始版本：** 19

## enum LocatingPriority

```cangjie
public enum LocatingPriority {
    | PRIORITY_ACCURACY
    | PRIORITY_LOCATING_SPEED
    | ...
}
```

**功能：** 单次位置请求中的优先级类型。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### PRIORITY_ACCURACY

```cangjie
PRIORITY_ACCURACY
```

**功能：** 表示精度优先。

定位精度优先策略会同时使用GNSS定位和网络定位技术，并把一段时间内精度较好的结果返回给应用；这个时间段长度为[SingleLocationRequest](#class-singlelocationrequest).locatingTimeoutMs与“30秒”中的较小者。
对设备的硬件资源消耗较大，功耗较大。

**起始版本：** 19

### PRIORITY_LOCATING_SPEED

```cangjie
PRIORITY_LOCATING_SPEED
```

**功能：** 表示快速获取位置优先，如果应用希望快速拿到一个位置，可以将优先级设置为该类型。

快速定位优先策略会同时使用GNSS定位和网络定位技术，以便在室内和户外场景下均可以快速获取到位置结果，我们会把最先拿到的定位结果返回给应用。对设备的硬件资源消耗较大，功耗也较大。

**起始版本：** 19

## enum LocationError

```cangjie
public enum LocationError {
    | LOCATING_FAILED_DEFAULT
    | LOCATING_FAILED_LOCATION_PERMISSION_DENIED
    | LOCATING_FAILED_BACKGROUND_PERMISSION_DENIED
    | LOCATING_FAILED_LOCATION_SWITCH_OFF
    | LOCATING_FAILED_INTERNET_ACCESS_FAILURE
    | ...
}
```

**功能：** 持续定位过程中的错误信息。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### LOCATING_FAILED_BACKGROUND_PERMISSION_DENIED

```cangjie
LOCATING_FAILED_BACKGROUND_PERMISSION_DENIED
```

**功能：** 表示应用在后台时位置权限校验失败导致持续定位失败。APP在后台定位时的位置权限申请方式参见[申请位置权限开发指导](../../../../Dev_Guide/location/cj-location-permission-guidelines.md)。

**起始版本：** 19

### LOCATING_FAILED_DEFAULT

```cangjie
LOCATING_FAILED_DEFAULT
```

**功能：** 默认值。

**起始版本：** 19

### LOCATING_FAILED_INTERNET_ACCESS_FAILURE

```cangjie
LOCATING_FAILED_INTERNET_ACCESS_FAILURE
```

**功能：** 表示无法访问网络，导致网络定位失败。

**起始版本：** 19

### LOCATING_FAILED_LOCATION_PERMISSION_DENIED

```cangjie
LOCATING_FAILED_LOCATION_PERMISSION_DENIED
```

**功能：** 表示ohos.permission.APPROXIMATELY_LOCATION权限或ohos.permission.LOCATION权限校验失败导致持续定位失败。

**起始版本：** 19

### LOCATING_FAILED_LOCATION_SWITCH_OFF

```cangjie
LOCATING_FAILED_LOCATION_SWITCH_OFF
```

**功能：** 表示位置信息开关关闭导致持续定位失败。

**起始版本：** 19