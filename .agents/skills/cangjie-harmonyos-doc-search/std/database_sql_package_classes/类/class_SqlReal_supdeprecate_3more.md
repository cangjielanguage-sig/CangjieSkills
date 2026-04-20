## class SqlReal <sup>(deprecated)</sup>

```cangjie
public class SqlReal <: SqlDbType {
    public init(v: Float32)
}
```

功能：浮点数，对应仓颉 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlReal <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlreal-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: Float32
```

功能：该数据的值。

类型：[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)

### init(Float32)

```cangjie
public init(v: Float32)
```

功能：根据传入参数 v 构造一个 [SqlReal <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlreal-deprecated) 实例。

参数：

- v: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的数据。

## class SqlSmallInt <sup>(deprecated)</sup>

```cangjie
public class SqlSmallInt <: SqlDbType {
    public init(v: Int16)
}
```

功能：小整数，对应仓颉 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlSmallInt <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlsmallint-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: Int16
```

功能：该数据的值。

类型：[Int16](../../core/core_package_api/core_package_intrinsics.md#int16)

### init(Int16)

```cangjie
public init(v: Int16)
```

功能：根据传入参数 v 构造一个 [SqlSmallInt <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlsmallint-deprecated) 实例。

参数：

- v: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入的数据。

## class SqlTime <sup>(deprecated)</sup>

```cangjie
public class SqlTime <: SqlDbType {
    public init(v: DateTime)
}
```

功能：时间，仅时分秒毫秒有效，对应仓颉 [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlTime <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqltime-deprecated)。

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

功能：根据传入参数 v 构造一个 [SqlTime <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqltime-deprecated) 实例。

参数：

- v: [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime) - 传入的数据。