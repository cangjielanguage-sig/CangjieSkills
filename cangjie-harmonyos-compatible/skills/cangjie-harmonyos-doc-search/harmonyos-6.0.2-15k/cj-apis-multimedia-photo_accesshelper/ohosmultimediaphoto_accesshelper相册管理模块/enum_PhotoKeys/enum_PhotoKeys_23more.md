## enum PhotoKeys

```cangjie
public enum PhotoKeys <: ToString & Equatable<PhotoKeys> {
    | URI
    | PHOTO_TYPE
    | DISPLAY_NAME
    | SIZE
    | DATE_ADDED
    | DATE_MODIFIED
    | DURATION
    | WIDTH
    | HEIGHT
    | DATE_TAKEN
    | ORIENTATION
    | FAVORITE
    | TITLE
    | DATE_ADDED_MS
    | DATE_MODIFIED_MS
    | PHOTO_SUBTYPE
    | DYNAMIC_RANGE_TYPE
    | COVER_POSITION
    | BURST_KEY
    | LCD_SIZE
    | THM_SIZE
    | ...
}
```

**功能：** 图片和视频文件关键信息。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<PhotoKeys>

### BURST_KEY

```cangjie
BURST_KEY
```

**功能：** 一组连拍照片的唯一标识：uuid。

**起始版本：** 19

### COVER_POSITION

```cangjie
COVER_POSITION
```

**功能：** 动态照片的封面位置，具体表示封面帧所对应的视频时间戳（单位：微秒）。

**起始版本：** 19

### DATE_ADDED

```cangjie
DATE_ADDED
```

**功能：** 添加日期（添加文件时间距1970年1月1日的秒数值）。

**起始版本：** 19

### DATE_ADDED_MS

```cangjie
DATE_ADDED_MS
```

**功能：** 添加日期（添加文件时间距1970年1月1日的毫秒数值）。

注意：查询照片时，不支持基于该字段排序。

**起始版本：** 19

### DATE_MODIFIED

```cangjie
DATE_MODIFIED
```

**功能：** 修改日期（修改文件时间距1970年1月1日的秒数值，修改文件名不会改变此值，当文件内容发生修改时才会更新）。

**起始版本：** 19

### DATE_MODIFIED_MS

```cangjie
DATE_MODIFIED_MS
```

**功能：** 修改日期（修改文件时间距1970年1月1日的毫秒数值，修改文件名不会改变此值，当文件内容发生修改时才会更新）。

注意：查询照片时，不支持基于该字段排序。

**起始版本：** 19

### DATE_TAKEN

```cangjie
DATE_TAKEN
```

**功能：** 拍摄日期（文件拍照时间距1970年1月1日的秒数值）。

**起始版本：** 19

### DISPLAY_NAME

```cangjie
DISPLAY_NAME
```

**功能：** 显示名字。

**起始版本：** 19

### DURATION

```cangjie
DURATION
```

**功能：** 持续时间（单位：毫秒）。

**起始版本：** 19

### DYNAMIC_RANGE_TYPE

```cangjie
DYNAMIC_RANGE_TYPE
```

**功能：** 媒体文件的动态范围类型。

**起始版本：** 19

### FAVORITE

```cangjie
FAVORITE
```

**功能：** 收藏。

**起始版本：** 19

### HEIGHT

```cangjie
HEIGHT
```

**功能：** 图片高度（单位：像素）。

**起始版本：** 19

### LCD_SIZE

```cangjie
LCD_SIZE
```

**功能：** LCD图片的宽高，值为width:height拼接而成的字符串。

**起始版本：** 19

### ORIENTATION

```cangjie
ORIENTATION
```

**功能：** 文件的旋转角度，单位为度。

**起始版本：** 19

### PHOTO_SUBTYPE

```cangjie
PHOTO_SUBTYPE
```

**功能：** 媒体文件的动态范围类型。

**起始版本：** 19

### PHOTO_TYPE

```cangjie
PHOTO_TYPE
```

**功能：** 媒体文件类型。

**起始版本：** 19

### SIZE

```cangjie
SIZE
```

**功能：** 文件大小（单位：字节）。

**起始版本：** 19

### THM_SIZE

```cangjie
THM_SIZE
```

**功能：** THUMB图片的宽高，值为width:height拼接而成的字符串。

**起始版本：** 19

### TITLE

```cangjie
TITLE
```

**功能：** 文件标题。

**起始版本：** 19

### URI

```cangjie
URI
```

**功能：** 文件uri。

注意：查询照片时，该字段仅支持使用[DataSharePredicates.equalTo](../ArkData/cj-apis-data_share_predicates.md#func-equaltostring-valuetype)谓词。

**起始版本：** 19

### WIDTH

```cangjie
WIDTH
```

**功能：** 图片宽度（单位：像素）。

**起始版本：** 19

### func !=(PhotoKeys)

```cangjie
public operator func !=(other: PhotoKeys): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoKeys](#enum-photokeys)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|