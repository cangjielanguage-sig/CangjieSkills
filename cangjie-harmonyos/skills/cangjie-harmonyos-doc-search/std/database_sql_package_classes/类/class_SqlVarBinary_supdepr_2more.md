## class SqlVarBinary <sup>(deprecated)</sup>

```cangjie
public class SqlVarBinary <: SqlDbType {
    public init(v: Array<Byte>)
}
```

功能：变长二进制字符串，对应仓颉 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlVarBinary <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlvarbinary-deprecated)。

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

功能：根据传入参数 v 构造一个 [SqlVarBinary <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlvarbinary-deprecated) 实例。

参数：

- v: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 传入的数据。

## class SqlVarchar <sup>(deprecated)</sup>

```cangjie
public class SqlVarchar <: SqlDbType {
    public init(v: String)
}
```

功能：变长字符串，对应仓颉 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlVarchar  <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlvarchar-deprecated)。

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

功能：根据传入参数 v 构造一个 [SqlVarchar  <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlvarchar-deprecated) 实例。

参数：

- v: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 传入的数据。