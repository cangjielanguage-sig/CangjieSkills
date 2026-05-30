## struct PhotoSelectResult

```cangjie
public struct PhotoSelectResult {
    public PhotoSelectResult (
        public var photoUris: Array<String>,
        public var isOriginalPhoto: Bool
    )
}
```

**功能：** 返回图库选择后的结果集。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

### var isOriginalPhoto

```cangjie
public var isOriginalPhoto: Bool
```

**功能：** 返回图库选择后的媒体文件是否为原图。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var photoUris

```cangjie
public var photoUris: Array<String>
```

**功能：** 返回图库选择后的媒体文件的URI数组。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### PhotoSelectResult(Array\<String>, Bool)

```cangjie
public PhotoSelectResult(
    public var photoUris: Array<String>,
    public var isOriginalPhoto: Bool
)
```

**功能：** 创建PhotoSelectResult对象。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|photoUris|Array\<String>|是|-|返回图库选择后的媒体文件的URI数组。|
|isOriginalPhoto|Bool|是|-|返回图库选择后的媒体文件是否为原图。|

## enum DocumentPickerMode

```cangjie
public enum DocumentPickerMode <: Equatable<DocumentPickerMode>  {
    | DEFAULT
    | DOWNLOAD
    | ...
}
```

**功能：** picker选择的文档模式。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**父类型：**

- Equatable\<DocumentPickerMode>

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 标准模式。

**起始版本：** 12

### DOWNLOAD

```cangjie
DOWNLOAD
```

**功能：** 下载模式。

**起始版本：** 12

### operator func !=(DocumentPickerMode)

```cangjie
public operator override func !=(other: DocumentPickerMode): Bool
```

**功能：** 对文档类型进行判不等。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DocumentPickerMode](#enum-documentpickermode)|是|-|文档类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果文档类型不同，返回true，否则返回false。|

### operator func ==(DocumentPickerMode)

```cangjie
public operator override func ==(mode: DocumentPickerMode): Bool
```

**功能：** 对文档类型进行判等。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[DocumentPickerMode](#enum-documentpickermode)|是|-|文档类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果文档类型相同，返回true，否则返回false。|

## enum DocumentSelectMode

```cangjie
public enum DocumentSelectMode {
    | FILE
    | FOLDER
    | MIXED
    | ...
}
```

**功能：** picker选择的文档类型。

**系统能力：** SystemCapability.FileManagement.UserFileService.FolderSelection

**起始版本：** 12

### FILE

```cangjie
FILE
```

**功能：** 文件类型。

**起始版本：** 12

### FOLDER

```cangjie
FOLDER
```

**功能：** 文件夹类型。

**起始版本：** 12

### MIXED

```cangjie
MIXED
```

**功能：** 文件和文件夹混合类型。

**起始版本：** 12

## enum PhotoViewMIMETypes

```cangjie
public enum PhotoViewMIMETypes {
    | IMAGE_TYPE
    | VIDEO_TYPE
    | IMAGE_VIDEO_TYPE
    | ...
}
```

**功能：** 可选择的媒体文件类型。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

### IMAGE_TYPE

```cangjie
IMAGE_TYPE
```

**功能：** 图片类型。

**起始版本：** 12

### IMAGE_VIDEO_TYPE

```cangjie
IMAGE_VIDEO_TYPE
```

**功能：** 图片和视频类型。

**起始版本：** 12

### VIDEO_TYPE

```cangjie
VIDEO_TYPE
```

**功能：** 视频类型。

**起始版本：** 12