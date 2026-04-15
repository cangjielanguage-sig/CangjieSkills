### let fileContextMenuConfig

```cangjie
public let fileContextMenuConfig: String
```

**功能：** 模块的文件菜单配置。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_MENU获取。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let hashValue

```cangjie
public let hashValue: String
```

**功能：** 模块的Hash值。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let icon

```cangjie
public let icon: String
```

**功能：** 当前模块入口Ability的图标，取值为图标资源文件的索引，与模块配置文件中abilities标签或extensionAbilities标签的icon字段值一致。若未配置入口Ability，则为空。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let iconId

```cangjie
public let iconId: Int32
```

**功能：** 当前模块入口Ability的图标资源id值。若未配置入口Ability，则为空。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let installationFree

```cangjie
public let installationFree: Bool
```

**功能：** 模块是否支免安装（无需用户通过应用市场显式安装），取值为true表示支持免安装，取值为false表示不支持免安装。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let label

```cangjie
public let label: String
```

**功能：** 当前模块入口Ability的名称，取值为字符串资源的索引，与模块配置文件中abilities标签或extensionAbilities标签的label字段值一致。若未配置入口Ability，则为空。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let labelId

```cangjie
public let labelId: Int32
```

**功能：** 当前模块入口Ability名称的资源id值。若未配置入口Ability，则为空。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let mainElementName

```cangjie
public let mainElementName: String
```

**功能：** 当前模块的入口UIAbility名称或者ExtensionAbility名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let metadata

```cangjie
public let metadata: Array<Metadata>
```

**功能：** 当前模块的元数据。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_METADATA获取。

**类型：** Array\<[Metadata](./cj-apis-metadata.md#class-metadata)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let moduleType

```cangjie
public let moduleType: ModuleType
```

**功能：** 标识当前模块的类型。

**类型：** [ModuleType](#enum-moduletype)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let name

```cangjie
public let name: String
```

**功能：** 模块名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let nativeLibraryPath

```cangjie
public let nativeLibraryPath: String
```

**功能：** 应用程序内模块本地库文件路径。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22