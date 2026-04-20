### let labelId

```cangjie
public let labelId: Int32
```

**功能：** 标识应用名称的资源id，是编译构建时根据应用配置的label自动生成的资源id。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let labelResource

```cangjie
public let labelResource: AppResource
```

**功能：** 应用程序的名称资源信息，包含bundleName、moduleName和id，可以调用全球化的接口[getMediaContent](../LocalizationKit/cj-apis-resource_manager.md#func-getmediacontentuint32-screendensity)来获取详细的资源数据信息。

**类型：** [AppResource](../LocalizationKit/cj-apis-resource.md#class-appresource)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let metadataArray

```cangjie
public let metadataArray: Array<ModuleMetadata>
```

**功能：** 应用程序的元信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_APPLICATION和GET_BUNDLE_INFO_WITH_METADATA的值。

**类型：** Array\<[ModuleMetadata](#class-modulemetadata)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let multiAppMode

```cangjie
public let multiAppMode: MultiAppMode
```

**功能：** 应用多开模式。

**类型：** [MultiAppMode](#class-multiappmode)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let name

```cangjie
public let name: String
```

**功能：** 应用程序的名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let nativeLibraryPath

```cangjie
public let nativeLibraryPath: String
```

**功能：** 应用程序的本地库文件路径。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let permissions

```cangjie
public let permissions: Array<String>
```

**功能：** 访问应用程序所需的权限。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_APPLICATION和GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION的值。

**类型：** Array\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let process

```cangjie
public let process: String
```

**功能：** 应用程序的进程名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let releaseType

```cangjie
public let releaseType: String
```

**功能：** 标识应用打包时使用的SDK的发布类型。当前SDK的发布类型可能为Canary、Beta、Release，其中Canary和Beta可能通过序号进一步细分，例如Canary1、Canary2、Beta1、Beta2等。开发者可通过对比应用打包依赖的SDK发布类型和OS的发布类型（[deviceInfo.distributionOSReleaseType](../BasicServicesKit/cj-apis-device_info.md)）来判断兼容性。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let removable

```cangjie
public let removable: Bool
```

**功能：** 应用程序是否可以被移除，取值为true表示可以被移除，取值为false表示不可以被移除。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22