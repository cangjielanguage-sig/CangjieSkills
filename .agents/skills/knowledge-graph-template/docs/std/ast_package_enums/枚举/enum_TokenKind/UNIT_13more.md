### UNIT

```cangjie
UNIT
```

功能：构造一个表示 `unit` 的枚举实例。

### UNIT_LITERAL

```cangjie
UNIT_LITERAL
```

功能：构造一个表示 `unit` 字面量的枚举实例。

### UNSAFE

```cangjie
UNSAFE
```

功能：构造一个表示 `unsafe` 的枚举实例。

### UPPERBOUND

```cangjie
UPPERBOUND
```

功能：构造一个表示 `<:` 的枚举实例。

### VAR

```cangjie
VAR
```

功能：构造一个表示 `var` 的枚举实例。

### VARRAY

```cangjie
VARRAY
```

功能：构造一个表示 `varray` 的枚举实例。

### WHERE

```cangjie
WHERE
```

功能：构造一个表示 `where` 的枚举实例。

### WHILE

```cangjie
WHILE
```

功能：构造一个表示 `while` 的枚举实例。

### WILDCARD

```cangjie
WILDCARD
```

功能：构造一个表示 `_` 的枚举实例。

### WITH

```cangjie
WITH
```

功能：构造一个表示 `with` 的枚举实例。

### func !=(TokenKind)

```cangjie
public operator func !=(right: TokenKind): Bool
```

功能：重载不等号操作符，用于比较两个 [TokenKind](ast_package_enums.md#enum-tokenkind) 是否相等。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 布尔类型。

### func ==(TokenKind)

```cangjie
public operator func ==(right: TokenKind): Bool
```

功能：重载等号操作符，用于比较两个 [TokenKind](ast_package_enums.md#enum-tokenkind) 是否相等。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 布尔类型。

### func toString()

```cangjie
public func toString(): String
```

功能：将 [TokenKind](ast_package_enums.md#enum-tokenkind) 类型转化为字符串类型表示。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - [TokenKind](ast_package_enums.md#enum-tokenkind) 转换后的字符串值。