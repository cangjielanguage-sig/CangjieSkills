## struct CPointerResource\<T> where T <: CType

```cangjie
public struct CPointerResource<T> <: Resource where T <: CType {
    public let value: CPointer<T>
}
```

功能：该结构体表示 [CPointer](core_package_intrinsics.md#cpointert) 对应的资源管理类型，其实例可以通过 [CPointer](core_package_intrinsics.md#cpointert) 的成员函数 `asResource` 获取。

父类型：

- [Resource](core_package_interfaces.md#interface-resource)

### let value

```cangjie
public let value: CPointer<T>
```

功能：表示当前实例管理的 [CPointer](core_package_intrinsics.md#cpointert)\<T> 类型实例。

类型：[CPointer](core_package_intrinsics.md#cpointert)\<T>

### func close()

```cangjie
public func close(): Unit
```

功能：释放其管理的 [CPointer](core_package_intrinsics.md#cpointert)\<T> 实例指向的内容。

### func isClosed()

```cangjie
public func isClosed(): Bool
```

功能：判断该指针内容是否已被释放。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 返回 true 为已释放。

## struct CStringResource

```cangjie
public struct CStringResource <: Resource {
    public let value: CString
}
```

功能：该结构体表示 [CString](core_package_intrinsics.md#cstring) 对应的资源管理类型，其实例可以通过 [CString](core_package_intrinsics.md#cstring) 的成员函数 `asResource` 获取。

父类型：

- [Resource](core_package_interfaces.md#interface-resource)

### let value

```cangjie
public let value: CString
```

功能：表示当前实例管理的 [CString](core_package_intrinsics.md#cstring) 资源。

类型：[CString](core_package_intrinsics.md#cstring)

### func close()

```cangjie
public func close(): Unit
```

功能：释放当前实例管理的 [CString](core_package_intrinsics.md#cstring) 类型实例指向的内容。

### func isClosed()

```cangjie
public func isClosed(): Bool
```

功能：判断该字符串是否被释放。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 返回 true 为已释放。