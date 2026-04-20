## class SqlNullableBool <sup>(deprecated)</sup>

```cangjie
public class SqlNullableBool <: SqlNullableDbType {
    public init(v: ?Bool)
}
```

功能：布尔类型，对应仓颉 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableBool <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablebool-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?Bool
```

功能：该数据的值。

类型：?[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

### init(?Bool)

```cangjie
public init(v: ?Bool)
```

功能：根据传入参数 v 构造一个 [SqlNullableBool <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablebool-deprecated) 实例。

参数：

- v: ?[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传入的数据。

## class SqlNullableByte <sup>(deprecated)</sup>

```cangjie
public class SqlNullableByte <: SqlNullableDbType {
    public init(v: ?Int8)
}
```

功能：字节，对应仓颉 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableByte <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablebyte-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?Int8
```

功能：该数据的值。

类型：?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8)

### init(?Int8)

```cangjie
public init(v: ?Int8)
```

功能：根据传入参数 v 构造一个 [SqlNullableByte <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablebyte-deprecated) 实例。

参数：

- v: ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入的数据。