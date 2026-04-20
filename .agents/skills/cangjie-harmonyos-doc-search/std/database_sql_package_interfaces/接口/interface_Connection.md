## interface Connection

```cangjie
public interface Connection <: Resource {
    prop state: ConnectionState
    func createTransaction(): Transaction
    func getMetaData(): Map<String, String>
    func prepareStatement(sql: String): Statement
}
```

功能：数据库连接接口。

继承该接口的 class、interface、struct 也需要遵守该接口中函数的入参及返回值定义。

父类型：

- [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource)

### prop state

```cangjie
prop state: ConnectionState
```

功能：描述与数据源连接的当前状态。

类型：[ConnectionState](database_sql_package_enums.md#enum-connectionstate)

### func createTransaction()

```cangjie
func createTransaction(): Transaction
```

功能：创建事务对象。

返回值：

- [Transaction](database_sql_package_interfaces.md#interface-transaction) - 事务对象。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当已经处于事务状态，不支持并行事务时，抛出异常。

### func getMetaData()

```cangjie
func getMetaData(): Map<String, String>
```

功能：返回连接到的数据源元数据。

返回值：

- [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v)\<[String](../../core/core_package_api/core_package_structs.md#struct-string), [String](../../core/core_package_api/core_package_structs.md#struct-string)> - 数据源元数据。

### func prepareStatement(String)

```cangjie
func prepareStatement(sql: String): Statement
```

功能：通过传入的 sql 语句，返回一个预执行的 [Statement](database_sql_package_interfaces.md#interface-statement) 对象实例。

参数：

- sql: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 预执行的 sql 语句，sql 语句的参数只支持 `?` 符号占位符。

返回值：

- [Statement](database_sql_package_interfaces.md#interface-statement) - 一个可以执行 sql 语句的实例对象。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当 sql 语句包含不认识的字符时，抛出异常。