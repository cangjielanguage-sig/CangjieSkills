## interface ColumnInfo

```cangjie
public interface ColumnInfo {
    prop displaySize: Int64
    prop length: Int64
    prop name: String
    prop nullable: Bool
    prop scale: Int64
    prop typeName: String
}
```

功能：执行 Select/Query 语句返回结果的列信息。

### prop displaySize

```cangjie
prop displaySize: Int64
```

功能：获取列值的最大显示长度，如果无限制，则应该返回 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64).Max （仍然受数据库的限制）。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop length

```cangjie
prop length: Int64
```

功能：获取列值大小。

> **说明：**
>
> - 对于数值数据，表示最大精度。
> - 对于字符数据，表示以字符为单位的长度。
> - 对于日期时间数据类型，表示字符串表示形式的最大字符长度。
> - 对于二进制数据，表示以字节为单位的长度。
> - 对于 RowID 数据类型，表示以字节为单位的长度。
> - 对于列大小不适用的数据类型，返回 0。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop name

```cangjie
prop name: String
```

功能：列名或者别名。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop nullable

```cangjie
prop nullable: Bool
```

功能：表示列值是否允许数据库 `Null` 值。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

### prop scale

```cangjie
prop scale: Int64
```

功能：获取列值的小数长度，如果无小数部分，返回 0。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop typeName

```cangjie
prop typeName: String
```

功能：获取列类型名称，如果在仓颉中有对应数据类型的定义，返回对应类型的 `toString` 函数的返回值；如果在仓颉中无对应数据类型的定义，由数据库驱动定义。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)