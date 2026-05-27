#### func equals(CString)

```cangjie
public func equals(rhs: CString): Bool
```

功能：判断两个字符串是否相等。

参数：

- rhs: [CString](core_package_intrinsics.md#cstring) - 比较的目标字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果两个字符串相等，返回 true，否则返回 false。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    var str2: CString = unsafe { LibC.mallocCString("hello") }
    var str3: CString = unsafe { LibC.mallocCString("Hello") }
    println(str1.equals(str2))
    println(str1.equals(str3))

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

#### func equalsLower(CString)

```cangjie
public func equalsLower(rhs: CString): Bool
```

功能：判断两个字符串是否相等，忽略大小写。

参数：

- rhs: [CString](core_package_intrinsics.md#cstring) - 匹配的目标字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果两个字符串忽略大小写相等，返回 true，否则返回 false。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    var str2: CString = unsafe { LibC.mallocCString("HELLO") }
    var str3: CString = unsafe { LibC.mallocCString("Hello") }
    println(str1.equalsLower(str2))
    println(str1.equalsLower(str3))

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
true
```

#### func getChars()

```cangjie
public func getChars(): CPointer<UInt8>
```

功能：获取该字符串的指针。

返回值：

- [CPointer](./core_package_intrinsics.md#cpointert)\<[UInt8](./core_package_intrinsics.md#uint8)> - 该字符串的指针。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    var ptr: CPointer<UInt8> = unsafe { str1.getChars() }
    var c: UInt8 = unsafe { ptr.read() }
    println(c) // h的ascii码为104
    unsafe {
        LibC.free(str1)
    }
}
```

运行结果：

```text
104
```

#### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断字符串是否为空字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果为空字符串或字符串指针为空，返回 true，否则返回 false。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    println(str1.isEmpty())

    unsafe {
        LibC.free(str1)
    }
}
```

运行结果：

```text
false
```

#### func isNotEmpty()

```cangjie
public func isNotEmpty(): Bool
```

功能：判断字符串是否不为空字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果不为空字符串，返回 true，如果字符串指针为空，返回 false。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    println(str1.isNotEmpty())

    unsafe {
        LibC.free(str1)
    }
}
```

运行结果：

```text
true
```

#### func isNull()

```cangjie
public func isNull(): Bool
```

功能：判断字符串指针是否为空。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果字符串指针为空，返回 true，否则返回 false。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    println(str1.isNull())

    unsafe {
        LibC.free(str1)
    }
}
```

运行结果：

```text
false
```

#### func size()

```cangjie
public func size(): Int64
```

功能：返回该字符串长度，同 C 语言中的 `strlen`。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 字符串长度。

示例：

<!-- verify -->
```cangjie
main() {
    var str1: CString = unsafe { LibC.mallocCString("hello") }
    println(str1.size())

    unsafe {
        LibC.free(str1)
    }
}
```

运行结果：

```text
5
```