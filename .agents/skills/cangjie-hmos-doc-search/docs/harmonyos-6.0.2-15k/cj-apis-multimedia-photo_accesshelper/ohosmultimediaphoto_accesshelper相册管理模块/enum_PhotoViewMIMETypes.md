## enum PhotoViewMIMETypes

```cangjie
public enum PhotoViewMIMETypes <: Equatable<PhotoViewMIMETypes> & ToString {
    | IMAGE_TYPE
    | VIDEO_TYPE
    | IMAGE_VIDEO_TYPE
    | MOVING_PHOTO_IMAGE_TYPE
    | ...
}
```

**功能：** 可选择的媒体文件类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- Equatable\<PhotoViewMIMETypes>
- ToString

### IMAGE_TYPE

```cangjie
IMAGE_TYPE
```

**功能：** 图片类型。

**起始版本：** 19

### IMAGE_VIDEO_TYPE

```cangjie
IMAGE_VIDEO_TYPE
```

**功能：** 图片和视频类型。

**起始版本：** 19

### MOVING_PHOTO_IMAGE_TYPE

```cangjie
MOVING_PHOTO_IMAGE_TYPE
```

**功能：** 动态照片类型。

**起始版本：** 19

### VIDEO_TYPE

```cangjie
VIDEO_TYPE
```

**功能：** 视频类型。

**起始版本：** 19

### func !=(PhotoViewMIMETypes)

```cangjie
public operator func !=(other: PhotoViewMIMETypes): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoViewMIMETypes](#enum-photoviewmimetypes)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PhotoViewMIMETypes)

```cangjie
public operator func ==(other: PhotoViewMIMETypes): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoViewMIMETypes](#enum-photoviewmimetypes)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|