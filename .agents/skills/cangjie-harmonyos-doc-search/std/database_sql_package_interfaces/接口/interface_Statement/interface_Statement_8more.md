## interface Statement

```cangjie
public interface Statement <: Resource {
    prop parameterColumnInfos: Array<ColumnInfo>
    func query(params: Array<SqlDbType>): QueryResult
    func setOption(key: String, value: String): Unit
    func update(params: Array<SqlDbType>): UpdateResult
    func set<T>(index: Int64, value: T): Unit
    func setNull(index: Int64): Unit
    func update(): UpdateResult
    func query(): QueryResult
}
```

功能：sql 语句预执行接口。

[Statement](database_sql_package_interfaces.md#interface-statement) 绑定了一个 [Connection](database_sql_package_interfaces.md#interface-connection) ，继承该接口的 class、interface、struct 也需要遵守该接口中函数的入参及返回值定义。

父类型：

- [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource)

### prop parameterColumnInfos

```cangjie
prop parameterColumnInfos: Array<ColumnInfo>
```

功能：预执行 sql 语句中，占位参数的列信息，比如列名，列类型，列长度，是否允许数据库 `Null` 值等。

类型：[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[ColumnInfo](database_sql_package_interfaces.md#interface-columninfo)>

### func query()

```cangjie
func query(): QueryResult
```

功能：执行 sql 语句，得到查询结果。

返回值：

- [QueryResult](database_sql_package_interfaces.md#interface-queryresult) - 查询结果。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当执行过程中发生了异常情况，比如网络中断，服务器超时，参数个数不正确时，抛出异常。

### func query(Array\<SqlDbType>) <sup>(deprecated)</sup>

```cangjie
func query(params: Array<SqlDbType>): QueryResult
```

功能：执行 sql 语句，得到查询结果。

> **注意：**
>
> 未来版本即将废弃不再使用，可使用 query() 替代。

参数：

- params: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)> - sql 数据类型的数据列表，用于替换 sql 语句中的 `?` 占位符。

返回值：

- [QueryResult](database_sql_package_interfaces.md#interface-queryresult) - 查询结果。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当执行过程中发生了异常情况，比如网络中断，服务器超时，参数个数不正确时，抛出异常。

### func set\<T>(Int64, T)

```cangjie
func set<T>(index: Int64, value: T): Unit
```

功能：设置 sql 参数，将仓颉的数据类型转成数据库的数据类型。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 参数所在序列。
- value: T - 参数值。

### func setNull(Int64)

```cangjie
func setNull(index: Int64): Unit
```

功能：将指定位置处的语句参数设置为 SQL NULL。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 参数所在序列。

### func setOption(String, String)

```cangjie
func setOption(key: String, value: String): Unit
```

功能：设置预执行 sql 语句选项。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 连接选项名称。
- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 连接选项的值。

### func update()

```cangjie
func update(): UpdateResult
```

功能：执行 sql 语句，得到更新结果。

返回值：

- [UpdateResult](database_sql_package_interfaces.md#interface-updateresult) - 更新结果。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当执行过程中发生了异常情况，比如网络中断，服务器超时，参数个数不正确时，抛出异常。