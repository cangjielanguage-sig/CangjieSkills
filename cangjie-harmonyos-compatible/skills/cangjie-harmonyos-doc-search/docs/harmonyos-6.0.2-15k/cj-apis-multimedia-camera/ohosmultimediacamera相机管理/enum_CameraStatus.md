## enum CameraStatus

```cangjie
public enum CameraStatus <: Equatable<CameraStatus> & ToString {
    | CAMERA_STATUS_APPEAR
    | CAMERA_STATUS_DISAPPEAR
    | CAMERA_STATUS_AVAILABLE
    | CAMERA_STATUS_UNAVAILABL
    | ...
}
```

**功能：** 相机状态。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<CameraStatus>
- ToString

### CAMERA_STATUS_APPEAR

```cangjie
CAMERA_STATUS_APPEAR
```

**功能：** 新的相机出现。

**起始版本：** 19

### CAMERA_STATUS_AVAILABLE

```cangjie
CAMERA_STATUS_AVAILABLE
```

**功能：** 相机可用。

**起始版本：** 19

### CAMERA_STATUS_DISAPPEAR

```cangjie
CAMERA_STATUS_DISAPPEAR
```

**功能：** 相机被移除。

**起始版本：** 19

### CAMERA_STATUS_UNAVAILABL

```cangjie
CAMERA_STATUS_UNAVAILABL
```

**功能：** 相机不可用。

**起始版本：** 19

### func !=(CameraStatus)

```cangjie
public operator func !=(other: CameraStatus): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraStatus](#enum-camerastatus)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CameraStatus)

```cangjie
public operator func ==(other: CameraStatus): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraStatus](#enum-camerastatus)|是|-|另一个枚举值。|

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