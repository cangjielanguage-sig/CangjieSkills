### func getFunctions(String)

```cangjie
public func getFunctions(name: String): Array<GlobalFunctionInfo>
```

功能：尝试在该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的包中获取拥有给定函数名称的所有 `public` 全局函数的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 全局函数的名称。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo)> - 拥有给定函数名称的所有 `public` 全局函数的信息数组。

### func getSubPackage(String)

```cangjie
public func getSubPackage(qualifiedName: String): PackageInfo
```

功能：尝试获取该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应限定名称为 `qualifiedName` 的子包的信息。

参数：

- qualifiedName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 子包的限定名称。

返回值：

- [PackageInfo](reflect_package_classes.md#class-packageinfo) - 该子包的包信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果该子包不存在或者未加载，则会抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `qualifiedName` 不符合规范，则抛出异常。

### func getTypeInfo(String)

```cangjie
public func getTypeInfo(qualifiedTypeName: String): TypeInfo
```

功能：尝试在该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的包中获取拥有给定类型名称的全局定义的 `public` 类型的类型信息。

参数：

- qualifiedTypeName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 类型的限定名称

返回值：

- [TypeInfo](reflect_package_classes.md#class-typeinfo) - 如果成功匹配则返回该全局定义的 `public` 类型的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应全局定义的 `public` 类型，则抛出异常。

### func getVariable(String)

```cangjie
public func getVariable(name: String): GlobalVariableInfo
```

功能：尝试在该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的包中获取拥有给定变量名称的 `public` 全局变量的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 全局变量的名称。

返回值：

- [GlobalVariableInfo](reflect_package_classes.md#class-globalvariableinfo) - 如果成功匹配则返回该全局定义的 `public` 类型的变量信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应全局定义的 `public` 全局变量，则抛出异常。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取该包信息的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 该包信息的哈希值。

### func toString()

```cangjie
public func toString(): String
```

功能：获取字符串形式的该包信息。

> **注意：**
>
> 内部实现为该包信息的限定名称字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的该包信息。