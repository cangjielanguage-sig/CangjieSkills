## enum DefaultChangeUri

```cangjie
public enum DefaultChangeUri <: ToString & Equatable<DefaultChangeUri> {
    | DEFAULT_PHOTO_URI
    | DEFAULT_ALBUM_URI
    | ...
}
```

**功能：** DefaultChangeUri子类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<DefaultChangeUri>

### DEFAULT_ALBUM_URI

```cangjie
DEFAULT_ALBUM_URI
```

**功能：** 默认相册的Uri，与forSubUri{true}一起使用，将接收所有相册的更改通知。

**起始版本：** 19

### DEFAULT_PHOTO_URI

```cangjie
DEFAULT_PHOTO_URI
```

**功能：** 默认PhotoAsset的Uri，与forSubUri{true}一起使用，将接收所有PhotoAsset的更改通知。

**起始版本：** 19

### func !=(DefaultChangeUri)

```cangjie
public operator func !=(other: DefaultChangeUri): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

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

**起始版本：** 19

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

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|