## class PhotoSelectOptions

```cangjie
public class PhotoSelectOptions <: BaseSelectOptions {
    public var isEditSupported: Bool = true
    public var isOriginalSupported: Bool = false
    public var subWindowName: ?String = None
    public init(
        MIMEType!: PhotoViewMIMETypes = IMAGE_VIDEO_TYPE,
        maxSelectNumber!: Int32 = 50,
        isPhotoTakingSupported!: Bool = true,
        isSearchSupported!: Bool = true,
        recommendationOptions!: RecommendationOptions = RecommendationOptions(),
        preselectedUris!: Array<String> = Array<String>(),
        isPreviewForSingleSelectionSupported!: Bool = true,
        isEditSupported!: Bool = true,
        isOriginalSupported!: Bool = false,
        subWindowName!: ?String = None
    )
}
```

**功能：** 图库选择选项子类，继承于BaseSelectOptions。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- [BaseSelectOptions](#class-baseselectoptions)

### var isEditSupported

```cangjie
public var isEditSupported: Bool = true
```

**功能：** 是否支持编辑照片。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var isOriginalSupported

```cangjie
public var isOriginalSupported: Bool = false
```

**功能：** 是否显示选择原图按钮。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var subWindowName

```cangjie
public var subWindowName: ?String = None
```

**功能：** 子窗窗口名称。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### init(PhotoViewMIMETypes, Int32, Bool, Bool, RecommendationOptions, Array\<String>, Bool, Bool, Bool, ?String)

```cangjie
public init(
    MIMEType!: PhotoViewMIMETypes = IMAGE_VIDEO_TYPE,
    maxSelectNumber!: Int32 = 50,
    isPhotoTakingSupported!: Bool = true,
    isSearchSupported!: Bool = true,
    recommendationOptions!: RecommendationOptions = RecommendationOptions(),
    preselectedUris!: Array<String> = Array<String>(),
    isPreviewForSingleSelectionSupported!: Bool = true,
    isEditSupported!: Bool = true,
    isOriginalSupported!: Bool = false,
    subWindowName!: ?String = None
)
```

**功能：** 构造PhotoSelectOptions对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|MIMEType|[PhotoViewMIMETypes](#enum-photoviewmimetypes)|否|IMAGE_VIDEO_TYPE| **命名参数。** 可选择的媒体文件类型，若无此参数，则默认为图片和视频类型。|
|maxSelectNumber|Int32|否|50| **命名参数。** 选择媒体文件数量的最大值(最大可设置的值为500，若不设置则默认为50)。|
|isPhotoTakingSupported|Bool|否|true| **命名参数。** 是否支持拍照，true表示支持，false表示不支持，默认为true。|
|isSearchSupported|Bool|否|true| **命名参数。** 是否支持搜索，true表示支持，false表示不支持，默认为true。|
|recommendationOptions|[RecommendationOptions](#struct-recommendationoptions)|否|RecommendationOptions()| **命名参数。** 图片推荐相关配置参数。|
|preselectedUris|Array\<String>|否|Array\<String>()| **命名参数。** 预选择图片的uri数据。|
|isPreviewForSingleSelectionSupported|Bool|否|true| **命名参数。** 单选模式下是否需要进大图预览，true表示需要，false表示不需要，默认为true。|
|isEditSupported|Bool|否|true| **命名参数。** 是否支持编辑照片，true表示支持，false表示不支持，默认为true。|
|isOriginalSupported|Bool|否|false| **命名参数。** 是否显示选择原图按钮，true表示显示，false表示不显示，默认为false。|
|subWindowName|?String|否|None| **命名参数。** 子窗窗口名称。|