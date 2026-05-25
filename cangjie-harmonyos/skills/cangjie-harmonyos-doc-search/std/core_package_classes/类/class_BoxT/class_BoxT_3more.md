## class Box\<T>

```cangjie
public class Box<T> {
    public var value: T
    public init(v: T)
}
```

功能：[Box](core_package_classes.md#class-boxt) 类型提供了为其他类型添加一层 `class` 封装的能力。

如果 `T` 类型本身不具备引用能力，如 `struct` 类型，封装后 [Box](core_package_classes.md#class-boxt)\<T> 类型将可被引用。

### var value

```cangjie
public var value: T
```

功能：获取或修改被包装的值。

类型：T

### init(T)

```cangjie
public init(v: T)
```

功能：给定 `T` 类型实例，构造对应的 [Box](core_package_classes.md#class-boxt)\<T> 实例。

参数：

- v: T - 任意类型实例。