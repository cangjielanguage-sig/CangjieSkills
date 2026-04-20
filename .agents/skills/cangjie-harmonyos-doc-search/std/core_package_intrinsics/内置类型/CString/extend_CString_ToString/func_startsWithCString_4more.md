#### func startsWith(CString)

```cangjie
public func startsWith(prefix: CString): Bool
```

功能：判断字符串是否包含指定前缀。

参数：

- prefix: [CString](core_package_intrinsics.md#cstring) - 匹配的目标前缀字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果该字符串包含 prefix 前缀，返回 true，如果该字符串不包含 prefix 前缀，返回 false，特别地，如果原字符串或者 prefix 前缀字符串指针为空，均返回 false。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    var str2: CString = unsafe { LibC.mallocCString("he") }
    println(str1.startsWith(str2))

    unsafe {
        LibC.free(str1)
        LibC.free(str2)
    }
}
```

运行结果：

```text
true
```

#### func subCString(UIntNative)

```cangjie
public func subCString(beginIndex: UIntNative): CString
```

功能：截取指定位置开始至字符串结束的子串。

> **注意：**
>
> 1. 该接口返回为字符串的副本，返回的子串使用完后需要手动 free。
> 2. 如果 beginIndex 与字符串长度相等，将返回空指针。

参数：

- beginIndex: [UIntNative](core_package_intrinsics.md#uintnative) - 截取的起始位置，取值范围为 [0, this.size()]。

返回值：

- [CString](core_package_intrinsics.md#cstring) - 截取的子串。

异常：

- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - 如果 beginIndex 大于字符串长度，抛出异常。
- [IllegalMemoryException](core_package_exceptions.md#class-illegalmemoryexception) - 如果内存申请失败或内存拷贝失败时，抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    let index: UIntNative = 2
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    var str2: CString = str1.subCString(index)
    println(str2)

    unsafe {
        LibC.free(str1)
        LibC.free(str2)
    }
}
```

运行结果：

```text
llo
```

#### func subCString(UIntNative, UIntNative)

```cangjie
public func subCString(beginIndex: UIntNative, subLen: UIntNative): CString
```

功能：截取字符串的子串，指定起始位置和截取长度。

如果截取的末尾位置超出字符串长度，截取至字符串末尾。

> **注意：**
>
> 1. 该接口返回为字符串的副本，返回的子串使用完后需要手动 free。
> 2. 如果 beginIndex 等于于字符串长度，或 subLen 等于 0，返回空指针。

参数：

- beginIndex: [UIntNative](core_package_intrinsics.md#uintnative) - 截取的起始位置，取值范围为 [0, this.size()]。
- subLen: [UIntNative](core_package_intrinsics.md#uintnative) - 截取长度，取值范围为 [0, [UIntNative](core_package_intrinsics.md#uintnative).Max]。

返回值：

- [CString](core_package_intrinsics.md#cstring) - 截取的子串。

异常：

- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - 如果 beginIndex 大于字符串长度，抛出异常。
- [IllegalMemoryException](core_package_exceptions.md#class-illegalmemoryexception) - 如果内存申请失败或内存拷贝失败时，抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    let index: UIntNative = 2
    let len: UIntNative = 2
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    var str2: CString = str1.subCString(index, len)
    println(str2)

    unsafe {
        LibC.free(str1)
        LibC.free(str2)
    }
}
```

运行结果：

```text
ll
```

#### func toString()

```cangjie
public func toString(): String
```

功能：将 [CString](core_package_intrinsics.md#cstring) 类型转为仓颉的 [String](core_package_structs.md#struct-string) 类型。

返回值：

- [String](core_package_structs.md#struct-string) - 转换后的字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 不合法的 UTF-8 字节序列。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    println(str1.toString())

    unsafe {
        LibC.free(str1)
    }
}
```

运行结果：

```text
hello
```