## enum ConnectionState

```cangjie
public enum ConnectionState <: Equatable<ConnectionState> {
    | Broken
    | Closed
    | Connecting
    | Connected
}
```

功能：描述与数据源连接的当前状态。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[ConnectionState](#enum-connectionstate)>

### Broken

```cangjie
Broken
```

功能：表示与数据源的连接已中断。只有在 Connected 之后才可能发生这种情况。

### Closed

```cangjie
Closed
```

功能：表示连接对象已关闭。

### Connected

```cangjie
Connected
```

功能：表示连接对象已与数据源连接上。

### Connecting

```cangjie
Connecting
```

功能：表示连接对象正在与数据源连接。

### operator func !=(ConnectionState)

```cangjie
public operator func !=(rhs: ConnectionState): Bool
```

功能：判断数据源连接状态是否不同。

参数：

- rhs: [ConnectionState](database_sql_package_enums.md#enum-connectionstate) - 数据源连接状态。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传入数据源连接状态与当前状态相同则返回 `false` ，否则返回 `true`。

### operator func ==(ConnectionState)

```cangjie
public operator func ==(rhs: ConnectionState): Bool
```

功能：判断数据源连接状态是否相同。

参数：

- rhs: [ConnectionState](database_sql_package_enums.md#enum-connectionstate) - 数据源连接状态。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传入数据源连接状态与当前状态相同则返回 `true` ，否则返回 `false`。