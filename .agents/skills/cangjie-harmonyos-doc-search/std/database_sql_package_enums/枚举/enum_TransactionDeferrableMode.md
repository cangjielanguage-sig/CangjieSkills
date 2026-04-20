## enum TransactionDeferrableMode

```cangjie
public enum TransactionDeferrableMode <: ToString & Hashable & Equatable<TransactionDeferrableMode> {
    | Deferrable
    | NotDeferrable
    | Unspecified
}
```

功能：事务的延迟模式。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[TransactionDeferrableMode](#enum-transactiondeferrablemode)>

### Deferrable

```cangjie
Deferrable
```

功能：表示可延迟。

> **说明：**
>
> 延迟事务是指在前滚阶段结束时未提交的事务，并且遇到了阻止其回滚的错误。因为事务无法回滚，所以它被延迟。

### NotDeferrable

```cangjie
NotDeferrable
```

功能：表示不可延迟。

### Unspecified

```cangjie
Unspecified
```

功能：未指定的事务延迟模式，其行为取决于具体的数据库服务器。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取事务延迟模式的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 事务延迟模式的哈希值。

### func toString()

```cangjie
public func toString(): String
```

功能：返回事务延迟模式的字符串表示。枚举值和字符串的对应关系如下表所示：

| 枚举值        | 字符串           |
| ------------- | ---------------- |
| Deferrable    | "Deferrable"     |
| NotDeferrable | "Not Deferrable" |
| Unspecified   | "Unspecified"    |

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 事务延迟模式的字符串。

### operator func !=(TransactionDeferrableMode)

```cangjie
public operator func != (rhs: TransactionDeferrableMode): Bool
```

功能：判断两个 [TransactionDeferrableMode](database_sql_package_enums.md#enum-transactiondeferrablemode) 是否不相等。

参数：

- rhs: [TransactionDeferrableMode](database_sql_package_enums.md#enum-transactiondeferrablemode) - 传入 [TransactionDeferrableMode](database_sql_package_enums.md#enum-transactiondeferrablemode) 的枚举值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果不相等，则返回 `true`，否则返回 `false`。

### operator func ==(TransactionDeferrableMode)

```cangjie
public operator func == (rhs: TransactionDeferrableMode): Bool
```

功能：判断两个 [TransactionDeferrableMode](database_sql_package_enums.md#enum-transactiondeferrablemode) 是否相等。

参数：

- rhs: [TransactionDeferrableMode](database_sql_package_enums.md#enum-transactiondeferrablemode) - 传入 [TransactionDeferrableMode](database_sql_package_enums.md#enum-transactiondeferrablemode) 的枚举值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果相等，则返回 `true`，否则返回 `false`。