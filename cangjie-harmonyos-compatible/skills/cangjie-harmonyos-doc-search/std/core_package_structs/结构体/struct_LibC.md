## struct LibC

```cangjie
public struct LibC {}
```

功能：提供了仓颉中较为高频使用的 C 接口，如申请、释放堆上 [CType](core_package_interfaces.md#interface-ctype) 实例。

### static func free(CString)

```cangjie
public unsafe static  func free(cstr: CString): Unit
```

功能：释放 C 风格字符串。

参数：

- cstr: [CString](core_package_intrinsics.md#cstring) - 需要释放的 C 风格字符串。

### static func free\<T>(CPointer\<T>) where T <: CType

```cangjie
public unsafe static  func free<T>(p: CPointer<T>): Unit where T <: CType
```

功能：释放指针 p 指向的堆内存。

参数：

- p: [CPointer](core_package_intrinsics.md#cpointert)\<T> - 表示需要被释放的内存地址。

### static func malloc\<T>(Int64) where T <: CType

```cangjie
public static func malloc<T>(count!: Int64 = 1): CPointer<T> where T <: CType
```

功能：在堆中申请指定个数的 `T` 实例，并返回其起始指针。

申请内存长度为 [sizeOf](core_package_funcs.md#func-sizeoft-where-t--ctype)\<T>() * [count](../../collection/collection_package_api/collection_package_function.md#func-counttiterablet)。

参数：

- [count](../../collection/collection_package_api/collection_package_function.md#func-counttiterablet)!: [Int64](core_package_intrinsics.md#int64) - 为可选参数，默认为 1，表示申请 T 类型的个数。

返回值：

- [CPointer](core_package_intrinsics.md#cpointert)\<T> - 申请的 T 类型指针。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 入参为负数时，抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    var p = unsafe { LibC.malloc<Int64>(count: 1) }
    unsafe { p.write(8) }
    let value: Int64 = unsafe { p.read() }
    println(value)
    unsafe { LibC.free<Int64>(p) }
}
```

运行结果：

```text
8
```

### static func mallocCString(String)

```cangjie
public unsafe static  func mallocCString(str: String): CString
```

功能：通过 [String](core_package_structs.md#struct-string) 申请与之字符内容相同的 C 风格字符串。

构造的 C 风格字符串将以 '\0' 结束。当异常场景如系统内存不足时，返回字符串指针可能为空，故使用前需要进行空指针检查。

参数：

- str: [String](core_package_structs.md#struct-string) - 根据该仓颉字符串构造 C 字符串。

返回值：

- [CString](core_package_intrinsics.md#cstring) - 新构造的 C 风格字符串。

异常：

- [IllegalMemoryException](core_package_exceptions.md#class-illegalmemoryexception) - 内存不足时，抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    var str = unsafe { LibC.mallocCString("I like Cangjie") }
    println(str)
    unsafe { LibC.free(str) }
}
```

运行结果：

```text
I like Cangjie
```