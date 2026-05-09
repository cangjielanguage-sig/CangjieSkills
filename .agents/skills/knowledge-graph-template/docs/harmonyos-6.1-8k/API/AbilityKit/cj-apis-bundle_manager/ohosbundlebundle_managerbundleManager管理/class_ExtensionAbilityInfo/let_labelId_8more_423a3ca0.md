### let labelId

```cangjie
public let labelId: Int32
```

**功能：** ExtensionAbility的标签资源ID。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let metadata

```cangjie
public let metadata: Array<Metadata>
```

**功能：** ExtensionAbility的元信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY和GET_BUNDLE_INFO_WITH_METADATA获取。

**类型：** Array\<[Metadata](./cj-apis-metadata.md#class-metadata)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** ExtensionAbility所属的HAP的名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let name

```cangjie
public let name: String
```

**功能：** ExtensionAbility名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let permissions

```cangjie
public let permissions: Array<String>
```

**功能：** 被其他应用ExtensionAbility调用时需要申请的权限集合。

**类型：** Array\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let readPermission

```cangjie
public let readPermission: String
```

**功能：** 读取ExtensionAbility数据所需的权限。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let skills

```cangjie
public let skills: Array<Skill>
```

**功能：** ExtensionAbility的Skills信息。

**类型：** Array\<[Skill](./cj-apis-skill.md#class-skill)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let writePermission

```cangjie
public let writePermission: String
```

**功能：** 向ExtensionAbility写数据所需的权限。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22