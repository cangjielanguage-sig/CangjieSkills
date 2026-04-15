## class ModuleMetadata

```cangjie
public class ModuleMetadata {
    public let moduleName: String
    public let metadata: Array<Metadata>
}
```

**功能：** 描述模块的元数据信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let metadata

```cangjie
public let metadata: Array<Metadata>
```

**功能：** 该模块下的元数据信息列表。

**类型：** Array\<[Metadata](./cj-apis-metadata.md#class-metadata)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** 模块名。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

## class MultiAppMode

```cangjie
public class MultiAppMode {
    public let multiAppModeType: MultiAppModeType
    public let maxCount: Int32
}
```

**功能：** 表示应用多开模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let maxCount

```cangjie
public let maxCount: Int32
```

**功能：** 应用多开的最大个数。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let multiAppModeType

```cangjie
public let multiAppModeType: MultiAppModeType
```

**功能：** 应用多开模式的类型。

**类型：** [MultiAppModeType](#enum-multiappmodetype)

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

## class PreloadItem

```cangjie
public class PreloadItem {
    public let moduleName: String
}
```

**功能：** 描述原子化服务中模块的预加载模块信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** 模块名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

## class ReqPermissionDetail

```cangjie
public class ReqPermissionDetail {
    public var name: String
    public var moduleName: String
    public var reason: String
    public var reasonId: Int32
    public var usedScene: UsedScene
}
```

**功能：** 应用运行时需向系统申请的权限集合的详细信息。

> **说明：**
>
> 如果应用内多包申请的权限名称一样，但是权限申请理由不一致，系统只会返回一个权限申请理由，优先级从高到低顺序为entry类型HAP、feature类型HAP、应用内HSP。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### var moduleName

```cangjie
public var moduleName: String
```

**功能：** 申请该权限的module名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 需要使用的权限名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### var reason

```cangjie
public var reason: String
```

**功能：** 描述申请权限的原因。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### var reasonId

```cangjie
public var reasonId: Int32
```

**功能：** 描述申请权限的原因ID。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### var usedScene

```cangjie
public var usedScene: UsedScene
```

**功能：** 权限使用的场景和时机。

**类型：** [UsedScene](#class-usedscene)

**读写能力：** 可读写

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22