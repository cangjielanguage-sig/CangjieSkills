## class ExtensionAbilityInfo

```cangjie
public class ExtensionAbilityInfo {
    public let bundleName: String
    public let moduleName: String
    public let name: String
    public let labelId: Int32
    public let descriptionId: Int32
    public let iconId: Int32
    public let exported: Bool
    public let extensionAbilityType: ExtensionAbilityType
    public let permissions: Array<String>
    public let applicationInfo: ApplicationInfo
    public let metadata: Array<Metadata>
    public let enabled: Bool
    public let readPermission: String
    public let writePermission: String
    public let extensionAbilityTypeName: String
    public let skills: Array<Skill>
    public let appIndex: Int32
}
```

**功能：** ExtensionAbilityInfo信息。三方应用可以通过[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)获取自身的ExtensionAbility信息，其中入参bundleFlags至少包含GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### let appIndex

```cangjie
public let appIndex: Int32
```

**功能：** 应用包的分身索引标识，仅在分身应用中生效。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let applicationInfo

```cangjie
public let applicationInfo: ApplicationInfo
```

**功能：** 应用程序的配置信息。

**类型：** [ApplicationInfo](#struct-applicationinfo)

**读写能力：** 只读

**起始版本：** 12

### let bundleName

```cangjie
public let bundleName: String
```

**功能：** 应用Bundle名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let descriptionId

```cangjie
public let descriptionId: Int32
```

**功能：** ExtensionAbility的描述资源ID。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let enabled

```cangjie
public let enabled: Bool
```

**功能：** ExtensionAbility是否可用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let exported

```cangjie
public let exported: Bool
```

**功能：** 判断ExtensionAbility是否可以被其他应用调用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let extensionAbilityType

```cangjie
public let extensionAbilityType: ExtensionAbilityType
```

**功能：** ExtensionAbility类型。

**类型：** [ExtensionAbilityType](#enum-extensionabilitytype)

**读写能力：** 只读

**起始版本：** 12

### let extensionAbilityTypeName

```cangjie
public let extensionAbilityTypeName: String
```

**功能：** ExtensionAbility的类型名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let iconId

```cangjie
public let iconId: Int32
```

**功能：** ExtensionAbility的图标资源ID。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let labelId

```cangjie
public let labelId: Int32
```

**功能：** ExtensionAbility的标签资源ID。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let metadata

```cangjie
public let metadata: Array<Metadata>
```

**功能：** ExtensionAbility的元信息。

**类型：** Array\<[Metadata](#class-metadata)>

**读写能力：** 只读

**起始版本：** 12

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** ExtensionAbility所属的HAP的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** ExtensionAbility名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let permissions

```cangjie
public let permissions: Array<String>
```

**功能：** 被其他应用ExtensionAbility调用时需要申请的权限集合。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### let readPermission

```cangjie
public let readPermission: String
```

**功能：** 读取ExtensionAbility数据所需的权限。

**类型：** String

**读写能力：** 只读

**起始版本：** 12