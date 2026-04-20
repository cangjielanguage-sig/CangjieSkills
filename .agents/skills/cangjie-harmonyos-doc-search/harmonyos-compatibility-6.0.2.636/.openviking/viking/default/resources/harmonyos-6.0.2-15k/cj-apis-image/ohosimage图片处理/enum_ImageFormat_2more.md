## enum ImageFormat

```cangjie
public enum ImageFormat <: Equatable<ImageFormat> & ToString {
    | YCBCR_422_SP
    | JPEG
    | ...
}
```

**功能：** 图片格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**父类型：**

- Equatable\<ImageFormat>
- ToString

### JPEG

```cangjie
JPEG
```

**功能：** JPEG编码格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### YCBCR_422_SP

```cangjie
YCBCR_422_SP
```

**功能：** YCBCR422半平面格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### func !=(ImageFormat)

```cangjie
public operator func !=(other: ImageFormat): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageFormat](#enum-imageformat)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ImageFormat)

```cangjie
public operator func ==(other: ImageFormat): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageFormat](#enum-imageformat)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|

## enum MetadataType

```cangjie
public enum MetadataType <: Equatable<MetadataType> & ToString {
    EXIF_METADATA |
    FRAGMENT_METADATA |
    ...
}
```

**功能：** 枚举，图片元数据类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

**父类型：**

- Equatable\<MetadataType>
- ToString

### EXIF_METADATA

```cangjie
EXIF_METADATA
```

**功能：** exif数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

### FRAGMENT_METADATA

```cangjie
FRAGMENT_METADATA
```

**功能：** 水印裁剪图元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20