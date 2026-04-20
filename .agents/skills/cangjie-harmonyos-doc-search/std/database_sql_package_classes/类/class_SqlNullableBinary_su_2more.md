## class SqlNullableBinary <sup>(deprecated)</sup>

```cangjie
public class SqlNullableBinary <: SqlNullableDbType {
    public init(v: ?Array<Byte>)
}
```

功能：定长二进制字符串，对应仓颉 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableBinary <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablebinary-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: ?Array<Byte>
```

功能：该数据的值。

类型：?[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)>

### init(?Array\<Byte>)

```cangjie
public init(v: ?Array<Byte>)
```

功能：根据传入参数 v 构造一个 [SqlNullableBinary <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullablebinary-deprecated) 实例。

参数：

- v: ?[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 传入的数据。

## class SqlNullableBlob <sup>(deprecated)</sup>

```cangjie
public class SqlNullableBlob <: SqlNullableDbType {
    public init(v: ?InputStream)
}
```

功能：变长超大二进制字符串（BINARY LARGE OBJECT），对应仓颉 [InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream) 类型，可为数据库 `Null` 值。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlNullableBlob <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullableblob-deprecated)。

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

功能：根据传入参数 v 构造一个 [SqlNullableBlob <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlnullableblob-deprecated) 实例。

参数：

- v: ?[InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream) - 传入的数据。