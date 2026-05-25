### BaseSelectOptions(PhotoViewMIMETypes, Int32, Bool, Bool, RecommendationOptions, Array\<String>, Bool)

```cangjie
public BaseSelectOptions(
    public var MIMEType!: PhotoViewMIMETypes = IMAGE_VIDEO_TYPE,
    public var maxSelectNumber!: Int32 = 50,
    public var isPhotoTakingSupported!: Bool = true,
    public var isSearchSupported!: Bool = true,
    public var recommendationOptions!: RecommendationOptions = RecommendationOptions(),
    public var preselectedUris!: Array<String> = Array<String>(),
    public var isPreviewForSingleSelectionSupported!: Bool = true
)
```

**功能：** 构造BaseSelectOptions对象。

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