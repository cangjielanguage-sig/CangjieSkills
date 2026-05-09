## 泛型

实现泛型类型的接口通常需要应用约束，以便类型仅在某些条件下实现接口。例如：

<!-- compile -->
```cangjie
class Cell<T> {
    Cell(let value: T) {}
}
main(){}
```

此时可能希望仅当单元格的值可打印时才能够打印该单元格。为了实现它，编写一个带有约束的扩展：

<!-- compile -->
```cangjie
class Cell<T> {
    Cell(let value: T) {}
}

extend<T> Cell<T> <: ToString where T <: ToString {
    public func toString(): String {
        "Cell(value = ${value})"
    }
}
main(){}
```

当使用 Deriving 时，它会默认尝试对所有泛型参数应用约束，因此以下内容与上面的扩展相同：

<!-- compile -->
```cangjie
import std.deriving.*

@Derive[ToString]
class Cell<T> {
    Cell(let value: T) {}
}
main(){}
```

然而在某些情况下，默认行为并不符合期望。此时，可使用 `@Derive` 内部的 `where` 来覆盖默认约束：

<!-- compile -->
```cangjie
import std.deriving.*

interface PrintableCellValue <: ToString { /*...*/ }

@Derive[ToString where T <: PrintableCellValue]
class Cell<T> {}
main(){}
```

请注意，在上面的示例中，自定义约束仅适用于 `ToString` ，因此如果需要对所有接口进行约束，则应单独为每个接口重复此动作。

<!-- compile -->
```cangjie
import std.deriving.*

interface PrintableCellValue <: ToString { /*...*/ }

@Derive[ToString where T <: PrintableCellValue]
@Derive[Hashable where T <: PrintableCellValue & Hashable]
class Cell<T> {}
main(){}
```

## 性能说明

由于 Deriving 是基于仓颉宏的，不涉及任何反射，因此 Deriving 实现的运行时性能与手写相当。但是，Deriving 涉及编译时的代码转换，因此它会影响编译时间。