## interface Transaction

```cangjie
public interface Transaction {
    mut prop accessMode: TransactionAccessMode
    mut prop deferrableMode: TransactionDeferrableMode
    mut prop isoLevel: TransactionIsoLevel
    func begin(): Unit
    func commit(): Unit
    func release(savePointName: String): Unit
    func rollback(): Unit
    func rollback(savePointName: String): Unit
    func save(savePointName: String): Unit
}
```

功能：定义数据库事务的核心行为。

继承该接口的 class、interface、struct 也需要遵守该接口中函数的入参及返回值定义。

### prop accessMode

```cangjie
mut prop accessMode: TransactionAccessMode
```

功能：获取数据库事务访问模式。

类型：[TransactionAccessMode](database_sql_package_enums.md#enum-transactionaccessmode)

### prop deferrableMode

```cangjie
mut prop deferrableMode: TransactionDeferrableMode
```

功能：获取数据库事务延迟模式。

类型：[TransactionDeferrableMode](database_sql_package_enums.md#enum-transactiondeferrablemode)

### prop isoLevel

```cangjie
mut prop isoLevel: TransactionIsoLevel
```

功能：获取数据库事务隔离级别。

类型：[TransactionIsoLevel](database_sql_package_enums.md#enum-transactionisolevel)

### func begin()

```cangjie
func begin(): Unit
```

功能：开始数据库事务。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当提交事务时服务器端发生错误，以及当事务已提交或回滚或连接已断开时，抛出异常。

### func commit()

```cangjie
func commit(): Unit
```

功能：提交数据库事务。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当提交事务时服务器端发生错误，以及当事务已提交或回滚或连接已断开时，抛出异常。

### func release(String)

```cangjie
func release(savePointName: String): Unit
```

功能：销毁先前在当前事务中定义的保存点。这允许系统在事务结束之前回收一些资源。

参数：

- savePointName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 保存点名称。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当提交事务时服务器端发生错误，以及当事务已提交或回滚或连接已断开时，抛出异常。

### func rollback()

```cangjie
func rollback(): Unit
```

功能：从挂起状态回滚事务。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当提交事务时服务器端发生错误，以及当事务已提交或回滚或连接已断开时，抛出异常。

### func rollback(String)

```cangjie
func rollback(savePointName: String): Unit
```

功能：回滚事务至指定保存点名称。

参数：

- savePointName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 保存点名称。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当提交事务时服务器端发生错误，以及当事务已提交或回滚或连接已断开时，抛出异常。

### func save(String)

```cangjie
func save(savePointName: String): Unit
```

功能：在事务中创建一个指定名称的保存点，可用于回滚此保存点之后的事务。

参数：

- savePointName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 保存点名称。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当提交事务时服务器端发生错误，以及当事务已提交或回滚或连接已断开时，抛出异常。