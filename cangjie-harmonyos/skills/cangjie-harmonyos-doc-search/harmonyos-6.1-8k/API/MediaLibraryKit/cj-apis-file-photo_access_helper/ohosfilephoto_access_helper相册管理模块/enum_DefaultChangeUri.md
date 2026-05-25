## enum DefaultChangeUri

```cangjie
public enum DefaultChangeUri <: ToString {
    | DefaultPhotoUri
    | DefaultAlbumUri
    | ...
}
```

**功能：** 枚举，DefaultChangeUri子类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- ToString

### DefaultAlbumUri

```cangjie
DefaultAlbumUri
```

**功能：** 默认相册的uri，与forChildUris{true}一起使用，将接收所有相册的更改通知。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### DefaultPhotoUri

```cangjie
DefaultPhotoUri
```

**功能：** 默认PhotoAsset的uri，与forChildUris{true}一起使用，将接收所有PhotoAsset的更改通知。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func !=(DefaultChangeUri)

```cangjie
public operator func !=(other: DefaultChangeUri): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DefaultChangeUri](#enum-defaultchangeuri)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(DefaultChangeUri)

```cangjie
public operator func ==(other: DefaultChangeUri): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DefaultChangeUri](#enum-defaultchangeuri)|是|-|另一个枚举值。|

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