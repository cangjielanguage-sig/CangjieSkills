## class SqlNullableInterval <sup>(deprecated)</sup>

```cangjie
public class SqlNullableInterval <: SqlNullableDbType {
    public init(v: ?Duration)
}
```

功能：时间间隔，对应仓颉 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableInterval <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullableinterval-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?Duration
```

功能：该数据的值。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### init(?Duration)

```cangjie
public init(v: ?Duration)
```

功能：根据传入参数 v 构造一个 [SqlNullableInterval <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullableinterval-deprecated) 实例。

参数：

- v: ?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 传入的数据。

## class SqlNullableReal <sup>(deprecated)</sup>

```cangjie
public class SqlNullableReal <: SqlNullableDbType {
    public init(v: ?Float32)
}
```

功能：浮点数，对应仓颉 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableReal <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablereal-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?Float32
```

功能：该数据的值。

类型：?[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)

### init(?Float32)

```cangjie
public init(v: ?Float32)
```

功能：根据传入参数 v 构造一个 [SqlNullableReal <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablereal-deprecated) 实例。

参数：

- v: ?[Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的数据。