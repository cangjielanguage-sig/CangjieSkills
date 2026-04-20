## func parseDecl(Tokens, String)

```cangjie
public func parseDecl(input: Tokens, astKind!: String = ""): Decl
```

功能：用于解析一组词法单元，获取一个 [Decl](ast_package_classes.md#class-decl) 类型的节点。

> **注意：**
>
> 该函数不支持解析 [FuncParam](ast_package_classes.md#class-funcparam) 类型。

参数：

- input: [Tokens](ast_package_classes.md#class-tokens) - 待解析源码的词法单元。
- astKind!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于指定解析特定的节点类型，有效支持的值为：`PrimaryCtorDecl` 和 `PropMemberDecl`。
    - `PrimaryCtorDecl`: 解析主构造函数。
    - `PropMemberDecl`: 解析 prop 声明的 getter 和 setter 函数。

返回值：

- [Decl](ast_package_classes.md#class-decl) - 一个 [Decl](ast_package_classes.md#class-decl) 类型的节点。

异常：

- [ParseASTException](ast_package_exceptions.md#class-parseastexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [Decl](ast_package_classes.md#class-decl) 节点时，抛出异常，异常中包含报错提示信息。

示例：

1. 以下代码展示 `astKind` 设为 `PropMemberDecl` 的案例。在这个参数下，可以使用 `parseDecl` 解析 `prop` 的 getter 和 setter 函数，解析结果为 `FuncDecl` 类型（如果不设置`astKind`，则会因为没有 `func` 关键字而无法解析）。

<!-- verify -->

```cangjie
import std.ast.*

main() {
    let getter = quote( get() { _val } )
    let setter = quote( set(v) { _val = v })
    let getterDecl = parseDecl(getter, astKind: "PropMemberDecl")
    let setterDecl = parseDecl(setter, astKind: "PropMemberDecl")
    println((getterDecl as FuncDecl).getOrThrow().block.toTokens())
    println((setterDecl as FuncDecl).getOrThrow().block.toTokens())
}
```

运行结果：

```text
{
    _val
}

{
    _val = v
}
```

1. 以下代码展示 `astKind` 设为 `PrimaryCtorDecl` 的案例。在这个参数下，可以使用 `parseDecl` 解析主构造函数节点，解析结果为 `PrimaryCtorDecl` 类型（如果不设置 `astKind`，则会因为没有 `func` 关键字而无法解析）。

<!-- verify -->

```cangjie
import std.ast.*

main() {
    let ctor = quote(
        Point(var x: Int32, var y: Int32) {}
    )
    let ctorDecl = parseDecl(ctor, astKind: "PrimaryCtorDecl")
    println(ctorDecl is PrimaryCtorDecl)
    println(ctorDecl.toTokens())
}
```

运行结果：

```text
true
Point(var x: Int32, var y: Int32) {
}
```