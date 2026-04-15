### let permissions

```cangjie
public let permissions: Array<String>
```

**功能：** 被其他应用拉起/访问时，其他应用需要申请的权限集合，只有当前AbilityInfo的exported为true，即当前Ability可以被其他应用拉起时，才会查看其他应用是否存在拉起/访问的权限。

**类型：** Array\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let process

```cangjie
public let process: String
```

**功能：** Ability的进程名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let skills

```cangjie
public let skills: Array<Skill>
```

**功能：** Ability的Skills信息，标识UIAbility组件或者ExtensionAbility组件能够接收的[Want](../../application-models/cj-want-overview.md)的特征。

**类型：** Array\<[Skill](./cj-apis-skill.md#class-skill)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let supportedWindowModes

```cangjie
public let supportedWindowModes: Array<SupportedWindowMode>
```

**功能：** Ability支持的窗口模式。

**类型：** Array\<[SupportedWindowMode](#enum-supportedwindowmode)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let windowSize

```cangjie
public let windowSize: WindowSize
```

**功能：** Ability窗口尺寸。

**类型：** [WindowSize](#class-windowsize)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22