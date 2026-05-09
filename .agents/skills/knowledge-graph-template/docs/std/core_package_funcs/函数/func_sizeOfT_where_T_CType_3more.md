## func sizeOf\<T>() where T <: CType

```cangjie
public func sizeOf<T>(): UIntNative where T <: CType
```

功能：获取类型 T 所占用的内存空间大小。

返回值：

- [UIntNative](core_package_intrinsics.md#uintnative) - 类型 T 所占用内存空间的字节数。

示例：

<!-- verify -->
```cangjie
@C
struct Data {
    var a: Int64 = 0
    var b: Float32 = 0.0
}

main() {
    let sizeInt8: UIntNative = sizeOf<Int8>()
    println("The size of Int8 is ${sizeInt8} byte")

    let sizeInt32: UIntNative = sizeOf<Int32>()
    println("The size of Int32 is ${sizeInt32} bytes")

    let sizeInt64: UIntNative = sizeOf<Int64>()
    println("The size of Int64 is ${sizeInt64} bytes")

    let sizeData: UIntNative = sizeOf<Data>()
    println("The size of Rectangle is ${sizeData} bytes")
}
```

运行结果：

```text
The size of Int8 is 1 byte
The size of Int32 is 4 bytes
The size of Int64 is 8 bytes
The size of Rectangle is 16 bytes
```

## func sleep(Duration)

```cangjie
public func sleep(dur: Duration): Unit
```

功能：休眠当前线程。

若 `dur` 小于等于 [Duration.Zero](core_package_structs.md#static-const-zero)，当前线程会让出运行权。

参数：

- dur: [Duration](core_package_structs.md#struct-duration) - 线程休眠的时长。

示例：

<!-- verify -->
```cangjie
import std.sync.*
import std.time.*

main(): Int64 {
    spawn {
        =>
        println("New thread starts")
        println("New thread ends")
    }

    println("Main thread")
    println("The main thread starts to sleep.")

    /* dur == 1 秒 */
    sleep(1000 * Duration.millisecond)
    println("The main thread ends sleep.")

    return 0
}
```

在启动主线程后，执行到 sleep 函数的时候，主线程会让出系统执行权，并睡眠 1 秒后重新唤醒竞争系统执行权，继续执行剩余逻辑。在主线程睡眠期间，自定义线程拿到执行权，开始执行。运行结果：

```text
Main thread
The main thread starts to sleep.
New thread starts
New thread ends
The main thread ends sleep.
```

## func zeroValue\<T>()

```cangjie
public unsafe func zeroValue<T>(): T
```

功能：获取一个已全零初始化的 T 类型实例。

> **注意：**
>
> 通过该函数获取到的实例一定要赋值为正常初始化的值再使用，否则将引发程序崩溃。

返回值：

- T - 一个已全零初始化的 T 类型实例。

示例：

<!-- verify -->

```cangjie
main(): Int64 {
    var m = MyClass<Student>()
    m.set(1, Student())
    var s = m.get(1)
    println(s)
    s = m.get(2)
    // 底下代码解除注释，运行时就会出错，因为其并不是 Student 对象
    // println(s)
    return 0
}

class MyClass<T> {
    var myData: Array<T>
    public init() {
        // 用 zeroValue<T>() 对 Array 进行全零初始化
        myData = Array<T>(10, repeat: unsafe { zeroValue<T>() })
    }
    public func get(index: Int64): T {
        myData[index]
    }
    public func set(index: Int64, element: T): Unit {
        myData[index] = element
    }
}

class Student <: ToString {
    public func toString() {
        "student"
    }
}
```

示例结果：

```text
student
```