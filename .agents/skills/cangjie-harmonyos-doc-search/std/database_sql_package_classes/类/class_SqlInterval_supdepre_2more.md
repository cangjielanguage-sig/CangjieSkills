## class SqlInterval <sup>(deprecated)</sup>

```cangjie
public class SqlInterval <: SqlDbType {
    public init(v: Duration)
}
```

功能：时间间隔，对应仓颉 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlInterval <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlinterval-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: Duration
```

功能：该数据的值。

类型：[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### init(Duration)

```cangjie
public init(v: Duration)
```

功能：根据传入参数 v 构造一个 [SqlInterval <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlinterval-deprecated) 实例。

参数：

- v: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 传入的数据。

## class SqlNullableBigInt <sup>(deprecated)</sup>

```cangjie
public class SqlNullableBigInt <: SqlNullableDbType {
    public init(v: ?Int64)
}
```

功能：大整数，对应仓颉 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableBigInt <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablebigint-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?Int64
```

功能：该数据的值。

类型：?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init(?Int64)

```cangjie
public init(v: ?Int64)
```

功能：根据传入参数 v 构造一个 [SqlNullableBigInt <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablebigint-deprecated) 实例。

参数：

- v: ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的数据。