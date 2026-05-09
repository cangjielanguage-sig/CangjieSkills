## enum DiagReportLevel

```cangjie
public enum DiagReportLevel {
    ERROR|
    WARNING
}
```

功能：表示报错接口的信息等级，支持 `ERROR` 和 `WARNING` 两种等级。

### ERROR

```cangjie
ERROR
```

功能：构造一个表示 ERROR 的枚举实例。

### WARNING

```cangjie
WARNING
```

功能：构造一个表示 WARNING 的枚举实例。

### func level()

```cangjie
public func level(): Int32
```

功能：返回枚举值对应的整型。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 枚举值对应的整型。`ERROR` 返回 0，`WARNING` 返回 1。

## enum ImportKind

```cangjie
public enum ImportKind <: ToString {
    Single | Alias | All | Multi
}
```

功能：表示导入语句的类型。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### Single

```cangjie
Single
```

功能：表示单导入，如 `import a.b`。

### Alias

```cangjie
Alias
```

功能：表示别名导入，如 `import a.b as c`。

### All

```cangjie
All
```

功能：表示全导入，如 `import a.b.*`。

### Multi

```cangjie
Multi
```

功能：表示多导入，如 `import a.{b, c, d}`。

### func toString()

```cangjie
public func toString(): String
```

功能：将 [ImportKind](ast_package_enums.md#enum-importkind) 类型转化为字符串类型表示。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - [ImportKind](ast_package_enums.md#enum-importkind) 转换后的字符串值。