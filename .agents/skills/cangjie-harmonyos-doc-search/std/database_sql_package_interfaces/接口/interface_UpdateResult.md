## interface UpdateResult

```cangjie
public interface UpdateResult {
    prop lastInsertId: Int64
    prop rowCount: Int64
}
```

功能：执行 Insert、Update、Delete 语句产生的结果接口。

继承该接口的 class、interface、struct 也需要遵守该接口中函数的入参及返回值定义。

### prop lastInsertId

```cangjie
prop lastInsertId: Int64
```

功能：执行 Insert 语句自动生成的最后 row ID ，如果不支持则 row ID 为 0。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop rowCount

```cangjie
prop rowCount: Int64
```

功能：执行 Insert、Update、Delete 语句影响的行数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)