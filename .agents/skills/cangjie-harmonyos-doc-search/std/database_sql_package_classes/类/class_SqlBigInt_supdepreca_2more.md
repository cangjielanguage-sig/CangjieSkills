## class SqlBigInt <sup>(deprecated)</sup>

```cangjie
public class SqlBigInt <: SqlDbType {
    public init(v: Int64)
}
```

功能：大整数，对应仓颉 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlBigInt <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlbigint-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: Int64
```

功能：该数据的值。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init(Int64)

```cangjie
public init(v: Int64)
```

功能：根据传入参数 v 构造一个 [SqlBigInt <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlbigint-deprecated) 实例。

参数：

- v: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的数据。

## class SqlBinary <sup>(deprecated)</sup>

```cangjie
public class SqlBinary <: SqlDbType {
    public init(v: Array<Byte>)
}
```

功能：定长二进制字符串，对应仓颉 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlBinary <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlbinary-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: Array<Byte>
```

功能：该数据的值。

类型：[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)>

### init(Array\<Byte>)

```cangjie
public init(v: Array<Byte>)
```

功能：根据传入参数 v 构造一个 [SqlBinary <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlbinary-deprecated) 实例。

参数：

- v: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 传入的数据。