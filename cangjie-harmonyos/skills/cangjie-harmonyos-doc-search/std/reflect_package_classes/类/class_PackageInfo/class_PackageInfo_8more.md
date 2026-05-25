## class PackageInfo

```cangjie
public class PackageInfo <: Equatable<PackageInfo> & Hashable & ToString {}
```

功能：描述包信息。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[PackageInfo](#class-packageinfo)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop variables

```cangjie
public prop variables: Collection<GlobalVariableInfo>
```

功能：获取该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的包中所有 `public` 全局变量的信息所组成的列表。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[GlobalVariableInfo](reflect_package_classes.md#class-globalvariableinfo)>

### prop functions

```cangjie
public prop functions: Collection<GlobalFunctionInfo>
```

功能：获取该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的包中所有 `public` 全局函数的信息所组成的列表。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo)>

### prop name

```cangjie
public prop name: String
```

功能：获取该包信息所对应的包的名称。

> **注意：**
>
> 包的名称不包含其所在的模块名称和其父包的名称，例如限定名称为 `a/b.c.d` 的包的名称是 `d` 。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop parentPackage

```cangjie
public prop parentPackage: PackageInfo
```

功能：获取该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的父包的 [PackageInfo](reflect_package_classes.md#class-packageinfo)。

类型：[PackageInfo](reflect_package_classes.md#class-packageinfo)

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果父包未被加载，则会抛出异常。

### prop qualifiedName

```cangjie
public prop qualifiedName: String
```

功能：获取该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的包的限定名称。

> **注意：**
>
> 包的限定名称的格式是 `(module_name/)?(default|package_name)(.package_name)*`，例如限定名称为 `a/b.c.d` 的包位于模块 `a` 下的 `b` 包里的 `c` 包里。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop rootPackage

```cangjie
public prop rootPackage: PackageInfo
```

功能：获取该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的 `root` 包的 [PackageInfo](reflect_package_classes.md#class-packageinfo)。

> **注意：**
>
> 如果包本身就是 `root` 包，那么其 `rootPackage` 属性返回的是其本身。例如，限定名称为 `a.b.c` 的包，`rootPackage` 返回的是 `a`; 限定名称为 `a` 的包，`rootpackage` 返回的是 `a`。

类型：[PackageInfo](reflect_package_classes.md#class-packageinfo)

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果 `root` 包未被加载，则会抛出异常。

### prop subPackages

```cangjie
public prop subPackages: Collection<PackageInfo>
```

功能：获取该 [PackageInfo](reflect_package_classes.md#class-packageinfo) 对应的所有子包的 [PackageInfo](reflect_package_classes.md#class-packageinfo) 集合。

> **注意：**
>
> - 该属性只会返回已被加载的子包。
> - 不保证返回结果的顺序。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[PackageInfo](reflect_package_classes.md#class-packageinfo)>