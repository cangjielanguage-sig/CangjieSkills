## struct HapModuleInfo

```cangjie
public struct HapModuleInfo {
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

**功能：** HAP信息。三方应用可以通过[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)获取自身的HAP信息，其中入参bundleFlags至少包含GET_BUNDLE_INFO_WITH_HAP_MODULE。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### let abilitiesInfo

```cangjie
public let abilitiesInfo: Array<AbilityInfo>
```

**功能：** Ability信息。

**类型：** Array\<[AbilityInfo](#class-abilityinfo)>

**读写能力：** 只读

**起始版本：** 12

### let codePath

```cangjie
public let codePath: String
```

**功能：** 模块的安装路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let dependencies

```cangjie
public let dependencies: Array<Dependency>
```

**功能：** 模块运行依赖的动态共享库列表。

**类型：** Array\<[Dependency](#struct-dependency)>

**读写能力：** 只读

**起始版本：** 12

### let description

```cangjie
public let description: String
```

**功能：** 模块描述信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let descriptionId

```cangjie
public let descriptionId: Int32
```

**功能：** 描述信息的资源id值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let deviceTypes

```cangjie
public let deviceTypes: Array<String>
```

**功能：** 可以运行模块的设备类型。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### let extensionAbilitiesInfo

```cangjie
public let extensionAbilitiesInfo: Array<ExtensionAbilityInfo>
```

**功能：** ExtensionAbility信息。

**类型：** Array\<[ExtensionAbilityInfo](#class-extensionabilityinfo)>

**读写能力：** 只读

**起始版本：** 12

### let fileContextMenuConfig

```cangjie
public let fileContextMenuConfig: String
```

**功能：** 模块的文件菜单配置。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let hashValue

```cangjie
public let hashValue: String
```

**功能：** 模块的Hash值。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let icon

```cangjie
public let icon: String
```

**功能：** 模块图标。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let iconId

```cangjie
public let iconId: Int32
```

**功能：** 模块图标的资源id值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let installationFree

```cangjie
public let installationFree: Bool
```

**功能：** 模块是否支持免安装。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let label

```cangjie
public let label: String
```

**功能：** 模块标签。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let labelId

```cangjie
public let labelId: Int32
```

**功能：** 模块标签的资源id值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let mainElementName

```cangjie
public let mainElementName: String
```

**功能：** 入口ability信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 12