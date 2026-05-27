## struct PhotoSaveOptions

```cangjie
public struct PhotoSaveOptions {
    public PhotoSaveOptions (
        public var newFileNames!: Array<String> = Array<String>()
    )
}
```

**功能：** 图片或视频的保存选项。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

### var newFileNames

```cangjie
public var newFileNames: Array<String> = Array<String>()
```

**功能：** 拉起photoPicker进行保存图片或视频资源的文件名，若无此参数，则默认需要用户自行输入。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### PhotoSaveOptions(Array\<String>)

```cangjie
public PhotoSaveOptions(
    public var newFileNames!: Array<String> = Array<String>()
)
```

**功能：** 创建PhotoSaveOptions对象。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newFileNames|Array\<String>|否|Array\<String>()| **命名参数。** 拉起photoPicker进行保存图片或视频资源的文件名，若无此参数，则默认需要用户自行输入。|

## struct PhotoSelectOptions

```cangjie
public struct PhotoSelectOptions {
    public PhotoSelectOptions (
        public var MIMEType!: PhotoViewMIMETypes = IMAGE_VIDEO_TYPE,
        public var maxSelectNumber!: Int64 = 50
    )
}
```

**功能：** 图库选择选项。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

### var MIMEType

```cangjie
public var MIMEType: PhotoViewMIMETypes = IMAGE_VIDEO_TYPE
```

**功能：** 可选择的媒体文件类型，若无此参数，则默认为图片和视频类型。

**类型：** [PhotoViewMIMETypes](#enum-photoviewmimetypes)

**读写能力：** 可读写

**起始版本：** 12

### var maxSelectNumber

```cangjie
public var maxSelectNumber: Int64 = 50
```

**功能：** 选择媒体文件数量的最大值（默认值为50，最大值为500。如果传入参数小于等于0，则取默认值；如果传入参数大于最大值，则取最大值）。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 12

### PhotoSelectOptions(PhotoViewMIMETypes, Int64)

```cangjie
public PhotoSelectOptions(
    public var MIMEType!: PhotoViewMIMETypes = IMAGE_VIDEO_TYPE,
    public var maxSelectNumber!: Int64 = 50
)
```

**功能：** 创建PhotoSelectOptions对象。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|MIMEType|[PhotoViewMIMETypes](#enum-photoviewmimetypes)|否|IMAGE_VIDEO_TYPE| **命名参数。** 可选择的媒体文件类型，若无此参数，则默认为图片和视频类型。|
|maxSelectNumber|Int64|否|50| **命名参数。** 选择媒体文件数量的最大值（默认值为50，最大值为500。如果传入参数小于等于0，则取默认值；如果传入参数大于最大值，则取最大值）。|