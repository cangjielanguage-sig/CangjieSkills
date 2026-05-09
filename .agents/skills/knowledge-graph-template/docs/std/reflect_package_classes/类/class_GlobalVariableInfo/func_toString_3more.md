### func toString()

```cangjie
public func toString(): String
```

功能：获取字符串形式的该全局变量信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的该全局变量信息。

### operator func !=(GlobalVariableInfo)

```cangjie
public operator func !=(that: GlobalVariableInfo): Bool
```

功能：判断该全局变量信息与给定的另一个全局变量信息是否不等。

参数：

- that: [GlobalVariableInfo](reflect_package_classes.md#class-globalvariableinfo) - 被比较相等性的另一个全局变量信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该全局变量信息与 `that` 不等则返回 `true`，否则返回 `false`。

### operator func ==(GlobalVariableInfo)

```cangjie
public operator func ==(that: GlobalVariableInfo): Bool
```

功能：判断该全局变量信息与给定的另一个全局变量信息是否相等。

参数：

- that: [GlobalVariableInfo](reflect_package_classes.md#class-globalvariableinfo) - 被比较相等性的另一个全局变量信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该全局变量信息与 `that` 相等则返回 `true`，否则返回 `false`。