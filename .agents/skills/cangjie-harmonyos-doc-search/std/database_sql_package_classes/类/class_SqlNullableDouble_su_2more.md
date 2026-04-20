## class SqlNullableDouble <sup>(deprecated)</sup>

```cangjie
public class SqlNullableDouble <: SqlNullableDbType {
    public init(v: ?Float64)
}
```

功能：双精度数，对应仓颉 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableDouble <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabledouble-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?Float64
```

功能：该数据的值。

类型：?[Float64](../../core/core_package_api/core_package_intrinsics.md#float64)

### init(?Float64)

```cangjie
public init(v: ?Float64)
```

功能：根据传入参数 v 构造一个 [SqlNullableDouble <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabledouble-deprecated) 实例。

参数：

- v: ?[Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的数据。

## class SqlNullableInteger <sup>(deprecated)</sup>

```cangjie
public class SqlNullableInteger <: SqlNullableDbType {
    public init(v: ?Int32)
}
```

功能：中整数，对应仓颉 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableInteger <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullableinteger-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?Int32
```

功能：该数据的值。

类型：?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### init(?Int32)

```cangjie
public init(v: ?Int32)
```

功能：根据传入参数 v 构造一个 [SqlNullableInteger <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullableinteger-deprecated) 实例。

参数：

- v: ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入的数据。