## class Metadata

```cangjie
public class Metadata {
    public var name: String
    public var value: String
    public var resource: String
    public init(name: String, value: String, resource: String)
}
```

**功能：** 元数据信息。三方应用可以通过[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)获取，其中入参bundleFlags至少包含GET_BUNDLE_INFO_WITH_METADATA。此对象在[AbilityInfo](#class-abilityinfo)、[ApplicationInfo](#struct-applicationinfo)、[ExtensionAbilityInfo](#class-extensionabilityinfo)、[HapModuleInfo](#struct-hapmoduleinfo)、[ModuleMetadata](#struct-modulemetadata)中均包含。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### var name

```cangjie
public var name: String
```

**功能：** 元数据名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var resource

```cangjie
public var resource: String
```

**功能：** 元数据资源。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var value

```cangjie
public var value: String
```

**功能：** 元数据值。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### init(String, String, String)

```cangjie
public init(name: String, value: String, resource: String)
```

**功能：** 创建元数据信息对象。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|元数据名称。|
|value|String|是|-|元数据值。|
|resource|String|是|-|元数据资源。|

## class SignatureInfo

```cangjie
public class SignatureInfo {
    public let appId: String
    public let fingerprint: String
    public let appIdentifier: String
}
```

**功能：** 描述应用包的签名信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### let appId

```cangjie
public let appId: String
```

**功能：** 应用的appId。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let appIdentifier

```cangjie
public let appIdentifier: String
```

**功能：** 应用的唯一标识，由云端统一分配。该ID在应用全生命周期中不会发生变化，包括版本升级、证书变更、开发者公私钥变更、应用转移等。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let fingerprint

```cangjie
public let fingerprint: String
```

**功能：** 应用包的指纹信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

```cangjie
public struct ModuleMetadata {
    public let moduleName: String
    public let metadata: Array<Metadata>
}
```

**功能：** 描述模块的元数据信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### let metadata

```cangjie
public let metadata: Array<Metadata>
```

**功能：** 该模块下的元数据信息列表。

**类型：** Array\<[Metadata](#class-metadata)>

**读写能力：** 只读

**起始版本：** 12

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** 模块名。

**类型：** String

**读写能力：** 只读

**起始版本：** 12