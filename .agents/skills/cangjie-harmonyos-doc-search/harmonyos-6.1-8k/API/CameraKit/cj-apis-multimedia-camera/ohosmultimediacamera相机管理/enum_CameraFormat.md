## enum CameraFormat

```cangjie
public enum CameraFormat {
    | CameraFormatRgba8888
    | CameraFormatYuv420Sp
    | CameraFormatJpeg
    | CameraFormatYcbcrP010
    | CameraFormatYcrcbP010
    | CameraFormatHeic
    | ...
}
```

**功能：** 枚举，输出格式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraFormatHeic

```cangjie
CameraFormatHeic
```

**功能：** HEIF格式的图片。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraFormatJpeg

```cangjie
CameraFormatJpeg
```

**功能：** JPEG格式的图片。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraFormatRgba8888

```cangjie
CameraFormatRgba8888
```

**功能：** RGBA_8888格式的图片。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraFormatYcbcrP010

```cangjie
CameraFormatYcbcrP010
```

**功能：** YCBCR_P010格式的图片。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraFormatYcrcbP010

```cangjie
CameraFormatYcrcbP010
```

**功能：** YCRCB_P010格式的图片。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraFormatYuv420Sp

```cangjie
CameraFormatYuv420Sp
```

**功能：** YUV_420_SP格式的图片。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(CameraFormat)

```cangjie
public operator func !=(other: CameraFormat): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

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

**起始版本：** 22

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

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|