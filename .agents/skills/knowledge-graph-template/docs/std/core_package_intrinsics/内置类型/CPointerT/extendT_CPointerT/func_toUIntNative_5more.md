#### func toUIntNative()

```cangjie
public func toUIntNative(): UIntNative
```

功能：获取该指针的整型形式。

返回值：

- [UIntNative](core_package_intrinsics.md#uintnative) - 该指针的整型形式。

示例：

<!-- run -->
```cangjie
foreign func malloc(size: UIntNative): CPointer<Unit>

foreign func free(ptr: CPointer<Unit>): Unit

main() {
    let sizeofInt64: UIntNative = 8
    var p = unsafe { malloc(sizeofInt64) }
    var p1 = unsafe { CPointer<Int64>(p) }
    unsafe { p1.write(8) }
    println(p1.toUIntNative())
    unsafe { free(p) }
}
```

运行结果：

```text
93954490863648
```

#### func write(Int64, T)

```cangjie
public unsafe func write(idx: Int64, value: T): Unit
```

功能：在指定下标位置写入一个数据，该接口需要用户保证指针的合法性，否则发生未定义行为。

参数：

- idx: [Int64](core_package_intrinsics.md#int64) - 指定的下标位置。
- value: T - 写入的数据。

示例：

<!-- verify -->
```cangjie
main() {
    var arr: Array<Int64> = [1, 2, 3, 4]
    var cptrHandle: CPointerHandle<Int64> = unsafe { acquireArrayRawData(arr) }

    var cptr: CPointer<Int64> = cptrHandle.pointer

    unsafe { cptr.write(2, 6) }

    println("The third element of the array is ${arr[2]} ")
    // The first element of the array is 1
    unsafe { releaseArrayRawData<Int64>(cptrHandle) }
}
```

运行结果：

```text
The third element of the array is 6
```

#### func write(T)

```cangjie
public unsafe func write(value: T): Unit
```

功能：写入一个数据，该数据总是在第一个，该接口需要用户保证指针的合法性，否则发生未定义行为。

参数：

- value: T - 要写入的数据。

示例：

<!-- verify -->
```cangjie
foreign func malloc(size: UIntNative): CPointer<Unit>

foreign func free(ptr: CPointer<Unit>): Unit

main() {
    let sizeofInt64: UIntNative = 8
    var p = unsafe { malloc(sizeofInt64) }
    var p1 = unsafe { CPointer<Int64>(p) }
    unsafe { p1.write(8) }
    let value: Int64 = unsafe { p1.read() }
    println(value)
    unsafe { free(p) }
}
```

运行结果：

```text
8
```

#### operator func +(Int64)

```cangjie
public unsafe operator func +(offset: Int64): CPointer<T>
```

功能：[CPointer](core_package_intrinsics.md#cpointert) 对象指针后移，同 C 语言的指针加法操作。

参数：

- offset: [Int64](core_package_intrinsics.md#int64) - 偏移量。

返回值：

- [CPointer](core_package_intrinsics.md#cpointert)\<T> - 返回偏移后的指针。

示例：

<!-- verify -->
```cangjie
main() {
    var arr: Array<Int64> = [1, 2, 3, 4]
    var cptrHandle: CPointerHandle<Int64> = unsafe { acquireArrayRawData(arr) }
    var cptr: CPointer<Int64> = cptrHandle.pointer

    let num1: Int64 = unsafe { cptr.read() }
    println(num1)
    cptr = unsafe { cptr + 1 }
    let num2: Int64 = unsafe { cptr.read() }
    println(num2)
    unsafe { releaseArrayRawData<Int64>(cptrHandle) }
}
```

运行结果：

```text
1
2
```

#### operator func -(Int64)

```cangjie
public unsafe operator func -(offset: Int64): CPointer<T>
```

功能：[CPointer](core_package_intrinsics.md#cpointert) 对象指针前移，同 C 语言的指针减法操作。

参数：

- offset: [Int64](core_package_intrinsics.md#int64) - 偏移量。

返回值：

- [CPointer](core_package_intrinsics.md#cpointert)\<T> - 返回偏移后的指针。

示例：

<!-- verify -->
```cangjie
main() {
    var arr: Array<Int64> = [1, 2, 3, 4]
    var cptrHandle: CPointerHandle<Int64> = unsafe { acquireArrayRawData(arr) }
    var cptr: CPointer<Int64> = cptrHandle.pointer

    let num1: Int64 = unsafe { cptr.read() }
    println(num1)
    cptr = unsafe { cptr + 1 }
    let num2: Int64 = unsafe { cptr.read() }
    println(num2)
    cptr = unsafe { cptr - 1 }
    let num3: Int64 = unsafe { cptr.read() }
    println(num3)
    unsafe { releaseArrayRawData<Int64>(cptrHandle) }
}
```

运行结果：

```text
1
2
1
```