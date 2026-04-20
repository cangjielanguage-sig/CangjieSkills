### prop typeInfos

```cangjie
public prop typeInfos: Collection<TypeInfo>
```

功能：获取该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的包中所有全局定义的 `public` 类型的类型信息，返回对应集合。

> **注意：**
>
> 目前该列表不包含所有反射尚未支持的类型。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[TypeInfo](reflect_package_classes.md#class-typeinfo)>

### prop version

```cangjie
public prop version: String
```

功能：获取该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的包的版本号。

> **注意：**
>
> 由于目前动态库中尚无版本信息，获取到的版本号总是空字符串。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static func get(String)

```cangjie
public static func get(qualifiedName: String): PackageInfo
```

功能：获取给定 `qualifiedName` 所对应的 [PackageInfo](./reflect_package_classes.md#class-packageinfo)。

参数：

- qualifiedName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 类型的限定名称。

返回值：

- [PackageInfo](./reflect_package_classes.md#class-packageinfo) - 类型的限定名称 `qualifiedName` 所对应的包信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获取与给定类型的限定名称 `qualifiedName` 所对应的类型信息，则抛出异常。

### static func load(String)

```cangjie
public static func load(path: String): PackageInfo
```

功能：运行时动态加载指定路径下的一个仓颉动态库模块并获得该模块的信息。

> **注意：**
>
> - 为了提升兼容性，路径 `path` 中的共享库文件名不需要后缀名（如 `.so` 和 `.dll` 等）。
> - 如果某个 `package` 通过静态加载方式（如：`import`）已经导入过，那么动态加载该 `package` 会抛出异常。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 共享库文件的绝对路径或相对路径。

返回值：

- [PackageInfo](reflect_package_classes.md#class-packageinfo) - 指定仓颉动态库的包信息。

异常：

- [ReflectException](reflect_package_exceptions.md#class-reflectexception) - 如果共享库加载失败，则会抛出异常。
- [ReflectException](reflect_package_exceptions.md#class-reflectexception) - 如果具有相同包名称或相同文件名的共享库被重复加载，则会抛出异常。
- [ReflectException](reflect_package_exceptions.md#class-reflectexception) - 如果动态库内部存在多个 Package，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当路径不合法时，抛出异常。

### func getFunction(String, Array\<TypeInfo>)

```cangjie
public func getFunction(name: String, parameterTypes: Array<TypeInfo>): GlobalFunctionInfo
```

功能：尝试在该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的包中获取拥有给定函数名称且与给定形参类型信息列表匹配的 `public` 全局函数的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 全局函数的名称。
- parameterTypes: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[TypeInfo](reflect_package_classes.md#class-typeinfo)> - 形参类型信息列表。

返回值：

- [GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo) - 如果成功匹配则返回该全局定义的 `public` 类型的函数信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应全局定义的 `public` 全局函数，则抛出异常。