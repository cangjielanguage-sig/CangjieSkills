### extend\<T> Box\<T> <: Comparable\<Box\<T>> where T <: Comparable\<T>

```cangjie
extend<T> Box<T> <: Comparable<Box<T>> where T <: Comparable<T>
```

功能：为 [Box](core_package_classes.md#class-boxt)\<T> 类扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[Box](core_package_classes.md#class-boxt)\<T>> 接口，提供比较大小的能力。

[Box](core_package_classes.md#class-boxt)\<T> 实例的大小关系与其封装的 `T` 实例大小关系相同。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[Box](#class-boxt)\<T>>

#### func compare(Box\<T>)

```cangjie
public func compare(that: Box<T>): Ordering
```

功能：判断当前 [Box](core_package_classes.md#class-boxt) 实例与另一个 [Box](core_package_classes.md#class-boxt) 实例的大小关系。

参数：

- that: [Box](core_package_classes.md#class-boxt)\<T> - 比较的另外一个 [Box](core_package_classes.md#class-boxt) 对象。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果当前 [Box](core_package_classes.md#class-boxt) 实例大于 that，返回 [Ordering](core_package_enums.md#enum-ordering).GT，等于返回 [Ordering](core_package_enums.md#enum-ordering).EQ，小于返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
struct Data <: Comparable<Data> {
    var a: Int64 = 0
    var b: Int64 = 0

    public init(a: Int64, b: Int64) {
        this.a = a
        this.b = b
    }

    public func compare(d: Data) {
        let tValue: Int64 = this.a + this.b
        let dValue: Int64 = d.a + d.b
        if (tValue > dValue) {
            return Ordering.GT
        } else if (tValue == dValue) {
            return Ordering.EQ
        } else {
            return Ordering.LT
        }
    }
}

main() {
    var data1: Box<Data> = Box<Data>(Data(12, 12))
    var data2: Box<Data> = Box<Data>(Data(7, 12))
    println(data1.compare(data2))
}
```

运行结果：

```text
Ordering.GT
```

#### operator func !=(Box\<T>)

```cangjie
public operator func !=(that: Box<T>): Bool
```

功能：比较 [Box](core_package_classes.md#class-boxt) 对象是否不相等。

参数：

- that: [Box](core_package_classes.md#class-boxt)\<T> - 比较的另外一个 [Box](core_package_classes.md#class-boxt) 对象。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 当前 [Box](core_package_classes.md#class-boxt) 对象不等于参数 [Box](core_package_classes.md#class-boxt) 对象返回 true，否则返回 false。

#### operator func <(Box\<T>)

```cangjie
public operator func <(that: Box<T>): Bool
```

功能：比较 [Box](core_package_classes.md#class-boxt) 对象的大小。

参数：

- that: [Box](core_package_classes.md#class-boxt)\<T> - 比较的另外一个 [Box](core_package_classes.md#class-boxt) 对象。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 当前 [Box](core_package_classes.md#class-boxt) 对象小于参数 [Box](core_package_classes.md#class-boxt) 对象返回 true，否则返回 false。

#### operator func <=(Box\<T>)

```cangjie
public operator func <=(that: Box<T>): Bool
```

功能：比较 [Box](core_package_classes.md#class-boxt) 对象的大小。

参数：

- that: [Box](core_package_classes.md#class-boxt)\<T> - 比较的另外一个 [Box](core_package_classes.md#class-boxt) 对象。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 当前 [Box](core_package_classes.md#class-boxt) 对象小于等于参数 [Box](core_package_classes.md#class-boxt) 对象返回 true，否则返回 false。