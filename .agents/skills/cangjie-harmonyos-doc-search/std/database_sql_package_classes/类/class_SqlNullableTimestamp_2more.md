## class SqlNullableTimestamp <sup>(deprecated)</sup>

```cangjie
public class SqlNullableTimestamp <: SqlNullableDbType {
    public init(v: ?DateTime)
}
```

功能：时间戳，对应仓颉 [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableTimestamp <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabletimestamp-deprecated)。

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

功能：根据传入参数 v 构造一个 [SqlNullableTimestamp <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabletimestamp-deprecated) 实例。

参数：

- v: ?[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) - 传入的数据。

## class SqlNullableTimeTz <sup>(deprecated)</sup>

```cangjie
public class SqlNullableTimeTz <: SqlNullableDbType {
    public init(v: ?DateTime)
}
```

功能：带时区的时间，仅时分秒毫秒时区有效，对应仓颉 [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableTimeTz <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabletimetz-deprecated)。

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

功能：根据传入参数 v 构造一个 [SqlNullableTimeTz <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabletimetz-deprecated) 实例。

参数：

- v: ?[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) - 传入的数据。