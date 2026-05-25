## class AbilityInfo

```cangjie
public class AbilityInfo {
    public let bundleName: String
    public let moduleName: String
    public let name: String
    public let label: String
    public let labelId: Int32
    public let description: String
    public let descriptionId: Int32
    public let icon: String
    public let iconId: Int32
    public let process: String
    public let exported: Bool
    public let orientation: DisplayOrientation
    public let launchType: LaunchType
    public let permissions: Array<String>
    public let deviceTypes: Array<String>
    public let applicationInfo: ApplicationInfo
    public let metadata: Array<Metadata>
    public let enabled: Bool
    public let supportWindowModes: Array<SupportWindowMode>
    public let windowSize: WindowSize
    public let excludeFromDock: Bool
    public let skills: Array<Skill>
    public let appIndex: Int32
}
```

**功能：** Ability信息。三方应用可以通过[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)获取Ability信息，其中入参bundleFlags至少包含GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ABILITY。

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

**功能：** 应用程序的配置信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY和GET_BUNDLE_INFO_WITH_APPLICATION的值。

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

### let description

```cangjie
public let description: String
```

**功能：** Ability的描述。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let descriptionId

```cangjie
public let descriptionId: Int32
```

**功能：** Ability的描述资源id。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let deviceTypes

```cangjie
public let deviceTypes: Array<String>
```

**功能：** Ability支持的设备类型。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### let enabled

```cangjie
public let enabled: Bool
```

**功能：** Ability是否可用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let excludeFromDock

```cangjie
public let excludeFromDock: Bool
```

**功能：** 判断Ability是否可以在dock区域隐藏图标。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let exported

```cangjie
public let exported: Bool
```

**功能：** 判断Ability是否可以被其他应用调用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let icon

```cangjie
public let icon: String
```

**功能：** Ability的图标资源描述符，如"icon": "$media: icon"。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let iconId

```cangjie
public let iconId: Int32
```

**功能：** Ability的图标资源id。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let label

```cangjie
public let label: String
```

**功能：** Ability对用户显示的名称的资源描述符，如："label": "$string: mainability_description"。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let labelId

```cangjie
public let labelId: Int32
```

**功能：** Ability的标签资源id。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let launchType

```cangjie
public let launchType: LaunchType
```

**功能：** Ability的启动模式。

**类型：** [LaunchType](#enum-launchtype)

**读写能力：** 只读

**起始版本：** 12