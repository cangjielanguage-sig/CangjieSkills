### extend CString <: ToString

```cangjie
extend CString <: ToString
```

功能：为 [CString](core_package_intrinsics.md#cstring) 类型扩展一些字符串指针常用方法，包括判空、获取长度、判等、获取子串等。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func asResource()

```cangjie
public func asResource(): CStringResource
```

功能：获取当前 [CString](core_package_intrinsics.md#cstring) 实例对应的 [CStringResource](core_package_structs.md#struct-cstringresource) C 字符串资源类型实例。

[CStringResource](core_package_structs.md#struct-cstringresource) 实现了 [Resource](core_package_interfaces.md#interface-resource) 接口，可以在 `try-with-resource` 语法上下文中实现资源自动释放。

返回值：

- [CStringResource](core_package_structs.md#struct-cstringresource) - 对应的 [CStringResource](core_package_structs.md#struct-cstringresource) C 字符串资源类型实例。

示例：

<!-- verify -->
```cangjie
foreign func malloc(size: UIntNative): CPointer<Unit>

main() {
    var str: CString = unsafe { LibC.mallocCString("hello") }
    var ptrResource: CStringResource = str.asResource()
    try (r = ptrResource) {
        var p = r.value
        println(p.size())
    }
    println(ptrResource.isClosed())
}
```

运行结果：

```text
5
true
```

#### func compare(CString)

```cangjie
public func compare(str: CString): Int32
```

功能：按字典序比较两个字符串，同 C 语言中的 `strcmp`。

参数：

- str: [CString](core_package_intrinsics.md#cstring) - 比较的目标字符串。

返回值：

- [Int32](core_package_intrinsics.md#int32) - 两者相等返回 0，如果当前字符串比参数 str 小，返回 -1，否则返回 1。

异常：

- [IllegalMemoryException](core_package_exceptions.md#class-illegalmemoryexception) - 如果被比较的两个 [CString](core_package_intrinsics.md#cstring) 中存在空指针，抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    var str2: CString = unsafe { LibC.mallocCString("hello") }
    println(str1.compare(str2))

    var str3: CString = unsafe { LibC.mallocCString("hello") }
    var str4: CString = unsafe { LibC.mallocCString("hellow") }
    println(str3.compare(str4))

    var str5: CString = unsafe { LibC.mallocCString("hello") }
    var str6: CString = unsafe { LibC.mallocCString("allow") }
    println(str5.compare(str6))

    unsafe {
        LibC.free(str1)
        LibC.free(str2)
        LibC.free(str3)
        LibC.free(str4)
        LibC.free(str5)
        LibC.free(str6)
    }
}
```

运行结果：

```text
0
-1
1
```

#### func endsWith(CString)

```cangjie
public func endsWith(suffix: CString): Bool
```

功能：判断字符串是否包含指定后缀。

参数：

- suffix: [CString](core_package_intrinsics.md#cstring) - 匹配的目标后缀字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果该字符串包含 suffix 后缀，返回 true，如果该字符串不包含 suffix 后缀，返回 false，特别地，如果原字符串或者 suffix 后缀字符串指针为空，均返回 false。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    var str2: CString = unsafe { LibC.mallocCString("lo") }
    var str3: CString = unsafe { LibC.mallocCString("ao") }

    println(str1.endsWith(str2))
    println(str1.endsWith(str3))

    unsafe {
        LibC.free(str1)
        LibC.free(str2)
        LibC.free(str3)
    }
}
```

运行结果：

```text
true
false
```