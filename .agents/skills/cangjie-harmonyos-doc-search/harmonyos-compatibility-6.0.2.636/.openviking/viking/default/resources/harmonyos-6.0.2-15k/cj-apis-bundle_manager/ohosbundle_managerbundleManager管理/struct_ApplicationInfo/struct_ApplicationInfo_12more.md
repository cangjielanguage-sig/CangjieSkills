## struct ApplicationInfo

```cangjie
public struct ApplicationInfo {
    public let name: String
    public let description: String
    public let descriptionId: Int32
    public let enabled: Bool
    public let label: String
    public let labelId: Int32
    public let icon: String
    public let iconId: Int32
    public let process: String
    public let permissions: Array<String>
    public let codePath: String
    public let metadataArray: Array<ModuleMetadata>
    public let removable: Bool
    public let accessTokenId: UInt32
    public let uid: Int32
    public let iconResource: AppResource
    public let labelResource: AppResource
    public let descriptionResource: AppResource
    public let appDistributionType: String
    public let appProvisionType: String
    public let systemApp: Bool
    public let bundleType: BundleType
    public let debug: Bool
    public let dataUnclearable: Bool
    public let cloudFileSyncEnabled: Bool
    public let nativeLibraryPath: String
    public let multiAppMode: MultiAppMode
    public let appIndex: Int32
    public let installSource: String
    public let releaseType: String
}
```

**功能：** 应用程序的配置信息。三方应用可以通过[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)获取自身的应用程序信息，其中入参bundleFlags至少包含GET_BUNDLE_INFO_WITH_APPLICATION。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### let accessTokenId

```cangjie
public let accessTokenId: UInt32
```

**功能：** 应用程序的accessTokenId。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let appDistributionType

```cangjie
public let appDistributionType: String
```

**功能：** 应用程序签名证书的分发类型，分为：app_gallery、enterprise、os_integration和crowdtesting。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let appIndex

```cangjie
public let appIndex: Int32
```

**功能：** 应用包的分身索引标识，仅在分身应用中生效。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let appProvisionType

```cangjie
public let appProvisionType: String
```

**功能：** 应用程序签名证书文件的类型，分为debug和release两种类型。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let bundleType

```cangjie
public let bundleType: BundleType
```

**功能：** 标识包的类型，取值为APP（应用）或者ATOMIC_SERVICE（元服务）。

**类型：** [BundleType](#enum-bundletype)

**读写能力：** 只读

**起始版本：** 12

### let cloudFileSyncEnabled

```cangjie
public let cloudFileSyncEnabled: Bool
```

**功能：** 标识当前应用是否启用端云文件同步能力。true表示当前应用启用端云文件同步能力，false表示当前应用不启用端云文件同步能力。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let codePath

```cangjie
public let codePath: String
```

**功能：** 应用程序的安装目录。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let dataUnclearable

```cangjie
public let dataUnclearable: Bool
```

**功能：** 标识应用数据是否可被删除。true表示不可删除，false表示可以删除。默认为false。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let debug

```cangjie
public let debug: Bool
```

**功能：** 标识应用是否处于调试模式，默认为false。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let description

```cangjie
public let description: String
```

**功能：** 标识应用的描述信息，使用示例："description": $string: mainability_description"。关于description的详细信息可参见descriptionResource字段说明。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let descriptionId

```cangjie
public let descriptionId: Int32
```

**功能：** 标识应用的描述信息的资源id。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12