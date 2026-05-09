## enum PhotoKeys

```cangjie
public enum PhotoKeys <: ToString {
    | Uri
    | PhotoType
    | DisplayName
    | Size
    | DateAdded
    | DateModified
    | Duration
    | Width
    | Height
    | DateTaken
    | Orientation
    | Favorite
    | Title
    | DateAddedMs
    | DateModifiedMs
    | PhotoSubtype
    | DynamicRangeType
    | CoverPosition
    | BurstKey
    | LcdSize
    | ThumbnailSize
    | ...
}
```

**功能：** 枚举，图片和视频文件关键信息。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- ToString

### BurstKey

```cangjie
BurstKey
```

**功能：** 一组连拍照片的唯一标识：uuid。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### CoverPosition

```cangjie
CoverPosition
```

**功能：** 动态照片的封面位置，具体表示封面帧所对应的视频时间戳（单位：微秒）。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### DateAdded

```cangjie
DateAdded
```

**功能：** 文件创建时的Unix时间戳（单位：秒）。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### DateAddedMs

```cangjie
DateAddedMs
```

**功能：** 文件创建时的Unix时间戳（单位：毫秒）。

注意：查询照片时，不支持基于该字段排序。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### DateModified

```cangjie
DateModified
```

**功能：** 文件修改时的Unix时间戳（单位：秒）。修改文件名不会改变此值，当文件内容发生修改时才会更新。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### DateModifiedMs

```cangjie
DateModifiedMs
```

**功能：** 文件修改时的Unix时间戳（单位：毫秒）。修改文件名不会改变此值，当文件内容发生修改时才会更新。

注意：查询照片时，不支持基于该字段排序。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### DateTaken

```cangjie
DateTaken
```

**功能：** 拍摄时的Unix时间戳（单位：秒）。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### DisplayName

```cangjie
DisplayName
```

**功能：** 显示名字。规格为：

- 应包含有效文件主名和图片或视频扩展名。

- 文件名字符串长度为1~255。

- 文件主名中不允许出现的非法英文字符，包括：. .. \ / : * ? " ' ` < > \| { } [ ]

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### Duration

```cangjie
Duration
```

**功能：** 持续时间（单位：毫秒）。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### DynamicRangeType

```cangjie
DynamicRangeType
```

**功能：** 媒体文件的动态范围类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### Favorite

```cangjie
Favorite
```

**功能：** 收藏。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### Height

```cangjie
Height
```

**功能：** 图片高度（单位：像素）。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### LcdSize

```cangjie
LcdSize
```

**功能：** LCD图片的宽高，值为width:height拼接而成的字符串。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### Orientation

```cangjie
Orientation
```

**功能：** 文件的旋转角度，单位为度。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### PhotoSubtype

```cangjie
PhotoSubtype
```

**功能：** 媒体文件的子类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### PhotoType

```cangjie
PhotoType
```

**功能：** 媒体文件类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22