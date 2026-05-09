## class 的继承

像大多数支持 `class` 的编程语言一样，仓颉中的 `class` 同样支持继承。如果类 B 继承类 A，则称 A 为父类，B 为子类。子类将继承父类中除 `private` 成员和构造函数以外的所有成员。

抽象类总是可被继承的，故抽象类定义时的 `open` 修饰符是可选的，也可以使用 `sealed` 修饰符修饰抽象类，表示该抽象类只能在本包被继承。但非抽象的类可被继承是有条件的：定义时必须使用修饰符 `open` 修饰。当带 `open` 修饰的实例成员被 class 继承时，该 `open` 的修饰符也会被继承。当非 `open` 修饰的类中存在 `open` 修饰的成员时，编译器会给出告警。

可以在子类定义处通过 `<:` 指定其继承的父类，但要求父类必须是可继承的。例如，下面的例子中，`class` A 使用 `open` 修饰，是可以被类 B 继承的，但是因为类 B 是不可继承的，所以 C 在继承 B 的时候会报错。

<!-- compile.error -->

```cangjie
open class A {
    let a: Int64 = 10
}

class B <: A { // OK: 'B' Inheritance 'A'
    let b: Int64 = 20
}

class C <: B { // Error, 'B' is not inheritable
    let c: Int64 = 30
}
```

`class` 仅支持单继承，因此下面这样一个类继承两个类的代码是不合法的（`&` 是类实现多个接口时的语法，详见[接口](interface.md)）。

<!-- compile.error -->

```cangjie
open class A {
    let a: Int64 = 10
}

open class B {
    let b: Int64 = 20
}

class C <: A & B { // Error, 'C' can only inherit one class
    let c: Int64 = 30
}
```

因为类是单继承的，所以任何类都最多只能有一个直接父类。对于定义时指定了父类的 `class`，它的直接父类就是定义时指定的类，对于定义时未指定父类的 `class`，它的直接父类是 `Object` 类型。`Object` 是所有类的父类（注意，`Object` 没有直接父类，并且 `Object` 中不包含任何成员）。

因为子类是继承自父类的，所以子类的对象天然可以当做父类的对象使用，但是反之不然。例如，下例中 B 是 A 的子类，那么 B 类型的对象可以赋值给 A 类型的变量，但是 A 类型的对象不能赋值给 B 类型的变量。

<!-- compile -->

```cangjie
open class A {
    let a: Int64 = 10
}

class B <: A {
    let b: Int64 = 20
}

let a: A = B() // OK: subclass objects can be assigned to superclass variables
```

<!-- compile.error -->

```cangjie
open class A {
    let a: Int64 = 10
}

class B <: A {
    let b: Int64 = 20
}

let b: B = A() // Error, superclass objects can not be assigned to subclass variables
```

`class` 定义的类型不允许继承类型本身。

<!-- compile.error -->

```cangjie
class A <: A {}  // Error, 'A' inherits itself
```

抽象类可以使用 `sealed` 修饰符，表示被修饰的类定义只能在本定义所在的包内被其他类继承。`sealed` 已经蕴含了 `public`/`open` 的语义，因此定义 sealed abstract class 时若提供 `public`/`open` 修饰符，编译器将会告警。`sealed` 的子类可以不是 `sealed` 类，仍可被 `open`/`sealed` 修饰，或不使用任何继承性修饰符。若 `sealed` 类的子类被 `open` 修饰，则其子类可在包外被继承。`sealed` 的子类可以不被 `public` 修饰。

<!-- compile -->

```cangjie
package A

public sealed abstract class C1 {}   // Warning, redundant modifier, 'sealed' implies 'public'
sealed open abstract class C2 {}     // Warning, redundant modifier, 'sealed' implies 'open'
sealed abstract class C3 {}          // OK, 'public' is optional when 'sealed' is used

class S1 <: C1 {}  // OK
public open class S2 <: C1 {}   // OK
public sealed abstract class S3 <: C1 {}  // OK
open class S4 <: C1 {}   // OK
```

<!-- compile.error -->

```cangjie
package B
import A.*

class SS1 <: S2 {}  // OK
class SS2 <: S3 {}  // Error, S3 is sealed class, cannot be inherited here
sealed class SS3 {} // Error, 'sealed' cannot be used on non-abstract class
```