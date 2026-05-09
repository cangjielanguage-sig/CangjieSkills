## enum PhotoViewMimeTypes

```cangjie
public enum PhotoViewMimeTypes <: Equatable<PhotoViewMimeTypes> & ToString {
    | ImageType
    | VideoType
    | ImageVideoType
    | MovingPhotoImageType
    | ...
}
```

**功能：** 枚举，可选择的媒体文件类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- Equatable\<PhotoViewMimeTypes>
- ToString

### ImageType

```cangjie
ImageType
```

**功能：** 图片类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### ImageVideoType

```cangjie
ImageVideoType
```

**功能：** 图片和视频类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### MovingPhotoImageType

```cangjie
MovingPhotoImageType
```

**功能：** 动态照片类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### VideoType

```cangjie
VideoType
```

**功能：** 视频类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func !=(PhotoViewMimeTypes)

```cangjie
public operator func !=(other: PhotoViewMimeTypes): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoViewMimeTypes](#enum-photoviewmimetypes)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PhotoViewMimeTypes)

```cangjie
public operator func ==(other: PhotoViewMimeTypes): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoViewMimeTypes](#enum-photoviewmimetypes)|是|-|另一个枚举值。|

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|