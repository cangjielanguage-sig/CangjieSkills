## 使用 `import` 语句导入其他包中的声明或定义

在仓颉编程语言中，可以通过 `import fullPackageName.itemName` 的语法导入其他包中的一个顶层声明或定义，`fullPackageName` 为完整路径包名，`itemName` 为声明的名字。导入语句在源文件中的位置必须在包声明之后，其他声明或定义之前。例如：

```cangjie
package a
import std.math.*
import package1.foo
import {package1.foo, package2.bar}
```

如果要导入的多个 `itemName` 同属于一个 `fullPackageName`，可以使用 `import fullPackageName.{itemName[, itemName]*}` 语法，例如：

```cangjie
import package1.{foo, bar, fuzz}
```

这等价于：

```cangjie
import package1.foo
import package1.bar
import package1.fuzz
```

除了通过 `import fullPackagename.itemName` 语法导入一个特定的顶层声明或定义外，还可以使用 `import packageName.*` 语法将 `packageName` 包中所有可见的顶层声明或定义全部导入。例如：

```cangjie
import package1.*
import {package1.*, package2.*}
```

需要注意：

- 导入的成员的作用域级别低于当前包声明的成员。
- 当已导出的包的模块名或者包名被篡改，使其与导出时指定的模块名或包名不一致，在导入时会报错。
- 只允许导入当前文件可见的顶层声明或定义，导入不可见的声明或定义将会在导入处报错。
- 禁止通过 `import` 导入当前源文件所在包的声明或定义。
- 禁止包间的循环依赖导入，如果包之间存在循环依赖，编译器会报错。

示例如下：

```cangjie
// pkga/a.cj
package pkga    // Error, packages pkga pkgb are in circular dependencies.
import pkgb.*

class C {}
public struct R {}

// pkgb/b.cj
package pkgb

import pkga.*

// pkgc/c1.cj
package pkgc

import pkga.C // Error, 'C' is not accessible in package 'pkga'.
import pkga.R // OK, R is an external top-level declaration of package pkga.
import pkgc.f1 // Error, package 'pkgc' should not import itself.

public func f1() {}

// pkgc/c2.cj
package pkgc

func f2() {
    /* OK, the imported declaration is visible to all source files of the same package
     * and accessing import declaration by its name is supported.
     */
    R()

    // OK, accessing imported declaration by fully qualified name is supported.
    pkga.R()

    // OK, the declaration of current package can be accessed directly.
    f1()

    // OK, accessing declaration of current package by fully qualified name is supported.
    pkgc.f1()
}
```

在仓颉编程语言中，导入的声明或定义如果和当前包中的顶层声明或定义重名且不构成函数重载，则导入的声明和定义会被遮盖；导入的声明或定义如果和当前包中的顶层声明或定义重名且构成函数重载，函数调用时将会根据函数重载的规则进行函数决议。

```cangjie
// pkga/a.cj
package pkga

public struct R {}            // R1
public func f(a: Int32) {}    // f1
public func f(a: Bool) {} // f2

// pkgb/b.cj
package pkgb
import pkga.*

func f(a: Int32) {}         // f3
struct R {}                 // R2

func bar() {
    R()     // OK, R2 shadows R1.
    f(1)    // OK, invoke f3 in current package.
    f(true) // OK, invoke f2 in the imported package
}
```