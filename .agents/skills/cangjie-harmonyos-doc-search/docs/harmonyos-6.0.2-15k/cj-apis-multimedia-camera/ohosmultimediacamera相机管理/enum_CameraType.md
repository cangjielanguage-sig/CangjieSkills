## enum CameraType

```cangjie
public enum CameraType <: Equatable<CameraType> & ToString {
    | CAMERA_TYPE_DEFAULT
    | CAMERA_TYPE_WIDE_ANGLE
    | CAMERA_TYPE_ULTRA_WIDE
    | CAMERA_TYPE_TELEPHOTO
    | CAMERA_TYPE_TRUE_DEPTH
    | ...
}
```

**功能：** 相机类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<CameraType>
- ToString

### CAMERA_TYPE_DEFAULT

```cangjie
CAMERA_TYPE_DEFAULT
```

**功能：** 相机类型未指定。

**起始版本：** 19

### CAMERA_TYPE_TELEPHOTO

```cangjie
CAMERA_TYPE_TELEPHOTO
```

**功能：** 长焦相机。

**起始版本：** 19

### CAMERA_TYPE_TRUE_DEPTH

```cangjie
CAMERA_TYPE_TRUE_DEPTH
```

**功能：** 带景深信息的相机。

**起始版本：** 19

### CAMERA_TYPE_ULTRA_WIDE

```cangjie
CAMERA_TYPE_ULTRA_WIDE
```

**功能：** 超广角相机。

**起始版本：** 19

### CAMERA_TYPE_WIDE_ANGLE

```cangjie
CAMERA_TYPE_WIDE_ANGLE
```

**功能：** 广角相机。

**起始版本：** 19

### func !=(CameraType)

```cangjie
public operator func !=(other: CameraType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraType](#enum-cameratype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CameraType)

```cangjie
public operator func ==(other: CameraType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraType](#enum-cameratype)|是|-|另一个枚举值。|

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