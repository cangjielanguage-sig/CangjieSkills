## class SqlNullableSmallInt <sup>(deprecated)</sup>

```cangjie
public class SqlNullableSmallInt <: SqlNullableDbType {
    public init(v: ?Int16)
}
```

功能：小整数，对应仓颉 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableSmallInt <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablesmallint-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?Int16
```

功能：该数据的值。

类型：?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16)

### init(?Int16)

```cangjie
public init(v: ?Int16)
```

功能：根据传入参数 v 构造一个 [SqlNullableSmallInt <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablesmallint-deprecated) 实例。

参数：

- v: ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入的数据。

## class SqlNullableTime <sup>(deprecated)</sup>

```cangjie
public class SqlNullableTime <: SqlNullableDbType {
    public init(v: ?DateTime)
}
```

功能：时间，仅时分秒毫秒有效，对应仓颉 [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableTime <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabletime-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?DateTime
```

功能：该数据的值。

类型：?[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime)

### init(?DateTime)

```cangjie
public init(v: ?DateTime)
```

功能：根据传入参数 v 构造一个 [SqlNullableTime <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabletime-deprecated) 实例。

参数：

- v: ?[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) - 传入的数据。