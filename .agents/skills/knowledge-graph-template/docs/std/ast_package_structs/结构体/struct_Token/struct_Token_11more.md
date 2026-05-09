## struct Token

```cangjie
public struct Token <: ToBytes {
    public let kind: TokenKind
    public let pos: Position
    public let value: String
    public var delimiterNum: UInt16 = 1
    public init()
    public init(kind: TokenKind)
    public init(kind: TokenKind, value: String)
}
```

功能：词法单元类型。

词法单元是构成仓颉源码的最小单元，一组合法的词法单元列表经过语法解析后可生成一个语法树节点。

父类型：

- [ToBytes](ast_package_interfaces.md#interface-tobytes)

### let kind

```cangjie
public let kind: TokenKind
```

功能：词法单元的类型。词法单元类型有关键字、标识符、运算符、常量值等，具体见 [TokenKind](ast_package_enums.md#enum-tokenkind) 章节。

类型：[TokenKind](ast_package_enums.md#enum-tokenkind)

### let pos

```cangjie
public let pos: Position
```

功能：词法单元在源码中的位置信息。

类型：[Position](ast_package_structs.md#struct-position)

### let value

```cangjie
public let value: String
```

功能：词法单元的字面量值。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### var delimiterNum

```cangjie
public var delimiterNum: UInt16 = 1
```

功能：多行字符串的 '#' 符号个数。

类型：[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Token](ast_package_structs.md#struct-token) 对象，其中 [TokenKind](ast_package_enums.md#enum-tokenkind) 类型为 `ILLEGAL`，`value` 为空字符串，[Position](ast_package_structs.md#struct-position) 成员变量均为 0。

### init(TokenKind)

```cangjie
public init(kind: TokenKind)
```

功能：根据词法单元类型，构造一个默认的 [Token](ast_package_structs.md#struct-token) 对象。

参数：

- kind: [TokenKind](ast_package_enums.md#enum-tokenkind) - 构建词法单元的类型。

### init(TokenKind, String)

```cangjie
public init(kind: TokenKind, value: String)
```

功能：根据词法单元类型 `kind` 和词法单元值 `value`，构造一个 [Token](ast_package_structs.md#struct-token) 对象。

参数：

- kind: [TokenKind](ast_package_enums.md#enum-tokenkind) - 要构建词法单元的类型。
- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要构建词法单元的 `value` 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当输入的 `kind` 与 `value` 不匹配时，抛出异常点。

### func addPosition(UInt32, Int32, Int32)

```cangjie
public func addPosition(fileID: UInt32, line: Int32, colum: Int32): Token
```

功能：补充词法单元的位置信息。

参数：

- fileID: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - [Token](ast_package_structs.md#struct-token) 所在的 fileID。
- line: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - [Token](ast_package_structs.md#struct-token) 所在的行号。
- colum: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - [Token](ast_package_structs.md#struct-token) 所在的列号。

返回值：

- [Token](ast_package_structs.md#struct-token) - 补充完位置信息后的 [Token](ast_package_structs.md#struct-token) 对象。

### func dump()

```cangjie
public func dump(): Unit
```

功能：将 [Token](ast_package_structs.md#struct-token) 的信息打印出来。

### func toBytes()

```cangjie
public func toBytes(): Array<UInt8>
```

功能：Token 类型的序列化。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 序列化后的字节序列。