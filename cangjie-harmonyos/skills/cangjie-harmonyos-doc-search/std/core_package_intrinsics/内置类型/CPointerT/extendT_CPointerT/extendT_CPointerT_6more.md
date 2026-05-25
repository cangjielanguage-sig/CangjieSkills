### extend\<T> CPointer\<T>

```cangjie
extend<T> CPointer<T>
```

功能：为 [CPointer](core_package_intrinsics.md#cpointert)\<T> 扩展一些必要的指针使用相关接口，包含判空、读写数据等接口。

其中泛型 `T` 为指针类型，其满足 [CType](core_package_interfaces.md#interface-ctype) 约束。对 [CPointer](core_package_intrinsics.md#cpointert) 做运算需要在 `unsafe` 上下文中进行。

#### func asResource()

```cangjie
public func asResource(): CPointerResource<T>
```

功能：获取该指针 [CPointerResource](core_package_structs.md#struct-cpointerresourcet-where-t--ctype) 实例，该实例可以在 `try-with-resource` 语法上下文中实现内容自动释放。

返回值：

- [CPointerResource](core_package_structs.md#struct-cpointerresourcet-where-t--ctype)\<T> - 当前指针对应的 [CPointerResource](core_package_structs.md#struct-cpointerresourcet-where-t--ctype) 实例。

示例：

<!-- verify -->
```cangjie
foreign func malloc(size: UIntNative): CPointer<Unit>

main() {
    let sizeofInt64: UIntNative = 8
    var p1 = unsafe { malloc(sizeofInt64) }
    var ptr = unsafe { CPointer<Int64>(p1) }
    unsafe { ptr.write(10) }
    var ptrResource: CPointerResource<Int64> = ptr.asResource()
    try (r = ptrResource) {
        var p = r.value
        let num: Int64 = unsafe { p.read() }
        println(num)
    }
    println(ptrResource.isClosed())
}
```

运行结果：

```text
10
true
```

#### func isNotNull()

```cangjie
public func isNotNull(): Bool
```

功能：判断指针是否不为空。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果不为空返回 true，否则返回 false。

示例：

<!-- verify -->
```cangjie
foreign func malloc(size: UIntNative): CPointer<Unit>

foreign func free(ptr: CPointer<Unit>): Unit

main() {
    let p1 = CPointer<Int64>()
    println(p1.isNotNull())
    let sizeofInt64: UIntNative = 8
    var p2 = unsafe { malloc(sizeofInt64) }
    println(p2.isNotNull())
    unsafe { free(p2) }
}
```

运行结果：

```text
false
true
```

#### func isNull()

```cangjie
public func isNull(): Bool
```

功能：判断指针是否为空。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果为空返回 true，否则返回 false。

示例：

<!-- verify -->
```cangjie
foreign func malloc(size: UIntNative): CPointer<Unit>

foreign func free(ptr: CPointer<Unit>): Unit

main() {
    let sizeofInt64: UIntNative = 8
    var p1 = unsafe { malloc(sizeofInt64) }
    var ptr = unsafe { CPointer<Int64>(p1) }
    unsafe { ptr.write(10) }
    let num: Int64 = unsafe { ptr.read() }
    println(num)
    unsafe { free(p1) }
}
```

运行结果：

```text
10
```

#### func read()

```cangjie
public unsafe func read(): T
```

功能：读取第一个数据，该接口需要用户保证指针的合法性，否则发生未定义行为。

返回值：

- T - 该对象类型的第一个数据。

示例：

<!-- verify -->
```cangjie
foreign func malloc(size: UIntNative): CPointer<Unit>

foreign func free(ptr: CPointer<Unit>): Unit

main() {
    let p1 = CPointer<Int64>()
    println(p1.isNull())
    let sizeofInt64: UIntNative = 8
    var p2 = unsafe { malloc(sizeofInt64) }
    println(p2.isNull())
    unsafe { free(p2) }
}
```

运行结果：

```text
true
false
```

#### func read(Int64)

```cangjie
public unsafe func read(idx: Int64): T
```

功能：根据下标读取对应的数据，该接口需要用户保证指针的合法性，否则发生未定义行为。

参数：

- idx: [Int64](core_package_intrinsics.md#int64) - 要获取数据的下标。

返回值：

- T - 输入下标对应的数据。

示例：

<!-- verify -->
```cangjie
main() {
    var arr: Array<Int64> = [1, 2, 3, 4]
    var cptrHandle: CPointerHandle<Int64> = unsafe { acquireArrayRawData(arr) }
    var cptr: CPointer<Int64> = cptrHandle.pointer

    let num: Int64 = unsafe { cptr.read(2) }
    println("The third element of the array is ${num} ")

    unsafe { releaseArrayRawData<Int64>(cptrHandle) }
}
```

运行结果：

```text
The third element of the array is 3
```