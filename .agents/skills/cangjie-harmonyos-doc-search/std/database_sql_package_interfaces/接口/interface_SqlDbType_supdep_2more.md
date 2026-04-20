## interface SqlDbType <sup>(deprecated)</sup>

```cangjie
public interface SqlDbType {
    prop name: String
}
```

功能：所有 sql 数据类型的父类。

> **注意：**
>
> 未来版本即将废弃不再使用。

要扩展用户定义的类型，请继承 [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated) 或 [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)。

> **说明：**
>
> [SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated) 接口所有实现类型都必须具有公共 `value` 属性。每种 sql 数据类型实现类，同时满足以下条件：
>
> - 只有一个参数的构造函数，参数类型为 `T`（`T` 为仓颉语言支持的类型）。
> - `public` 修饰的 `value` 属性，其类型必须上一条中使用的参数类型一致，其值为对应仓颉类型的值。
> - 如果数据类型允许 `null` 值，继承 [SqlNullableDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqlnullabledbtype-deprecated)，`null` 值时，`value` 字段的值为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>.None。

### prop name

```cangjie
prop name: String
```

功能：获取类型名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

## interface SqlNullableDbType <sup>(deprecated)</sup>

```cangjie
public interface SqlNullableDbType <: SqlDbType {}
```

功能：允许 `null` 值的 sql 数据类型父类。

> **注意：**
>
> 未来版本即将废弃不再使用。

如果为 `null` 值，`value` 属性值为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont).None。

父类型：

- [SqlDbType <sup>(deprecated)</sup>](#interface-sqldbtype-deprecated)