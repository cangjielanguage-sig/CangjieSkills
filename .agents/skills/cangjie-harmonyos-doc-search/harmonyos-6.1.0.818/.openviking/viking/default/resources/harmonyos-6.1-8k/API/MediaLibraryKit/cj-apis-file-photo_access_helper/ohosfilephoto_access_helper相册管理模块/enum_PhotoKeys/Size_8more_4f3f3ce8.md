### Size

```cangjie
Size
```

**功能：** 文件大小（单位：字节）。动态照片的size包括图片和视频的总大小。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### ThumbnailSize

```cangjie
ThumbnailSize
```

**功能：** THUMB图片的宽高，值为width:height拼接而成的字符串。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### Title

```cangjie
Title
```

**功能：** 文件标题。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### Uri

```cangjie
Uri
```

**功能：** 文件uri。

注意：查询照片时，该字段仅支持使用[DataSharePredicates.equalTo](../ArkData/cj-apis-data_share_predicates.md#func-equaltostring-vbvaluetype)谓词。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### Width

```cangjie
Width
```

**功能：** 图片宽度（单位：像素）。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func !=(PhotoKeys)

```cangjie
public operator func !=(other: PhotoKeys): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoKeys](#enum-photokeys)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PhotoKeys)

```cangjie
public operator func ==(other: PhotoKeys): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoKeys](#enum-photokeys)|是|-|另一个枚举值。|

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