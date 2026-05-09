## class SqlNullableChar <sup>(deprecated)</sup>

```cangjie
public class SqlNullableChar <: SqlNullableDbType {
    public init(v: ?String)
}
```

功能：定长字符串，对应仓颉 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableChar <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablechar-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?String
```

功能：该数据的值。

类型：?[String](../../core/core_package_api/core_package_structs.md#struct-string)

### init(?String)

```cangjie
public init(v: ?String)
```

功能：根据传入参数 v 构造一个 [SqlNullableChar <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablechar-deprecated) 实例。

参数：

- v: ?[String](../../core/core_package_api/core_package_structs.md#struct-string) - 传入的数据。

## class SqlNullableClob <sup>(deprecated)</sup>

```cangjie
public class SqlNullableClob <: SqlNullableDbType {
    public init(v: ?InputStream)
}
```

功能：变长超大字符串（RUNE LARGE OBJECT），对应仓颉 [InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableClob <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullableclob-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?InputStream
```

功能：该数据的值。

类型：?[InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream)

### init(?InputStream)

```cangjie
public init(v: ?InputStream)
```

功能：根据传入参数 v 构造一个 [SqlNullableClob <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullableclob-deprecated) 实例。

参数：

- v: ?[InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream) - 传入的数据。