## @Attribute

仓颉语言内部提供 `@Attribute` 标记，开发者通过内置的 `@Attribute` 来对某个声明设置属性值，从而达到标记声明的目的。属性值可以是 `identifier` 或者 `string`，下面是一个简单的例子，这段示例代码为变量 `cnt` 添加了一个 `identifier` 类型的属性 `State`，为变量 `bcnt` 添加了一个 `string` 类型的属性 `"Binding"`。

<!-- compile -->

```cangjie
@Attribute[State] var cnt = 0       // identifier
@Attribute["Binding"] var bcnt = 0  // string
```

同时，标准库 `std.ast` 包提供了 `getAttrs()` 方法用于获取节点的属性，以及 `hasAttr(attrs: String)` 方法用于判断当前节点是否具有某个属性，下面是一个具体的例子。

宏定义如下：

<!-- run -macro0 -->
<!-- cfg="--compile-macro" -->

```cangjie
public macro Component(input: Tokens): Tokens {
    var varDecl = parseDecl(input)
    if (varDecl.hasAttr("State")) { // 如果该节点被标记了属性且值为 “State” 返回 true, 否则返回 false
        var attrs = varDecl.getAttrs() // 返回一组 Tokens
        println(attrs[0].value)
    }
    return input
}
```

宏调用如下：

<!-- run -macro0 -->
<!-- cfg="--debug-macro" -->

```cangjie
@Component(
    @Attribute[State] var cnt = 0
)
```

## @Deprecated

`@Deprecated` 表示此 API 已废弃，虽然暂时可用，但未来将被移除或更改，建议其他开发者不要调用此 API。例如：

<!-- compile -->

```cangjie
@Deprecated["用boo代替", since: "1.3.4"]
func foo() {}

main() {
    foo()
}
```

编译器编译时将提供告警信息：

```text
warning: function 'foo' is deprecated since 1.3.4. 用boo代替
 ==> file.cj:5:5:
  |
5 |     foo()
  |     ^^^ deprecated
  |
  # note: this warning can be suppressed by setting the compiler option `-Woff deprecated`

1 warning generated, 1 warning printed.
```

@Deprecated 自定义宏可以应用于以下声明：

- 类、接口、结构体、枚举、枚举构造器
- 顶级（全局）函数或变量
- 静态或非静态的成员函数、成员变量、属性、属性设置器
- 运算符函数
- 扩展的成员函数、静态函数、属性或属性设置器
- foreign 函数或声明在 foreign 块内的函数
- 构造函数和主构造函数
- 抽象的函数和属性
- 类型别名（包括关联类型）
- 函数具有默认参数的命名参数
- const 变量和函数
- 宏定义
- 注解类

### @Deprecated 参数

- `message: String` - 描述声明为何废弃、如何迁移等。
- `since!: ?String` - 废弃版本。
- `strict!: Bool` - 默认值为 `false`，在被该标记修饰的 API 的调用处会触发警告。如果设置为 `true`，则会触发编译错误。

<!-- compile.error -->

```cangjie
@Deprecated["Use Macro2", since: "1990", strict: true]
public macro Macro(input: Tokens): Tokens {
    return input
}
```