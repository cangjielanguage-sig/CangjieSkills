### prop modifiers

```cangjie
public prop modifiers: Collection<ModifierInfo>
```

功能：获取该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应的类型拥有的所有修饰符的信息，返回对应集合。

> **注意：**
>
> - 如果该类型无任何修饰符，则返回空集合。
> - 该集合不保证遍历顺序恒定。
> - `interface` 类型默认拥有 `open` 语义，故返回的集合总是包含 `open` 修饰符。
> - 由于反射功能只能对所有被 `public` 访问控制修饰符所修饰的类型进行操作，故将忽略所有访问控制修饰符。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[ModifierInfo](reflect_package_enums.md#enum-modifierinfo)>

### prop name

```cangjie
public prop name: String
```

功能：获取该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应的类型的名称。

> **注意：**
>
> - 该名称不包含任何模块名和包名前缀。
> - 类型别名的类型信息就是实际类型其本身的类型信息，所以该函数并不会返回类型别名本身的名称而是实际类型的名称，如类型别名 [Byte](../../core/core_package_api/core_package_types.md#type-byte) 的类型信息的名称是 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 而不是 [Byte](../../core/core_package_api/core_package_types.md#type-byte)。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop qualifiedName

```cangjie
public prop qualifiedName: String
```

功能：获取该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应的类型的限定名称。

> **注意：**
>
> - 限定名称包含模块名和包名前缀。
> - 特别的，仓颉内置数据类型，以及位于 `std` 模块 `core` 包下的所有类型的限定名称都是不带有任何模块名和包名前缀的。
> - 在缺省模块名和包名的上下文中定义的所有类型，均无模块名前缀，但拥有包名前缀"`default`"，如："`default.MyType`"。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop staticFunctions

```cangjie
public prop staticFunctions: Collection<StaticFunctionInfo>
```

功能：获取该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应类型的所有 `public` 静态成员函数信息，返回对应集合。

> **注意：**
>
> - 如果该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应的类型无任何 `public` 静态成员函数，则返回空集合。
> - 该集合不保证遍历顺序恒定。
> - 如果该类型信息所对应的类型是 `struct` 、`class` 或 `interface` 类型，则该集合不包含继承而来的静态成员函数的信息。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[StaticFunctionInfo](reflect_package_classes.md#class-staticfunctioninfo)>

### prop staticProperties

```cangjie
public prop staticProperties: Collection<StaticPropertyInfo>
```

功能：获取该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应类型的所有 `public` 静态成员属性信息，返回对应集合。

> **注意：**
>
> - 如果该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应的类型无任何 `public` 静态成员属性，则返回空集合。
> - 该集合不保证遍历顺序恒定。
> - 如果该类型信息所对应的类型是 `struct` 、`class` 或 `interface` 类型，则该集合不包含继承而来的静态成员属性的信息。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[StaticPropertyInfo](reflect_package_classes.md#class-staticpropertyinfo)>