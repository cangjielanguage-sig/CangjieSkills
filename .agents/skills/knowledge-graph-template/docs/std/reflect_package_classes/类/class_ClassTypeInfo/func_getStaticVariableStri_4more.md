### func getStaticVariable(String)

```cangjie
public func getStaticVariable(name: String): StaticVariableInfo
```

功能：给定变量名称，尝试获取该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 所对应的 `class` 类型中匹配的静态成员变量的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 变量名称。

返回值：

- [StaticVariableInfo](reflect_package_classes.md#class-staticvariableinfo) - 如果成功匹配则返回该静态成员变量的信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应静态成员变量，则抛出异常。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {
    public static var area: Int64 = 10
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("test.Rectangular")

    // 获取静态变量
    let sv = ty.getStaticVariable("area")
    println(sv)
    return
}
```

运行结果：

```text
static area: Int64
```

### func isAbstract()

```cangjie
public func isAbstract(): Bool
```

功能：判断该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 类型是否是抽象类。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 类型是抽象类则返回 `true`，否则返回 `false`。

### func isOpen()

```cangjie
public func isOpen(): Bool
```

功能：判断该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 类型是否拥有 `open` 语义。

> **注意：**
>
> 并不是只有被 `open` 修饰符所修饰的 `class` 类型定义才拥有 `open` 语义，如：`abstract class` 无论是否被 `open` 修饰符修饰都会拥有 `open` 语义。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 类型拥有 `open` 语义则返回 `true`，否则返回 `false`。

### func isSealed()

```cangjie
public func isSealed(): Bool
```

功能：判断该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 类型是否拥有 `sealed` 语义。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 类型拥有 `sealed` 语义则返回 `true`，否则返回 `false`。