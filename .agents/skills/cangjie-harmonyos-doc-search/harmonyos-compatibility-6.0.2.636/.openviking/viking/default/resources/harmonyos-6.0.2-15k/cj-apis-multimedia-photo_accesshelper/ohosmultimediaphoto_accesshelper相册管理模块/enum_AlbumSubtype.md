## enum AlbumSubtype

```cangjie
public enum AlbumSubtype <: Equatable<AlbumSubtype> & ToString {
    | USER_GENERIC
    | FAVORITE
    | VIDEO
    | IMAGE
    | ANY
    | UNKNOWN
    | ...
}
```

**功能：** 相册子类型，表示具体的相册类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- Equatable\<AlbumSubtype>
- ToString

### ANY

```cangjie
ANY
```

**功能：** 任意相册。

**起始版本：** 19

### FAVORITE

```cangjie
FAVORITE
```

**功能：** 收藏夹。

**起始版本：** 19

### IMAGE

```cangjie
IMAGE
```

**功能：** 图片相册。

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知相册子类型。

**起始版本：** 19

### USER_GENERIC

```cangjie
USER_GENERIC
```

**功能：** 用户相册。

**起始版本：** 19

### VIDEO

```cangjie
VIDEO
```

**功能：** 视频相册。

**起始版本：** 19

### func !=(AlbumSubtype)

```cangjie
public operator func !=(other: AlbumSubtype): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AlbumSubtype](#enum-albumsubtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(AlbumSubtype)

```cangjie
public operator func ==(other: AlbumSubtype): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AlbumSubtype](#enum-albumsubtype)|是|-|另一个枚举值。|

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