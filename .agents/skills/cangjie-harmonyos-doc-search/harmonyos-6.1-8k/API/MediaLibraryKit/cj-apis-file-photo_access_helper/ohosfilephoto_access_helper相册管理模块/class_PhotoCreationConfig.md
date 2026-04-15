## class PhotoCreationConfig

```cangjie
public class PhotoCreationConfig {
    public var fileNameExtension: String
    public var photoType: PhotoType
    public var title: String
    public var subtype: PhotoSubtype
    public init(fileNameExtension: String, photoType: PhotoType, title!: String = "", subtype!: PhotoSubtype = Default)
}
```

**功能：** 保存图片/视频到媒体库的配置，包括保存的文件名等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var fileNameExtension

```cangjie
public var fileNameExtension: String
```

**功能：** 文件扩展名。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var photoType

```cangjie
public var photoType: PhotoType
```

**功能：** 创建的文件类型[PhotoType](#phototype)，Image或者Video。

**类型：** [PhotoType](#enum-phototype)

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var subtype

```cangjie
public var subtype: PhotoSubtype
```

**功能：** 图片或者视频的文件子类型[PhotoSubtype](#enum-photosubtype)。

**类型：** [PhotoSubtype](#enum-photosubtype)

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var title

```cangjie
public var title: String
```

**功能：** 图片或者视频的标题，不传入时由系统生成。参数规格为：

- 不应包含扩展名。

- 文件名字符串长度为1~255（资产文件名为标题+扩展名）。

- 不允许出现的非法英文字符，包括：. \ / : * ? " ' ` < > \| { } [ ]

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### init(String, PhotoType, String, PhotoSubtype)

```cangjie
public init(fileNameExtension: String, photoType: PhotoType, title!: String = "", subtype!: PhotoSubtype = Default)
```

**功能：** 构造PhotoCreationConfig对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fileNameExtension|String|是|-|文件扩展名，例如'jpg'。|
|photoType|[PhotoType](#enum-phototype)|是|-|创建的文件类型[PhotoType](#phototype)，IMAGE或者VIDEO。|
|title|String|否|""| **命名参数。** 图片或者视频的标题，不传入时由系统生成。|
|subtype|[PhotoSubtype](#enum-photosubtype)|否|Default| **命名参数。** 图片或者视频的文件子类型[PhotoSubtype](#enum-photosubtype)，不传入时默认为Default。|