## class BaseSelectOptions

```cangjie
public open class BaseSelectOptions {
    public BaseSelectOptions(
        public var MIMEType!: PhotoViewMIMETypes = IMAGE_VIDEO_TYPE,
        public var maxSelectNumber!: Int32 = 50,
        public var isPhotoTakingSupported!: Bool = true,
        public var isSearchSupported!: Bool = true,
        public var recommendationOptions!: RecommendationOptions = RecommendationOptions(),
        public var preselectedUris!: Array<String> = Array<String>(),
        public var isPreviewForSingleSelectionSupported!: Bool = true
    )
}
```

**功能：** 图库选择选项基类。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### var MIMEType

```cangjie
public var MIMEType: PhotoViewMIMETypes = IMAGE_VIDEO_TYPE
```

**功能：** 媒体文件类型。

**类型：** [PhotoViewMIMETypes](#enum-photoviewmimetypes)

**读写能力：** 可读写

**起始版本：** 19

### var isPhotoTakingSupported

```cangjie
public var isPhotoTakingSupported: Bool = true
```

**功能：** 是否支持拍照。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var isPreviewForSingleSelectionSupported

```cangjie
public var isPreviewForSingleSelectionSupported: Bool = true
```

**功能：** 单选模式下是否需要进大图预览。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var isSearchSupported

```cangjie
public var isSearchSupported: Bool = true
```

**功能：** 是否支持搜索。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var maxSelectNumber

```cangjie
public var maxSelectNumber: Int32 = 50
```

**功能：** 媒体文件数量的最大值。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var preselectedUris

```cangjie
public var preselectedUris: Array<String> = Array<String>()
```

**功能：** 预选择图片的uri数据。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var recommendationOptions

```cangjie
public var recommendationOptions: RecommendationOptions = RecommendationOptions()
```

**功能：** 图片推荐相关配置参数。

**类型：** [RecommendationOptions](#struct-recommendationoptions)

**读写能力：** 可读写

**起始版本：** 19