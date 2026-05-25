## 嵌套宏

仓颉语言不支持宏定义的嵌套；有条件地支持在宏定义和宏调用中嵌套宏调用。

### 宏定义中嵌套宏调用

下面是一个宏定义中包含其他宏调用的例子。

宏包 `pkg1` 中定义 `getIdent` 宏：

<!-- compile -macro8 -->
<!-- cfg="--compile-macro" -->

```cangjie
macro package pkg1

import std.ast.*

public macro getIdent(attr:Tokens, input:Tokens):Tokens {
    return quote(
        let decl = (parseDecl(input) as VarDecl).getOrThrow()
        let name = decl.identifier.value
        let size = name.size - 1
        let $(attr) = Token(TokenKind.IDENTIFIER, name[0..size])
    )
}
```

宏包 `pkg2` 中定义 `Prop` 宏，其中嵌套了 `getIdent` 宏的调用：

<!-- compile -macro8 -->
<!-- cfg="--compile-macro" -->

```cangjie
macro package pkg2

import std.ast.*
import pkg1.*

public macro Prop(input:Tokens):Tokens {
    let v = parseDecl(input)
    @getIdent[ident](input)
    return quote(
        $(input)
        public prop $(ident): $(decl.declType) {
            get() {
                this.$(v.identifier)
            }
        }
    )
}
```

宏调用包 `pkg3`  中调用 `Prop` 宏：

<!-- compile -macro8 -->

```cangjie
package pkg3

import pkg2.*
class A {
    @Prop
    private let a_: Int64 = 1
}

main() {
    let b = A()
    println("${b.a}")
}
```

注意，按照宏定义必须比宏调用点先编译的约束，上述 3 个文件的编译顺序必须是：pkg1 -> pkg2 -> pkg3。pkg2 中的 `Prop` 宏定义：

<!-- code_no_check -->

```cangjie
public macro Prop(input:Tokens):Tokens {
    let v = parseDecl(input)
    @getIdent[ident](input)
    return quote(
        $(input)
        public prop $(ident): $(decl.declType) {
            get() {
                this.$(v.identifier)
            }
        }
    )
}
```

会先被展开成如下代码，再进行编译。

<!-- code_no_check -->

```cangjie
public macro Prop(input: Tokens): Tokens {
    let v = parseDecl(input)

    let decl = (parseDecl(input) as VarDecl).getOrThrow()
    let name = decl.identifier.value
    let size = name.size - 1
    let ident = Token(TokenKind.IDENTIFIER, name[0 .. size])

    return quote(
        $(input)
        public prop $(ident): $(decl.declType) {
            get() {
                this.$(v.identifier)
            }
        }
    )
}
```

### 宏调用中嵌套宏调用

嵌套宏的常见场景，是宏修饰的代码块中，出现了宏调用。一个具体的例子如下：

`pkg1` 包中定义 `Foo` 和 `Bar` 宏：

<!-- run -macro9 -->
<!-- cfg="--compile-macro" -->

```cangjie
macro package pkg1

import std.ast.*

public macro Foo(input: Tokens): Tokens {
    return input
}

public macro Bar(input: Tokens): Tokens {
    return input
}
```

`pkg2` 包中定义 `addToMul` 宏：

<!-- run -macro9 -->
<!-- cfg="--compile-macro" -->

```cangjie
macro package pkg2

import std.ast.*

public macro addToMul(inputTokens: Tokens): Tokens {
    var expr: BinaryExpr = match (parseExpr(inputTokens) as BinaryExpr) {
        case Some(v) => v
        case None => throw Exception()
    }
    var op0: Expr = expr.leftExpr
    var op1: Expr = expr.rightExpr
    return quote(($(op0)) * ($(op1)))
}
```

`pkg3` 包中使用上面定义的三个宏：

<!-- run -macro9 -->

```cangjie
package pkg3

import pkg1.*
import pkg2.*
@Foo
struct Data {
    let a = 2
    let b = @addToMul(2+3)

    @Bar
    public func getA() {
        return a
    }

    public func getB() {
        return b
    }
}

main(): Int64 {
    let data = Data()
    var a = data.getA() // a = 2
    var b = data.getB() // b = 6
    println("a: ${a}, b: ${b}")
    return 0
}
```

如上代码所示，宏 `Foo` 修饰了 `struct Data`，而在 `struct Data` 内，出现了宏调用 `addToMul` 和 `Bar`。这种嵌套场景下，代码变换的规则是：将嵌套内层的宏（`addToMul` 和 `Bar`）展开后，再去展开外层的宏（`Foo`）。允许出现多层宏嵌套，代码变换的规则总是由内向外去依次展开宏。

嵌套宏可以出现在带括号和不带括号的宏调用中，二者可以组合，但开发者需要保证没有歧义，且明确宏的展开顺序：

<!-- code_no_check -->

```cangjie
var a = @foo(@foo1(2 * 3)+@foo2(1 + 3))  // foo1, foo2 have to be defined.

@Foo1 // Foo2 expands first, then Foo1 expands.
@Foo2[attr: struct] // Attribute macro can be used in nested macro.
struct Data{
    @Foo3 @Foo4[123] var a = @bar1(@bar2(2 + 3) + 3)  // bar2, bar1, Foo4, Foo3 expands in order.
    public func getA() {
        return @foo(a + 2)
    }
}
```