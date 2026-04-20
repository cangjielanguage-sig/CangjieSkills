## class PooledDatasource

```cangjie
public class PooledDatasource <: Datasource {
    public init(datasource: Datasource)
}
```

功能：数据库连接池类，提供数据库连接池能力。

父类型：

- [Datasource](database_sql_package_interfaces.md#interface-datasource)

### prop connectionTimeout

```cangjie
public mut prop connectionTimeout: Duration
```

功能：从池中获取连接的超时时间。

类型：[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当该属性被设置为 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration).Max 或 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration).Min 时，抛此异常。
- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当获取连接超时后，抛出此异常。

### prop idleTimeout

```cangjie
public mut prop idleTimeout: Duration
```

功能：允许连接在池中闲置的最长时间，超过这个时间的空闲连接可能会被回收。

类型：[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### prop keepaliveTime

```cangjie
public mut prop keepaliveTime: Duration
```

功能：检查空闲连接健康状况的间隔时间，防止它被数据库或网络基础设施超时。

类型：[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### prop maxIdleSize

```cangjie
public mut prop maxIdleSize: Int32
```

功能：最大空闲连接数量，超过这个数量的空闲连接会被关闭，负数或 0 表示无限制。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### prop maxLifeTime

```cangjie
public mut prop maxLifeTime: Duration
```

功能：自连接创建以来的最大持续时间，在该持续时间之后，连接将自动关闭。

类型：[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### prop maxSize

```cangjie
public mut prop maxSize: Int32
```

功能：连接池最大连接数量，负数或 0 表示无限制。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### init(Datasource)

```cangjie
public init(datasource: Datasource)
```

功能：通过数据源 datasource 构造一个 [PooledDatasource](database_sql_package_classes.md#class-pooleddatasource) 实例，入参必须为 [Datasource](database_sql_package_interfaces.md#interface-datasource) 对象。

参数：

- datasource: [Datasource](database_sql_package_interfaces.md#interface-datasource) - 数据源。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭连接池中的所有连接并阻止其他连接请求。调用该方法会阻塞至所有连接关闭并归还到连接池。

### func connect()

```cangjie
public func connect(): Connection
```

功能：获取一个连接。

返回值：

- [Connection](./database_sql_package_interfaces.md#interface-connection) - 获取到的连接。

### func isClosed()

```cangjie
public func isClosed(): Bool
```

功能：判断连接是否关闭。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 连接是否关闭。

### func setOption(String, String)

```cangjie
public func setOption(key: String, value: String): Unit
```

功能：设置数据库驱动连接选项（公钥在 [SqlOption](database_sql_package_classes.md#class-sqloption) 中预定义）。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 连接选项名称。
- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 连接选项的值。