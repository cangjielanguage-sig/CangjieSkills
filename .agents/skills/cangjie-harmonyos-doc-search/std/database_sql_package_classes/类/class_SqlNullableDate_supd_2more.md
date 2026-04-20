## class SqlNullableDate <sup>(deprecated)</sup>

```cangjie
public class SqlNullableDate <: SqlNullableDbType {
    public init(v: ?DateTime)
}
```

功能：日期，仅年月日有效，对应仓颉 [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableDate <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabledate-deprecated)。

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

功能：根据传入参数 v 构造一个 [SqlNullableDate <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabledate-deprecated) 实例。

参数：

- v: ?[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) - 传入的数据。

## class SqlNullableDecimal <sup>(deprecated)</sup>

```cangjie
public class SqlNullableDecimal <: SqlNullableDbType {
    public init(v: ?Decimal)
}
```

功能：高精度数，对应仓颉 [Decimal](../../math_numeric/math_numeric_package_api/math_numeric_package_structs.md#struct-decimal) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableDecimal <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabledecimal-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?Decimal
```

功能：该数据的值。

类型：?[Decimal](../../math_numeric/math_numeric_package_api/math_numeric_package_structs.md#struct-decimal)

### init(?Decimal)

```cangjie
public init(v: ?Decimal)
```

功能：根据传入参数 v 构造一个 [SqlNullableDecimal <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullabledecimal-deprecated) 实例。

参数：

- v: ?[Decimal](../../math_numeric/math_numeric_package_api/math_numeric_package_structs.md#struct-decimal) - 传入的数据。