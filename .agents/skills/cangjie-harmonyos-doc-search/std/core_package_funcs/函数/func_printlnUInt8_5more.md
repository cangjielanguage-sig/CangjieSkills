## func println(UInt8)

```cangjie
public func println(i: UInt8): Unit
```

功能：向控制台输出 [UInt8](core_package_intrinsics.md#uint8) 类型数据的字符串表达，末尾添加换行。

参数：

- i: [UInt8](core_package_intrinsics.md#uint8) - 待输出的 [UInt8](core_package_intrinsics.md#uint8) 类型数据。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UInt8 = 8
    var num2: UInt8 = 32
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
8
32
```

## func println\<T>(T) where T <: ToString

```cangjie
public func println<T>(arg: T): Unit where T <: ToString
```

功能：向控制台输出 `T` 类型实例的字符串表示，末尾添加换行。

参数：

- arg: T - 待输出的数据，支持实现了 [ToString](core_package_interfaces.md#interface-tostring) 接口的类型。

示例：

<!-- verify -->
```cangjie
class Rectangle <: ToString {
    var width: Int64
    var height: Int64

    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
    }

    public func toString(): String {
        return "width: ${this.width}, height: ${this.height}"
    }
}

main() {
    println<Rectangle>(Rectangle(10, 20))
    println<Rectangle>(Rectangle(5, 10))
}
```

运行结果：

```text
width: 10, height: 20
width: 5, height: 10
```

## func readln()

```cangjie
public func readln(): String
```

功能：接受控制台输入，直到遇到换行或 EOF 结束。

返回值：

- [String](core_package_structs.md#struct-string) - 接受到的字符串。

示例：

<!-- compile -->
```cangjie
main() {
    var str: String = readln() // Console input 12345 234 and enter
    println(str)
}
```

运行结果：

```text
12345 234
```

## func refEq(Object, Object)

```cangjie
public func refEq(a: Object, b: Object): Bool
```

功能：判断两个 [Object](core_package_classes.md#class-object) 实例的内存地址是否相同。

参数：

- a: [Object](core_package_classes.md#class-object) - 一个 [Object](core_package_classes.md#class-object) 实例。
- b: [Object](core_package_classes.md#class-object) - 另一个 [Object](core_package_classes.md#class-object) 实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果两个 [Object](core_package_classes.md#class-object) 实例的内存地址相同，返回 true，否则返回 false。

示例：

<!-- verify -->
```cangjie
class Rectangle {
    var width: Int64
    var height: Int64

    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
    }
}

main() {
    var r1: Rectangle = Rectangle(10, 20)
    var r2: Rectangle = r1
    var r3: Rectangle = Rectangle(5, 6)
    println(refEq(r1, r2))
    println(refEq(r1, r3))
}
```

运行结果：

```text
true
false
```

## func releaseArrayRawData\<T>(CPointerHandle\<T>) where T <: CType

```cangjie
public unsafe func releaseArrayRawData<T>(handle: CPointerHandle<T>): Unit where T <: CType
```

功能：释放原始指针实例，该实例通过 [acquireArrayRawData](core_package_funcs.md#func-acquirearrayrawdatatarrayt-where-t--ctype) 获取。

参数：

- handle: [CPointerHandle](core_package_structs.md#struct-cpointerhandlet-where-t--ctype)\<T> - 待释放的指针实例。

示例：

<!-- verify -->
```cangjie
main() {
    var arr: Array<Int64> = [1, 2, 3, 4]
    var cptrHandle: CPointerHandle<Int64> = unsafe { acquireArrayRawData(arr) }

    var cptr: CPointer<Int64> = cptrHandle.pointer
    let num: Int64 = unsafe { cptr.read() }
    println("The first element of the array is ${num} ")

    unsafe { releaseArrayRawData<Int64>(cptrHandle) }
}
```

运行结果：

```text
The first element of the array is 1
```