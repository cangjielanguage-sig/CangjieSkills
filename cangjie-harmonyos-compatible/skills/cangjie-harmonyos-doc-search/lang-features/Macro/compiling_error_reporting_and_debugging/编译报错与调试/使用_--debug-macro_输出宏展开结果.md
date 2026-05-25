## 使用 --debug-macro 输出宏展开结果

借助宏在编译期做代码生成时，如果发生错误，处理起来十分棘手，这是开发者经常遇到但一般很难定位的问题。这是因为，开发者写的源码，经过宏的变换后变成了不同的代码片段。编译器抛出的错误信息是基于宏最终生成的代码进行提示的，但这些代码在开发者的源码中没有体现。

为了解决这个问题，仓颉宏提供 debug 模式，在这个模式下，开发者可以从编译器为宏生成的 debug 文件中看到完整的宏展开后的代码，如下所示。

宏定义文件：

<!-- compile -macro3 -->
<!-- cfg="--compile-macro" -->

```cangjie
macro package define

import std.ast.*

public macro Outer(input: Tokens): Tokens {
    let messages = getChildMessages("Inner")

    let getTotalFunc = quote(public func getCnt() {
                       )
    for (m in messages) {
        let identName = m.getString("identifierName")
        getTotalFunc.append(Token(TokenKind.IDENTIFIER, identName))
        getTotalFunc.append(quote(+))
    }
    getTotalFunc.append(quote(0))
    getTotalFunc.append(quote(}))
    let funcDecl = parseDecl(getTotalFunc)

    let decl = (parseDecl(input) as ClassDecl).getOrThrow()
    decl.body.decls.add(funcDecl)
    return decl.toTokens()

}

public macro Inner(input: Tokens): Tokens {
    assertParentContext("Outer")
    let decl = parseDecl(input)
    setItem("identifierName", decl.identifier.value)
    return input
}
```

宏调用文件 `demo.cj`：

<!-- compile -macro3 -->
<!-- cfg="--debug-macro" -->

```cangjie
import define.*

@Outer
class Demo {
    @Inner var state = 1
    @Inner var cnt = 42
}

main(): Int64 {
    let d = Demo()
    println("${d.getCnt()}")
    return 0
}

```

在编译使用宏的文件时，在选项中，增加 `--debug-macro`，即使用仓颉宏的 _debug_ 模式。

```shell
cjc --debug-macro demo.cj --import-path ./target
```

> **注意：**
>
> 如果使用仓颉的 `CJPM` 项目管理工具进行编译，可在配置文件 `cjpm.toml` 中添加 `--debug-macro` 的编译选项来使用宏的 _debug_ 模式。
>
> ```text
> compile-option = "--debug-macro"
> ```

在 _debug_ 模式下，会生成临时文件 _demo.cj.macrocall_，对应宏展开的部分如下：

<!-- code_no_check -->

```cangjie
// demo.cj.macrocall
/* ===== Emitted by MacroCall @Outer in demo.cj:3:1 ===== */
/* 3.1 */class Demo {
/* 3.2 */    var state = 1
/* 3.3 */    var cnt = 42
/* 3.4 */    public func getCnt() {
/* 3.5 */        state + cnt + 0
/* 3.6 */    }
/* 3.7 */}
/* 3.8 */
/* ===== End of the Emit ===== */
```

如果宏展开后的代码有语义错误，则编译器的错误信息会溯源到宏展开后代码的具体行列号。仓颉宏的 _debug_ 模式有以下注意事项：

- 宏的 _debug_ 模式会重排源码的行列号信息，不适用于某些特殊的换行场景。例如：

  <!-- code_no_check -->

  ```cangjie
  // before expansion
  @M{} - 2 // macro M return 2

  // after expansion
  // ===== Emmitted my Macro M at line 1 ===
  2
  // ===== End of the Emit =====
  - 2
  ```

  这些因换行符导致语义改变的情形，不应使用 _debug_ 模式。

- 不支持宏调用在宏定义内的调试，会编译报错。

  <!-- code_no_check -->

  ```cangjie
  public macro M(input: Tokens) {
      let a = @M2(1+2) // M2 is in macro M, not suitable for debug mode.
      return input + quote($a)
  }
  ```

- 不支持带括号宏的调试。

  <!-- code_no_check -->

  ```cangjie
  // main.cj

  main() {
      // For macro with parenthesis, newline introduced by debug will change the semantics
      // of the expression, so it is not suitable for debug mode.
      let t = @M(1+2)
  }
  ```