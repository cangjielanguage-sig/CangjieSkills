### func update(Array\<SqlDbType>) <sup>(deprecated)</sup>

```cangjie
func update(params: Array<SqlDbType>): UpdateResult
```

功能：执行 sql 语句，得到更新结果。

> **注意：**
>
> 未来版本即将废弃不再使用，可使用 update() 替代。

参数：

- params: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)> - sql 数据类型的数据列表，用于替换 sql 语句中的 `?` 占位符。

返回值：

- [UpdateResult](database_sql_package_interfaces.md#interface-updateresult) - 更新结果。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当执行过程中发生了异常情况，比如网络中断、服务器超时，参数个数不正确时，抛出异常。