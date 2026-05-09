## func acquireArrayRawData\<T>(Array\<T>) where T <: CType

```cangjie
public unsafe func acquireArrayRawData<T>(arr: Array<T>): CPointerHandle<T> where T <: CType
```

功能：获取 [Array](core_package_structs.md#struct-arrayt)\<T> 中数据的原始指针实例，指针实例指向数组首元素的地址，T 需要满足 [CType](core_package_interfaces.md#interface-ctype) 约束。

> **注意：**
>
> 指针使用完后需要及时用 [releaseArrayRawData](core_package_funcs.md#func-releasearrayrawdatatcpointerhandlet-where-t--ctype) 函数释放该指针。
> 指针的获取和释放之间仅可包含简单的 foreign C 函数调用等逻辑，不构造例如 [CString](core_package_intrinsics.md#cstring) 等的仓颉对象，否则可能造成不可预期现象。

参数：

- arr: [Array](./core_package_structs.md#struct-arrayt)\<T> - 待获取原始指针的数组。

返回值：

- [CPointerHandle](core_package_structs.md#struct-cpointerhandlet-where-t--ctype)\<T> - 数组的原始指针实例。

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

## func alignOf\<T>() where T <: CType

```cangjie
public func alignOf<T>(): UIntNative where T <: CType
```

功能：获取类型 T 的内存对齐值。

返回值：

- [UIntNative](core_package_intrinsics.md#uintnative) - 类型 T 满足内存对齐要求的字节数。

示例：

<!-- verify -->
```cangjie
@C
struct Data {
    var a: Int64 = 0
    var b: Float32 = 0.0
}

main() {
    let alignSizeInt8: UIntNative = alignOf<Int8>()
    println("The memory alignment requirement for Int64 type is ${alignSizeInt8} byte")

    let alignSizeInt32: UIntNative = alignOf<Int32>()
    println("The memory alignment requirement for Int64 type is ${alignSizeInt32} bytes")

    let alignSizeInt64: UIntNative = alignOf<Int64>()
    println("The memory alignment requirement for Int64 type is ${alignSizeInt64} bytes")

    let alignSizeData: UIntNative = alignOf<Data>()
    println("The memory alignment requirement for Int64 type is ${alignSizeData} bytes")
}
```

运行结果：

```text
The memory alignment requirement for Int64 type is 1 byte
The memory alignment requirement for Int64 type is 4 bytes
The memory alignment requirement for Int64 type is 8 bytes
The memory alignment requirement for Int64 type is 8 bytes
```

## func eprint(String, Bool)

```cangjie
public func eprint(str: String, flush!: Bool = true): Unit
```

功能：将指定字符串打印到标准错误文本流。

如抛出异常时，消息将打印到标准错误文本流（stderr），而不是标准输出（stdout）。

参数：

- str: [String](core_package_structs.md#struct-string) - 待输出的字符串。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否将缓存数据区的内容立即刷新写入与标准错误流相关的文件和设备中，true 表示立即刷新，false 表示暂不刷新 ，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    try {
        throw NegativeArraySizeException("I am an Exception!")
    } catch (e: NegativeArraySizeException) {
        eprint("NegativeArraySizeException is caught!", flush: true)
    }
}
```

运行结果：

```text
NegativeArraySizeException is caught!
```