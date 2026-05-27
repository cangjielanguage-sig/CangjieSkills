## struct ModuleMetadata

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

## struct MultiAppMode

```cangjie
public struct MultiAppMode {
    public let multiAppModeType: MultiAppModeType
    public let count: Int32
}
```

**功能：** 表示应用多开模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 19

### let count

```cangjie
public let count: Int32
```

**功能：** 应用多开的最大个数。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let multiAppModeType

```cangjie
public let multiAppModeType: MultiAppModeType
```

**功能：** 应用多开模式的类型。

**类型：** [MultiAppModeType](#enum-multiappmodetype)

**读写能力：** 只读

**起始版本：** 19

## struct PreloadItem

```cangjie
public struct PreloadItem {
    public let moduleName: String
}
```

**功能：** 描述元服务中模块的预加载模块信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** 模块运行时，由系统自动执行预加载的模块名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12