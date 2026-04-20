## enum AnnotationKind

```cangjie
public enum AnnotationKind {
    | Type
    | Parameter
    | Init
    | MemberProperty
    | MemberFunction
    | MemberVariable
    | EnumConstructor
    | GlobalFunction
    | GlobalVariable
    | Extension
    | ...
}
```

功能：表示自定义注解希望支持的位置。

### EnumConstructor

```cangjie
EnumConstructor
```

功能：枚举构造器声明。

### Extension

```cangjie
Extension
```

功能：扩展声明。

### GlobalFunction

```cangjie
GlobalFunction
```

功能：全局函数声明。

### GlobalVariable

```cangjie
GlobalVariable
```

功能：全局变量声明。

### Init

```cangjie
Init
```

功能：构造函数声明。

### MemberFunction

```cangjie
MemberFunction
```

功能：成员函数声明。

### MemberProperty

```cangjie
MemberProperty
```

功能：成员属性声明。

### MemberVariable

```cangjie
MemberVariable
```

功能：成员变量声明。

### Parameter

```cangjie
Parameter
```

功能：成员函数/构造函数中的参数（不包括枚举构造器的参数）。

### Type

```cangjie
Type
```

功能：类型声明（class、struct、enum、interface）。

## enum Endian

```cangjie
public enum Endian {
    | Big
    | Little
}
```

功能：枚举类型 [Endian](core_package_enums.md#enum-endian) 表示运行平台的端序，分为大端序和小端序。

### Big

```cangjie
Big
```

功能：表示大端序。

### Little

```cangjie
Little
```

功能：表示小端序。

### static prop Platform

```cangjie
public static prop Platform: Endian
```

功能：获取所在运行平台的端序。

类型：[Endian](core_package_enums.md#enum-endian)

异常：

- [UnsupportedException](core_package_exceptions.md#class-unsupportedexception) - 当所运行平台返回的端序无法识别时，抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    let e = Endian.Platform
    match (e) {
        case Big => println("BigEndian")
        case Little => println("LittleEndian")
    }
}
```

运行结果：

```text
LittleEndian
```