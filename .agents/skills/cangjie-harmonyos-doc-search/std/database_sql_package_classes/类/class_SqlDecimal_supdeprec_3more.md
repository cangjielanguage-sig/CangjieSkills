## class SqlDecimal <sup>(deprecated)</sup>

```cangjie
public class SqlDecimal <: SqlDbType {
    public init(v: Decimal)
}
```

功能：高精度数，对应仓颉 [Decimal](../../math_numeric/math_numeric_package_api/math_numeric_package_structs.md#struct-decimal) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlDecimal <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqldecimal-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: Decimal
```

功能：该数据的值。

类型：[Decimal](../../math_numeric/math_numeric_package_api/math_numeric_package_structs.md#struct-decimal)

### init(Decimal)

```cangjie
public init(v: Decimal)
```

功能：根据传入参数 v 构造一个 [SqlDecimal <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqldecimal-deprecated) 实例。

参数：

- v: [Decimal](../../math_numeric/math_numeric_package_api/math_numeric_package_structs.md#struct-decimal) - 传入的数据。

## class SqlDouble <sup>(deprecated)</sup>

```cangjie
public class SqlDouble <: SqlDbType {
    public init(v: Float64)
}
```

功能：双精度数，对应仓颉 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlDouble <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqldouble-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: Float64
```

功能：该数据的值。

类型：[Float64](../../core/core_package_api/core_package_intrinsics.md#float64)

### init(Float64)

```cangjie
public init(v: Float64)
```

功能：根据传入参数 v 构造一个 [SqlDouble <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqldouble-deprecated) 实例。

参数：

- v: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的数据。

## class SqlInteger <sup>(deprecated)</sup>

```cangjie
public class SqlInteger <: SqlDbType {
    public init(v: Int32)
}
```

功能：中整数，对应仓颉 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlInteger <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlinteger-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: Int32
```

功能：该数据的值。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### init(Int32)

```cangjie
public init(v: Int32)
```

功能：根据传入参数 v 构造一个 [SqlInteger <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlinteger-deprecated) 实例。

参数：

- v: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入的数据。