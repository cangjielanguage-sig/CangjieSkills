## interface QueryResult

```cangjie
public interface QueryResult <: Resource {
    prop columnInfos: Array<ColumnInfo>
    func next(values: Array<SqlDbType>): Bool
    func next(): Bool
    func get<T>(index: Int64): T
    func getOrNull<T>(index: Int64): ?T
}
```

功能：执行 Select 语句产生的结果接口。

继承该接口的 class、interface、struct 也需要遵守该接口中函数的入参及返回值定义。

父类型：

- [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource)

### prop columnInfos

```cangjie
prop columnInfos: Array<ColumnInfo>
```

功能：返回结果集的列信息，比如列名，列类型，列长度，是否允许数据库 Null 值等。

类型：[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[ColumnInfo](database_sql_package_interfaces.md#interface-columninfo)>

### func get\<T>(Int64)

```cangjie
func get<T>(index: Int64): T
```

功能：从结果集的当前行检索指定列的值。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定列。

返回值：

- T - `T` 类型的实例。

### func getOrNull\<T>(Int64)

```cangjie
func getOrNull<T>(index: Int64): ?T
```

功能：从结果集的当前行检索指定列的值，数据库列允许 SQL NULL。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定列。

返回值：

- ?T - `T` 类型的实例，如果为空，返回 None。

异常：

- [SqlException](database_sql_package_exceptions.md#class-sqlexception) - 索引超出列范围，或者行数据未准备好时，抛出异常。

### func next()

```cangjie
func next(): Bool
```

功能：向后移动一行，必须先调用一次 `next()` 才能移动到第一行，第二次调用移动到第二行，依此类推。当返回 `true` 时，驱动会在结果集的当前行填入数据，当返回 `false` 时结束，且不会修改结果集当前行的内容。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 下一行存在数据则返回 `true`，否则返回 `false`。

### func next(Array\<SqlDbType>) <sup>(deprecated)</sup>

```cangjie
func next(values: Array<SqlDbType>): Bool
```

功能：向后移动一行，必须先调用一次 `next` 才能移动到第一行，第二次调用移动到第二行，依此类推。当返回 `true` 时，驱动会在 `values` 中填入行数据；当返回 `false` 时结束，且不会修改 `values` 的内容。

> **注意：**
>
> 未来版本即将废弃不再使用，可使用 [next()](database_sql_package_interfaces.md#func-next) 替代。

参数：

- values: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[SqlDbType <sup>(deprecated)</sup>](database_sql_package_interfaces.md#interface-sqldbtype-deprecated)> - sql 数据类型的数据列表。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 下一行存在数据则返回 `true`，否则返回 `false`。