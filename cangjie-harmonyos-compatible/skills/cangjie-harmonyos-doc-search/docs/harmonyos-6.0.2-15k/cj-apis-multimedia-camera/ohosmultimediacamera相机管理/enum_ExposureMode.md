## enum ExposureMode

```cangjie
public enum ExposureMode <: Equatable<ExposureMode> & ToString {
    | EXPOSURE_MODE_LOCKED
    | EXPOSURE_MODE_AUTO
    | EXPOSURE_MODE_CONTINUOUS_AUTO
    | EXPOSURE_MODE_UNKNOWN
    | ...
}
```

**功能：** 曝光模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<ExposureMode>
- ToString

### EXPOSURE_MODE_AUTO

```cangjie
EXPOSURE_MODE_AUTO
```

**功能：** 自动曝光模式。支持曝光区域中心点设置，可以使用[AutoExposure.setMeteringPoint](#func-setmeteringpointpoint)设置曝光区域中心点。

**起始版本：** 19

### EXPOSURE_MODE_CONTINUOUS_AUTO

```cangjie
EXPOSURE_MODE_CONTINUOUS_AUTO
```

**功能：** 连续自动曝光。不支持曝光区域中心点设置。

**起始版本：** 19

### EXPOSURE_MODE_LOCKED

```cangjie
EXPOSURE_MODE_LOCKED
```

**功能：** 锁定曝光模式。不支持曝光区域中心点设置。

**起始版本：** 19

### EXPOSURE_MODE_UNKNOWN

```cangjie
EXPOSURE_MODE_UNKNOWN
```

**功能：** 未知曝光模式。

**起始版本：** 19

### func !=(ExposureMode)

```cangjie
public operator func !=(other: ExposureMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ExposureMode](#enum-exposuremode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ExposureMode)

```cangjie
public operator func ==(other: ExposureMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ExposureMode](#enum-exposuremode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|