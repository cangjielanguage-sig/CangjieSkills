### operator func !=(PackageInfo)

```cangjie
public operator func !=(that: PackageInfo): Bool
```

功能：判断该包信息与给定的另一个包信息是否不等。

> **注意：**
>
> 内部实现为比较两个包信息的限定名称是否相等。

参数：

- that: [PackageInfo](reflect_package_classes.md#class-packageinfo) - 被比较相等性的另一个包信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该包信息与 `that` 不等则返回 `true`，否则返回 `false`。

### operator func ==(PackageInfo)

```cangjie
public operator func ==(that: PackageInfo): Bool
```

功能：判断该包信息与给定的另一个包信息是否相等。

> **注意：**
>
> 内部实现为比较两个包信息的限定名称是否相等。

参数：

- that: [PackageInfo](reflect_package_classes.md#class-packageinfo) - 被比较相等性的另一个包信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该包信息与 `that` 相等则返回 `true`，否则返回 `false`。