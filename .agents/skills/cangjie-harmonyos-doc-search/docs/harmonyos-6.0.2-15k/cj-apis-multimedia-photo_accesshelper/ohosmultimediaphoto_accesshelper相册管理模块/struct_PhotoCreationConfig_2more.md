## struct PhotoCreationConfig

```cangjie
public struct PhotoCreationConfig {
    public PhotoCreationConfig(
        public let fileNameExtension: String,
        public let photoType: PhotoType,
        public let title!: String = "",
        public let subtype!: PhotoSubtype = DEFAULT
    )
}
```

**功能：** 保存图片/视频到媒体库的配置，包括保存的文件名等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### let fileNameExtension

```cangjie
public let fileNameExtension: String
```

**功能：** 文件扩展名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let photoType

```cangjie
public let photoType: PhotoType
```

**功能：** 文件类型。

**类型：** [PhotoType](#enum-phototype)

**读写能力：** 只读

**起始版本：** 19

### let subtype

```cangjie
public let subtype: PhotoSubtype = DEFAULT
```

**功能：** 文件子类型。

**类型：** [PhotoSubtype](#enum-photosubtype)

**读写能力：** 只读

**起始版本：** 19

### let title

```cangjie
public let title: String = ""
```

**功能：** 图片或者视频的标题。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### PhotoCreationConfig(String, PhotoType, String, PhotoSubtype)

```cangjie
public PhotoCreationConfig(
    public let fileNameExtension: String,
    public let photoType: PhotoType,
    public let title!: String = "",
    public let subtype!: PhotoSubtype = DEFAULT
)
```

**功能：** 构造PhotoCreationConfig对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fileNameExtension|String|是|-|文件扩展名，例如'jpg'。|
|photoType|[PhotoType](#enum-phototype)|是|-|创建的文件类型，IMAGE或者VIDEO。|
|title|String|否|""| **命名参数。** 图片或者视频的标题。|
|subtype|[PhotoSubtype](#enum-photosubtype)|否|DEFAULT| **命名参数。** 图片或者视频的文件子类型，DEFAULT或者MOVING_PHOTO。|

## struct PhotoSelectResult

```cangjie
public struct PhotoSelectResult {
    public PhotoSelectResult(
        public var photoUris: Array<String>,
        public var isOriginalPhoto: Bool
    )
}
```

**功能：** 返回图库选择后的结果集。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### var isOriginalPhoto

```cangjie
public var isOriginalPhoto: Bool
```

**功能：** 是否为原图。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var photoUris

```cangjie
public var photoUris: Array<String>
```

**功能：** 媒体文件的uri数组。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### PhotoSelectResult(Array\<String>, Bool)

```cangjie
public PhotoSelectResult(
    public var photoUris: Array<String>,
    public var isOriginalPhoto: Bool
)
```

**功能：** 构造PhotoSelectResult对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|photoUris|Array\<String>|是|-|返回图库选择后的媒体文件的uri数组，此uri数组只能通过临时授权的方式调用[getAssets接口](#func-getassetsfetchoptions)去使用。|
|isOriginalPhoto|Bool|是|-|返回图库选择后的媒体文件是否为原图。|