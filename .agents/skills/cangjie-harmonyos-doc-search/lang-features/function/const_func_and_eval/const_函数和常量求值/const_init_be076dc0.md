## `const init`

如果一个 `struct` 或 `class` 定义了 `const` 构造器，那么这个 `struct`/`class` 实例可以用在 `const` 表达式中。

1. 如果当前类型是 `class`，则不能具有 `var` 声明的实例成员变量，否则不允许定义 `const init` 。如果当前类型具有父类，当前的 `const init` 必须调用父类的 `const init`（可以显式调用或者隐式调用无参`const init`），如果父类没有 `const init` 则报错。

    <!-- compile.error -->

    ```cangjie
    public class Foo {
        val a: Int64 = 9 // Error, expected declaration, found 'val'
        let b: String
        const init(b: String) {
            this.b = b
        }
    }
    ```

    <!-- compile.error -->

    ```cangjie
    open public class Boo {
        let boo: String
        const init(b: String) {
            this.boo = b
        }
    }

    public class Foo <: Boo {
        let c: String
        const init(c: String) { //Error, there is no non-parameter constructor in super class, please invoke super call explicitly
            this.c = c
        }
    }
    ```

2. 当前类型的实例成员变量如果有初始值，初始值必须要是 `const` 表达式，否则不允许定义 `const init`。

    <!-- compile.error -->

    ```cangjie
    var a = "4123"

    class Foo {
        let foo: String = a // Error, expected 'const' expression guaranteed to be evaluated at compile time
        const init() {}
    }
    ```

3. `const init` 内可以使用赋值表达式 `=` 对实例成员变量赋值，除此以外不能有其他赋值表达式（如 `+=`, `-=`）。

    <!-- compile.error -->

    ```cangjie
    var a = "4123"

    class Foo {
        let foo: String
        let boo: Int64
        const init() {
            foo = "aa" // OK
            boo += 10 // Error, variable 'boo' is used before initialization
        }
    }
    ```

`const init` 与 `const` 函数的区别是 `const init` 内允许对实例成员变量进行赋值（需要使用赋值表达式）。