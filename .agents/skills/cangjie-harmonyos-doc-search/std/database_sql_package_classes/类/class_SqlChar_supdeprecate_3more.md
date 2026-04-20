## class SqlChar <sup>(deprecated)</sup>

```cangjie
public class SqlChar <: SqlDbType {
    public init(v: String)
}
```

功能：定长字符串，对应仓颉 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlChar <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlchar-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: String
```

功能：该数据的值。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### init(String)

```cangjie
public init(v: String)
```

功能：根据传入参数 v 构造一个 [SqlChar <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlchar-deprecated) 实例。

参数：

- v: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 传入的数据。

## class SqlClob <sup>(deprecated)</sup>

```cangjie
public class SqlClob <: SqlDbType {
    public init(v: InputStream)
}
```

功能：变长超大字符串（RUNE LARGE OBJECT），对应仓颉 [InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlClob](database_sql_package_classes.md#class-sqlclob-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: InputStream
```

功能：该数据的值。

类型：[InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream)

### init(InputStream)

```cangjie
public init(v: InputStream)
```

功能：根据传入参数 v 构造一个 [SqlClob](database_sql_package_classes.md#class-sqlclob-deprecated) 实例。

参数：

- v: [InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream) - 传入的数据。

## class SqlDate <sup>(deprecated)</sup>

```cangjie
public class SqlDate <: SqlDbType {
    public init(v: DateTime)
}
```

功能：日期，仅年月日有效，对应仓颉 [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlDate <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqldate-deprecated)。

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

功能：根据传入参数 v 构造一个 [SqlDate <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqldate-deprecated) 实例。

参数：

- v: [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) - 传入的数据。