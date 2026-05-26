## struct DataItem

```cangjie
public struct DataItem {
    public let key: String
    public let value: String
}
```

**功能：** 描述模块配置的路由表中的自定义数据。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 19

### let key

```cangjie
public let key: String
```

**功能：** 标识路由表自定义数据的键。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let value

```cangjie
public let value: String
```

**功能：** 标识路由表自定义数据的值。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

## struct Dependency

```cangjie
public struct Dependency {
    public let bundleName: String
    public let moduleName: String
    public let versionCode: UInt32
}
```

**功能：** 描述模块所依赖的动态共享库信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### let bundleName

```cangjie
public let bundleName: String
```

**功能：** 标识当前模块依赖的共享包包名。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** 标识当前模块依赖的共享包模块名。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let versionCode

```cangjie
public let versionCode: UInt32
```

**功能：** 标识当前共享包的版本号。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12