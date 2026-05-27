### let descriptionResource

```cangjie
public let descriptionResource: AppResource
```

**功能：** 应用程序的描述资源信息，包含了bundleName、moduleName和资源的id，可以调用全球化的接口[getMediaContent](../LocalizationKit/cj-apis-resource_manager.md#func-getmediacontentappresource-uint32)来获取详细的资源数据信息。

**类型：** [AppResource](../LocalizationKit/cj-apis-resource_manager.md#class-appresource)

**读写能力：** 只读

**起始版本：** 12

### let enabled

```cangjie
public let enabled: Bool
```

**功能：** 判断应用程序是否可以使用，默认为true。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let icon

```cangjie
public let icon: String
```

**功能：** 应用程序的图标，使用示例："icon": "$media: icon"。关于icon的详细信息可参见iconResource字段说明。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let iconId

```cangjie
public let iconId: Int32
```

**功能：** 应用程序图标的资源id。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let iconResource

```cangjie
public let iconResource: AppResource
```

**功能：** 应用程序的图标资源信息，包含了bundleName、moduleName和资源的id，可以调用全球化的接口[getMediaContent](../LocalizationKit/cj-apis-resource_manager.md#func-getmediacontentappresource-uint32)来获取详细的资源数据信息。

**类型：** [AppResource](../LocalizationKit/cj-apis-resource_manager.md#class-appresource)

**读写能力：** 只读

**起始版本：** 12

### let installSource

```cangjie
public let installSource: String
```

**功能：** 应用程序的安装来源。pre-installed表示应用为预置应用，格式为包名表示应用由包名对应的应用安装，unknown表示应用安装来源未知。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let label

```cangjie
public let label: String
```

**功能：** 标识应用的名称，使用示例："label": "$string: mainability_description"。关于label的详细信息可参见labelResource字段说明。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let labelId

```cangjie
public let labelId: Int32
```

**功能：** 标识应用名称的资源id。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let labelResource

```cangjie
public let labelResource: AppResource
```

**功能：** 应用程序的标签资源信息，包含了bundleName、moduleName和资源的id，可以调用全球化的接口[getMediaContent](../LocalizationKit/cj-apis-resource_manager.md#func-getmediacontentappresource-uint32)来获取详细的资源数据信息。

**类型：** [AppResource](../LocalizationKit/cj-apis-resource_manager.md#class-appresource)

**读写能力：** 只读

**起始版本：** 12

### let metadataArray

```cangjie
public let metadataArray: Array<ModuleMetadata>
```

**功能：** 应用程序的元信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_APPLICATION和GET_BUNDLE_INFO_WITH_METADATA的值。

**类型：** Array\<[ModuleMetadata](#struct-modulemetadata)>

**读写能力：** 只读

**起始版本：** 12

### let multiAppMode

```cangjie
public let multiAppMode: MultiAppMode
```

**功能：** 应用多开模式。

**类型：** [MultiAppMode](#struct-multiappmode)

**读写能力：** 只读

**起始版本：** 19

### let name

```cangjie
public let name: String
```

**功能：** 应用程序的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let nativeLibraryPath

```cangjie
public let nativeLibraryPath: String
```

**功能：** 应用程序的本地库文件路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 19