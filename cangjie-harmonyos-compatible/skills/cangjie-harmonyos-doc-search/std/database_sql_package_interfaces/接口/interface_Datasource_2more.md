## interface Datasource

```cangjie
public interface Datasource <: Resource {
    func connect(): Connection
    func setOption(key: String, value: String): Unit
}
```

功能：数据源接口。

继承该接口的 class、interface、struct 也需要遵守该接口中函数的入参及返回值定义。

父类型：

- [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource)

### func connect()

```cangjie
func connect(): Connection
```

功能：返回一个可用的连接。

返回值：

- [Connection](database_sql_package_interfaces.md#interface-connection) - 数据库连接实例。

### func setOption(String, String)

```cangjie
func setOption(key: String, value: String): Unit
```

功能：设置连接选项。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 连接选项名称。
- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 连接选项的值。

## interface Driver

```cangjie
public interface Driver {
    prop name: String
    prop preferredPooling: Bool
    prop version: String
    func open(connectionString: String, opts: Array<(String, String)>): Datasource
}
```

功能：数据库驱动接口。

继承该接口的 class、interface、struct 也需要遵守该接口中函数的入参及返回值定义。

### prop name

```cangjie
prop name: String
```

功能：驱动名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop preferredPooling

```cangjie
prop preferredPooling: Bool
```

功能：指示驱动程序是否与连接池亲和。

当该属性为 `false` 时，不建议使用连接池进行管理。例如，对于某些数据库驱动（如 SQLite），连接池化的收益不明显，因此不建议使用连接池。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

### prop version

```cangjie
prop version: String
```

功能：驱动版本。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### func open(String, Array\<(String, String)>)

```cangjie
func open(connectionString: String, opts: Array<(String, String)>): Datasource
```

功能：通过 `connectionString` 和选项打开数据源。

参数：

- connectionString: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 数据库连接字符串。
- opts: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<([String](../../core/core_package_api/core_package_structs.md#struct-string), [String](../../core/core_package_api/core_package_structs.md#struct-string))> - key，value 的 tuple 数组，打开数据源的选项。

返回值：

- [Datasource](database_sql_package_interfaces.md#interface-datasource) - 数据源实例。