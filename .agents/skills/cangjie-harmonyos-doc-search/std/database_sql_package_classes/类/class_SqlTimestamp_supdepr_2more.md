## class SqlTimestamp <sup>(deprecated)</sup>

```cangjie
public class SqlTimestamp <: SqlDbType {
    public init(v: DateTime)
}
```

功能：时间戳，对应仓颉 [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlTimestamp <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqltimestamp-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: DateTime
```

功能：该数据的值。

类型：[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime)

### init(DateTime)

```cangjie
public init(v: DateTime)
```

功能：根据传入参数 v 构造一个 [SqlTimestamp <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqltimestamp-deprecated) 实例。

参数：

- v: [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) - 传入的数据。

## class SqlTimeTz <sup>(deprecated)</sup>

```cangjie
public class SqlTimeTz <: SqlDbType {
    public init(v: DateTime)
}
```

功能：带时区的时间，仅时分秒毫秒时区有效，对应仓颉 [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlTimeTz <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqltimetz-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: DateTime
```

功能：该数据的值。

类型：[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime)

### init(DateTime)

```cangjie
public init(v: DateTime)
```

功能：根据传入参数 v 构造一个 [SqlTimeTz <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqltimetz-deprecated) 实例。

参数：

- v: [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) - 传入的数据。