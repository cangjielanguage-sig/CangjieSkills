## enum BundleType

```cangjie
public enum BundleType {
    | APP
    | ATOMIC_SERVICE
    | ...
}
```

**功能：** 标识应用的类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### APP

```cangjie
APP
```

**功能：** 该Bundle是应用。

**起始版本：** 12

### ATOMIC_SERVICE

```cangjie
ATOMIC_SERVICE
```

**功能：** 该Bundle是元服务。

**起始版本：** 12

## enum CompatiblePolicy

```cangjie
public enum CompatiblePolicy {
    | BACKWARD_COMPATIBILITY
    | ...
}
```

**功能：** 标识共享库的版本兼容类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### BACKWARD_COMPATIBILITY

```cangjie
BACKWARD_COMPATIBILITY
```

**功能：** 该字段表明共享库是向后兼容类型。

**起始版本：** 12