# 动态特性

本章介绍 Cangjie 的动态特性，应用动态特性开发者能够更为优雅的实现一些功能。仓颉的动态特性主要包含反射。

## 仓颉反射基本介绍

反射指程序可以访问、检测和修改它本身状态或行为的一种机制。

反射这一动态特性有以下的优点：

- 提高了程序的灵活性和扩展性。

- 程序能够在运行时获悉各种对象的类型，对其成员进行枚举、调用等操作。

- 允许在运行时创建新类型，无需提前硬编码。

但使用反射调用，其性能通常低于直接调用，因此反射机制主要应用于对灵活性和拓展性要求很高的系统框架上。

## 如何获得 TypeInfo

对于仓颉的反射特性，需要知道 TypeInfo 这一类型，这个核心类型中记录任意类型的类型信息，并且定义了方法用于获取类型信息、设置值等。当然为了便于用户操作仓颉还提供了 ClassTypeInfo、PrimitiveTypeInfo、ParameterInfo 等一系列的信息类型。

可以使用三种静态的 `of` 方法来生成 TypeInfo 信息类。

```cangjie
public class TypeInfo {
    public static func of(a: Any): TypeInfo
    public static func of(a: Object): ClassTypeInfo
    public static func of<T>(): TypeInfo
}
```

当采用入参为 `Any` 和 `Object` 类型的 `of` 函数，输出为该实例的运行时类型信息，采用泛型参数的 `of` 函数则会返回传入参数的静态类型信息。两种方法产生的信息完全相同，但不保证一定对应同一对象。

例如可以用反射来获取一个自定义类型的类型信息。

```cangjie
import std.reflect.*

class Foo {}

main() {
    let a: Foo = Foo()
    let info: TypeInfo = TypeInfo.of(a)
    let info2: TypeInfo = TypeInfo.of<Foo>()
    println(info)
    println(info2)
}
```

编译并执行上面的代码，会输出：

```text
default.Foo
default.Foo
```

此外 TypeInfo 还提供了静态函数 `get`，该接口可通过传入的类型名称获取 TypeInfo。

```cangjie
public class TypeInfo {
    public static func get(qualifiedName: String): TypeInfo
}
```

请注意，传入参数需要符合 `module.package.type` 的完全限定模式规则。对于编译器预导入的类型，包含 core 包中的类型和编译器内置类型，例如 `primitive type`、`Option`、`Iterable` 等，查找的字符串需要直接使用其类型名，不能带包名和模块名前缀。当运行时无法查询到对应类型的实例，则会抛出 `InfoNotFoundException`。

```cangjie
let t1: TypeInfo = TypeInfo.get("Int64")
let t1: TypeInfo = TypeInfo.get("default.Foo")
let t2: TypeInfo = TypeInfo.get("std.socket.TcpSocket")
let t3: TypeInfo = TypeInfo.get("net.http.ServerBuilder")
```

采用这种方式时无法获取一个未实例化的泛型类型。

```cangjie
import std.collection.*
import std.reflect.*

class A<T> {
    A(public let t: T) {}
}

class B<T> {
    B(public let t: T) {}
}

main() {
    let aInfo: TypeInfo = TypeInfo.get("default.A<Int64>")// Error,`default.A<Int64>` is not instantiated，will throw InfoNotFoundException
    let b: B<Int64> = B<Int64>(1)
    let bInfo: TypeInfo = TypeInfo.get("default.B<Int64>")// OK `default.B<Int64>` has been instantiated.
}
```