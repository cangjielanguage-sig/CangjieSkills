### func findAnnotation\<T>() where T <: Annotation

```cangjie
public func findAnnotation<T>(): Option<T> where T <: Annotation
```

功能：尝试获取拥有给定限定名称且作用于该对象的注解。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 如果成功匹配则返回该注解，重复标注或者无法匹配时返回 `None`。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取该全局函数信息的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 该全局函数信息的哈希值。

### func toString()

```cangjie
public func toString(): String
```

功能：获取字符串形式的该全局函数信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的该全局函数信息。

### operator func !=(GlobalFunctionInfo)

```cangjie
public operator func !=(that: GlobalFunctionInfo): Bool
```

功能：判断该全局函数信息与给定的另一个全局函数信息是否不等。

参数：

- that: [GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo) - 被比较相等性的另一个全局函数信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该全局函数信息与 `that` 不等则返回 `true`，否则返回 `false`。

### operator func ==(GlobalFunctionInfo)

```cangjie
public operator func ==(that: GlobalFunctionInfo): Bool
```

功能：判断该全局函数信息与给定的另一个全局函数信息是否相等。

参数：

- that: [GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo) - 被比较相等性的另一个全局函数信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该全局函数信息与 `that` 相等则返回 `true`，否则返回 `false`。