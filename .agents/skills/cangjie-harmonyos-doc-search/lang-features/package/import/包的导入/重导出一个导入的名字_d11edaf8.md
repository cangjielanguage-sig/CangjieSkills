## 重导出一个导入的名字

在功能繁多的大型项目的开发过程中，这样的场景是非常常见的：包 `p2` 大量地使用从包 `p1` 中导入的声明，当包 `p3` 导入包 `p2` 并使用其中的功能时，`p1` 中的声明同样需要对包 `p3` 可见。如果要求包 `p3` 自行导入 `p2` 中使用到的 `p1` 中的声明，这个过程将过于繁琐。因此希望能够在 `p2` 被导入时一并导入 `p2` 使用到的 `p1` 中的声明。

在仓颉编程语言中，`import` 可以被 `private`、`internal`、`protected`、`public` 访问修饰符修饰。其中，被 `public`、`protected` 或者 `internal` 修饰的 `import` 可以把导入的成员重导出（如果这些导入的成员没有因为名称冲突或者被遮盖导致在本包中不可用）。其他包可以根据可见性直接导入并使用本包中用重导出的内容，无需从原包中导入这些内容。

- `private import` 表示导入的内容仅当前文件内可访问，`private` 是 `import` 的默认修饰符，不写访问修饰符的 `import` 等价于 `private import`。
- `internal import` 表示导入的内容在当前包及其子包（包括子包的子包）均可访问。非当前包访问需要显式 `import`。
- `protected import` 表示导入的内容在当前 module 内都可访问。非当前包访问需要显式 `import`。
- `public import` 表示导入的内容外部都可访问。非当前包访问需要显式 `import`。

在下面的例子中，`b` 是 `a` 的子包，在 `a` 中通过 `public import` 重导出了 `b` 中定义的函数 `f`。

```cangjie
package a
public import a.b.f

public let x = 0
```

```cangjie
internal package a.b

public func f() { 0 }
```

```cangjie
import a.f  // OK
let _ = f() // OK
```

需要注意的是，包不可以被重导出：如果被 `import` 导入的是包，那么该 `import` 不允许被 `public`、`protected` 或者 `internal` 修饰。

<!-- compile.error -->

```cangjie
public import a.b // Error, cannot re-export package
```