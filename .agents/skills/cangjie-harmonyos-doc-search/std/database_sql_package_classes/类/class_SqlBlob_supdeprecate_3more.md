## class SqlBlob <sup>(deprecated)</sup>

```cangjie
public class SqlBlob <: SqlDbType {
    public init(v: InputStream)
}
```

功能：变长超大二进制字符串（BINARY LARGE OBJECT），对应仓颉 [InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlBlob <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlblob-deprecated)。

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

功能：根据传入参数 v 构造一个 [SqlBlob <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlblob-deprecated) 实例。

参数：

- v: [InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream) - 传入的数据。

## class SqlBool <sup>(deprecated)</sup>

```cangjie
public class SqlBool <: SqlDbType {
    public init(v: Bool)
}
```

功能：布尔类型，对应仓颉 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlBool<sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlbool-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: Bool
```

功能：该数据的值。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

### init(Bool)

```cangjie
public init(v: Bool)
```

功能：根据传入参数 v 构造一个 [SqlBool<sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlbool-deprecated) 实例。

参数：

- v: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传入的数据。

## class SqlByte <sup>(deprecated)</sup>

```cangjie
public class SqlByte <: SqlDbType {
    public init(v: Int8)
}
```

功能：字节，对应仓颉 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型。

> **注意：**
>
> 未来版本即将废弃不再使用，使用仓颉原生类型替代。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)

### prop name

```cangjie
public prop name: String
```

功能：类型名称，即 [SqlByte <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlbyte-deprecated)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop value

```cangjie
public mut prop value: Int8
```

功能：该数据的值。

类型：[Int8](../../core/core_package_api/core_package_intrinsics.md#int8)

### init(Int8)

```cangjie
public init(v: Int8)
```

功能：根据传入参数 v 构造一个 [SqlByte <sup>(deprecated)</sup>](database_sql_package_classes.md#class-sqlbyte-deprecated) 实例。

参数：

- v: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入的数据。