## enum ExposureMode

```cangjie
public enum ExposureMode {
    | ExposureModeLocked
    | ExposureModeAuto
    | ExposureModeContinuousAuto
    | ...
}
```

**功能：** 枚举，曝光模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<ExposureMode>
- ToString

### ExposureModeAuto

```cangjie
ExposureModeAuto
```

**功能：** 自动曝光模式。支持曝光区域中心点设置，可以使用[AutoExposure.setMeteringPoint](#func-setmeteringpointpoint)设置曝光区域中心点。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### ExposureModeContinuousAuto

```cangjie
ExposureModeContinuousAuto
```

**功能：** 连续自动曝光。不支持曝光区域中心点设置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### ExposureModeLocked

```cangjie
ExposureModeLocked
```

**功能：** 锁定曝光模式。不支持曝光区域中心点设置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(ExposureMode)

```cangjie
public operator func !=(other: ExposureMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

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

**起始版本：** 22

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

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|