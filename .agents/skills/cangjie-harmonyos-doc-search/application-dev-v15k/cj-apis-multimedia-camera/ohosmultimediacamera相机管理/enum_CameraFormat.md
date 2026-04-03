## enum CameraFormat

```cangjie
public enum CameraFormat <: Equatable<CameraFormat> & ToString {
    | CAMERA_FORMAT_YCRCB_P010
    | CAMERA_FORMAT_YCBCR_P010
    | CAMERA_FORMAT_HEIC
    | CAMERA_FORMAT_JPEG
    | CAMERA_FORMAT_YUV_420_SP
    | CAMERA_FORMAT_RGBA_8888
    | CAMERA_FORMAT_UNKNOWN
    | ...
}
```

**功能：** 输出格式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<CameraFormat>
- ToString

### CAMERA_FORMAT_HEIC

```cangjie
CAMERA_FORMAT_HEIC
```

**功能：** HEIF格式的图片。

**起始版本：** 19

### CAMERA_FORMAT_JPEG

```cangjie
CAMERA_FORMAT_JPEG
```

**功能：** JPEG格式的图片。

**起始版本：** 19

### CAMERA_FORMAT_RGBA_8888

```cangjie
CAMERA_FORMAT_RGBA_8888
```

**功能：** RGBA_888格式的图片。

**起始版本：** 19

### CAMERA_FORMAT_YCBCR_P010

```cangjie
CAMERA_FORMAT_YCBCR_P010
```

**功能：** YCBCR_P010格式的图片。

**起始版本：** 19

### CAMERA_FORMAT_YCRCB_P010

```cangjie
CAMERA_FORMAT_YCRCB_P010
```

**功能：** YCRCB_P010格式的图片。

**起始版本：** 19

### CAMERA_FORMAT_YUV_420_SP

```cangjie
CAMERA_FORMAT_YUV_420_SP
```

**功能：** YUV_420_SP格式的图片。

**起始版本：** 19

### CAMERA_FORMAT_UNKNOWN

```cangjie
CAMERA_FORMAT_UNKNOWN
```

**功能：** 未知格式的图片。

**起始版本：** 19

### func !=(CameraFormat)

```cangjie
public operator func !=(other: CameraFormat): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraFormat](#enum-cameraformat)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CameraFormat)

```cangjie
public operator func ==(other: CameraFormat): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraFormat](#enum-cameraformat)|是|-|另一个枚举值。|

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