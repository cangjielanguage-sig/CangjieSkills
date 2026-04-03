## struct Position

```cangjie
public struct Position <: ToBytes {
    public let column: Int32
    public let fileID: UInt32
    public let line: Int32
    public init()
    public init(fileID: UInt32, line: Int32, column: Int32)
}
```

功能：表示位置信息的数据结构，包含文件 ID、行号和列号。

父类型：

- [ToBytes](ast_package_interfaces.md#interface-tobytes)

### let column

```cangjie
public let column: Int32
```

功能：获取列号信息。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### let fileID

```cangjie
public let fileID: UInt32
```

功能：获取文件 ID 信息。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

### let line

```cangjie
public let line: Int32
```

功能：获取行号信息。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Position](ast_package_structs.md#struct-position) 实例，其中 `fileID`、`line`、`column` 成员变量均为 `0`。

### init(UInt32, Int32, Int32)

```cangjie
public init(fileID: UInt32, line: Int32, column: Int32)
```

功能：构造一个 [Position](ast_package_structs.md#struct-position) 实例。

参数：

- fileID: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 文件 ID。
- line: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 行号。
- column: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 列号。

### func dump()

```cangjie
public func dump(): Unit
```

功能：将 [Position](ast_package_structs.md#struct-position) 的信息打印出来。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断行号和列号是否同时为 `0`。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当行号和列号为 `0` 时返回 true。

### func toBytes()

```cangjie
public func toBytes(): Array<UInt8>
```

功能：Position 类型的序列化。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 序列化后的字节序列。

### operator func !=(Position)

```cangjie
public operator func !=(r: Position): Bool
```

功能：比较两个 [Position](ast_package_structs.md#struct-position) 实例是否不等。

参数：

- r: [Position](ast_package_structs.md#struct-position) - 与当前位置比较的另一个位置实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当两个 [Position](ast_package_structs.md#struct-position) 实例不完全相等时返回 true。

### operator func ==(Position)

```cangjie
public operator func ==(r: Position): Bool
```

功能：比较两个 [Position](ast_package_structs.md#struct-position) 实例是否相等。

参数：

- r: [Position](ast_package_structs.md#struct-position) - 与当前位置比较的另一个位置实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当两个 [Position](ast_package_structs.md#struct-position) 实例完全相等时返回 true。