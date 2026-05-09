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
    public let supportedWindowModes: Array<SupportedWindowMode>
    public let windowSize: WindowSize
    public let excludeFromDock: Bool
    public let skills: Array<Skill>
    public let appIndex: Int32
}
```

**功能：** Ability信息。三方应用可以通过[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)获取Ability信息，其中入参bundleFlags至少包含GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ABILITY。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let appIndex

```cangjie
public let appIndex: Int32
```

**功能：** 应用包的分身索引标识，仅在分身应用中生效。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let applicationInfo

```cangjie
public let applicationInfo: ApplicationInfo
```

**功能：** 应用程序的配置信息。通过调用[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)接口获取，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY和GET_BUNDLE_INFO_WITH_APPLICATION的值。

**类型：** [ApplicationInfo](#class-applicationinfo)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let bundleName

```cangjie
public let bundleName: String
```

**功能：** 应用Bundle名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let description

```cangjie
public let description: String
```

**功能：** Ability的描述，对应module.json5中abilities下配置的description字段，用于描述当前ability提供的页面内容和功能作用。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let descriptionId

```cangjie
public let descriptionId: Int32
```

**功能：** Ability的描述资源id，是编译构建时根据应用配置abilities下的description自动生成的资源id。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let deviceTypes

```cangjie
public let deviceTypes: Array<String>
```

**功能：** Ability支持的设备类型，来源于module.json5配置的deviceTypes。

**类型：** Array\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let enabled

```cangjie
public let enabled: Bool
```

**功能：** Ability的可用性。可用表示可以拉起或查询，不可用时调用getAbilityInfo需携带GET_ABILITY_INFO_WITH_DISABLE的AbilityFlag。取值true表示可用，false表示不可用。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let excludeFromDock

```cangjie
public let excludeFromDock: Bool
```

**功能：** 判断Ability是否可在dock区域隐藏图标，true表示可以，false表示不可以。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22