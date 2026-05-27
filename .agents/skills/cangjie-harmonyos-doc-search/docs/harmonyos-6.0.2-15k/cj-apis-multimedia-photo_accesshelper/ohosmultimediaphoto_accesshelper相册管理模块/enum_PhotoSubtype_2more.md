## enum PhotoSubtype

```cangjie
public enum PhotoSubtype <: Equatable<PhotoSubtype> & ToString {
    | DEFAULT
    | MOVING_PHOTO
    | BURST
    | ...
}
```

**功能：** 连拍照片文件类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- Equatable\<PhotoSubtype>
- ToString

### BURST

```cangjie
BURST
```

**功能：** 连拍照片文件类型。

**起始版本：** 19

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 默认照片类型。

**起始版本：** 19

### MOVING_PHOTO

```cangjie
MOVING_PHOTO
```

**功能：** 动态照片文件类型。

**起始版本：** 19

### func !=(PhotoSubtype)

```cangjie
public operator func !=(other: PhotoSubtype): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoSubtype](#enum-photosubtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PhotoSubtype)

```cangjie
public operator func ==(other: PhotoSubtype): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoSubtype](#enum-photosubtype)|是|-|另一个枚举值。|

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

## enum PhotoType

```cangjie
public enum PhotoType <: Equatable<PhotoType> & ToString {
    | IMAGE
    | VIDEO
    | ...
}
```

**功能：** 媒体文件类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- Equatable\<PhotoType>
- ToString

### IMAGE

```cangjie
IMAGE
```

**功能：** 图片。

**起始版本：** 19

### VIDEO

```cangjie
VIDEO
```

**功能：** 视频。

**起始版本：** 19

### func !=(PhotoType)

```cangjie
public operator func !=(other: PhotoType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoType](#enum-phototype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PhotoType)

```cangjie
public operator func ==(other: PhotoType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoType](#enum-phototype)|是|-|另一个枚举值。|

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