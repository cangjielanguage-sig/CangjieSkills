## class DriverManager

```cangjie
public class DriverManager {}
```

功能：支持运行时根据驱动名获取数据库驱动实例。

### static func deregister(String)

```cangjie
public static func deregister(driverName: String): Unit
```

功能：按名称取消注册数据库驱动（如果存在）。本函数并发安全。

参数：

- driverName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 驱动名称。

### static func drivers()

```cangjie
public static func drivers(): Array<String>
```

功能：返回已注册数据库驱动名称的列表（名称已按照字典序排序）。本方法并发安全。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 数据库驱动名称的列表。

### static func getDriver(String)

```cangjie
public static func getDriver(driverName: String): Option<Driver>
```

功能：按名称获取已注册的数据库驱动，如果不存在返回 `None`。本函数并发安全。

参数：

- driverName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 驱动名称。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Driver](database_sql_package_interfaces.md#interface-driver)> - 若驱动存在则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 包装的驱动实例，否则返回 `None`。

### static func register(String, Driver)

```cangjie
public static func register(driverName: String, driver: Driver): Unit
```

功能：按名称和驱动实例注册数据库驱动，名称和实例一一对应。本方法并发安全。

参数：

- driverName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 驱动名称。
- driver: [Driver](database_sql_package_interfaces.md#interface-driver) - 驱动实例。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 当指定的驱动名称已经存在时，抛出异常。