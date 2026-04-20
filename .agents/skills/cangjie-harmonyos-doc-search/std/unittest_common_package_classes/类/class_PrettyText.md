## class PrettyText

```cangjie
public class PrettyText <: PrettyPrinter & PrettyPrintable & ToString {
    public init()
    public init(string: String)
}
```

功能：存储打印的输出。主要用途是中间存储和传递这些值。

实现了 [PrettyPrinter](#class-prettyprinter)（可以打印到）和 [PrettyPrintable](./unittest_common_package_interfaces.md#interface-prettyprintable)（可以从中打印）的方法。

父类型：

- [PrettyPrinter](#class-prettyprinter)
- [PrettyPrintable](unittest_common_package_interfaces.md#interface-prettyprintable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### init()

```cangjie
public init()
```

功能：默认构造器，生成一个空的对象。

### init(String)

```cangjie
public init(string: String)
```

功能：构造器，生成一个以入参开头的文本构造器。

参数：

- string: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 希望放入打印文本开头的字符串。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：返回当前构造器是否为空，即未有值传入给构造器。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 未有内容传入时返回 `true` ，否则返回 `false` 。

### func pprint(PrettyPrinter)

```cangjie
public func pprint(to: PrettyPrinter): PrettyPrinter
```

功能：打印信息到打印器上。

参数：

- to: [PrettyPrinter](#class-prettyprinter) - 打印器。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func toString()

```cangjie
public func toString(): String
```

功能：打印文本到字符串上。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 打印文本的字符串。

### static func of\<PP>(PP)

```cangjie
public static func of<PP>(pp: PP): PrettyText where PP <: PrettyPrintable
```

功能：通过打印从 [PrettyPrintable](./unittest_common_package_interfaces.md#interface-prettyprintable) 创建 [PrettyText](#class-prettytext)。

参数：

- pp: PP  - 一个实现了 [PrettyPrintable](./unittest_common_package_interfaces.md#interface-prettyprintable) 的类型。

返回值：

- [PrettyText](#class-prettytext) - 打印文本对象。