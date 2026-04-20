## enum TransactionAccessMode

```cangjie
public enum TransactionAccessMode <: ToString & Hashable & Equatable<TransactionAccessMode> {
    | ReadOnly
    | ReadWrite
    | Unspecified
}
```

功能：事务读写模式。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[TransactionAccessMode](#enum-transactionaccessmode)>

### ReadOnly

```cangjie
ReadOnly
```

功能：表示只读模式。

### ReadWrite

```cangjie
ReadWrite
```

功能：表示读 + 写模式。

### Unspecified

```cangjie
Unspecified
```

功能：表示未指定的事务读写模式。其行为取决于具体的数据库服务器。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取事务读写模式的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 事务读写模式的哈希值。

### func toString()

```cangjie
public func toString(): String
```

功能：返回事务读写模式的字符串表示。枚举值和字符串的对应关系如下表所示：

| 枚举值      | 字符串        |
| ----------- | ------------- |
| ReadOnly    | "Read Only"   |
| ReadWrite   | "Read Write"  |
| Unspecified | "Unspecified" |

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 事务读写模式的字符串。

### operator func !=(TransactionAccessMode)

```cangjie
public operator func != (rhs: TransactionAccessMode): Bool
```

功能：判断两个 [TransactionAccessMode](database_sql_package_enums.md#enum-transactionaccessmode) 是否不相等。

参数：

- rhs: [TransactionAccessMode](database_sql_package_enums.md#enum-transactionaccessmode) - 传入 [TransactionAccessMode](database_sql_package_enums.md#enum-transactionaccessmode) 的枚举值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果不相等，则返回 `true`，否则返回 `false`。

### operator func ==(TransactionAccessMode)

```cangjie
public operator func == (rhs: TransactionAccessMode): Bool
```

功能：判断两个 [TransactionAccessMode](database_sql_package_enums.md#enum-transactionaccessmode) 是否相等。

参数：

- rhs: [TransactionAccessMode](database_sql_package_enums.md#enum-transactionaccessmode) - 传入 [TransactionAccessMode](database_sql_package_enums.md#enum-transactionaccessmode) 的枚举值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果相等，则返回 `true`，否则返回 `false`。