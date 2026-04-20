## class HapModuleInfo

```cangjie
public class HapModuleInfo {
    public let name: String
    public let icon: String
    public let iconId: Int32
    public let label: String
    public let labelId: Int32
    public let description: String
    public let descriptionId: Int32
    public let mainElementName: String
    public let abilitiesInfo: Array<AbilityInfo>
    public let extensionAbilitiesInfo: Array<ExtensionAbilityInfo>
    public let metadata: Array<Metadata>
    public let deviceTypes: Array<String>
    public let installationFree: Bool
    public let hashValue: String
    public let moduleType: ModuleType
    public let preloads: Array<PreloadItem>
    public let dependencies: Array<Dependency>
    public let fileContextMenuConfig: String
    public let routerMap: Array<RouterItem>
    public let codePath: String
    public let nativeLibraryPath: String
}
```

**功能：** HAP信息，可以通过[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)获取自身的HAP信息，其中参数[bundleFlags](#class-bundleflag)至少包含GET_BUNDLE_INFO_WITH_HAP_MODULE。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let abilitiesInfo

```cangjie
public let abilitiesInfo: Array<AbilityInfo>
```

**功能：** 当前模块所有Ability的信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ABILITY获取。

**类型：** Array\<[AbilityInfo](#class-abilityinfo)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let codePath

```cangjie
public let codePath: String
```

**功能：** 模块的安装路径。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let dependencies

```cangjie
public let dependencies: Array<Dependency>
```

**功能：** 模块运行依赖的动态共享库列表。

**类型：** Array\<[Dependency](#class-dependency)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let description

```cangjie
public let description: String
```

**功能：** 模块描述信息。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let descriptionId

```cangjie
public let descriptionId: Int32
```

**功能：** 描述信息的资源id值。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let deviceTypes

```cangjie
public let deviceTypes: Array<String>
```

**功能：** 可以运行模块的设备类型。

**类型：** Array\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let extensionAbilitiesInfo

```cangjie
public let extensionAbilitiesInfo: Array<ExtensionAbilityInfo>
```

**功能：** 当前模块所有ExtensionAbility的信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY获取。

**类型：** Array\<[ExtensionAbilityInfo](#class-extensionabilityinfo)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22