### func writeln(UInt64)

```cangjie
public func writeln(v: UInt64): Unit
```

功能：写入 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 类型 + 换行符。

参数：

- v: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 类型的实例。

### func writeln(UInt8)

```cangjie
public func writeln(v: UInt8): Unit
```

功能：写入 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 类型 + 换行符。

参数：

- v: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 类型的实例。

### func writeln\<T>(T) where T <: ToString

```cangjie
public func writeln<T>(v: T): Unit where T <: ToString
```

功能：写入 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 类型 + 换行符。

参数：

- v: T - [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 类型的实例。

### extend\<T> StringWriter\<T> <: Resource where T <: Resource

```cangjie
extend<T> StringWriter<T> <: Resource where T <: Resource
```

功能：为 [StringWriter](./io_package_classes.md#class-stringwritert-where-t--outputstream) 实现 [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource) 接口，该类型对象可在 `try-with-resource` 语法上下文中实现自动资源释放。

父类型：

- [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource)

#### func close()

```cangjie
public func close(): Unit
```

功能：关闭当前流。

> **注意：**
>
> 调用此方法后不可再调用 [StringWriter](io_package_classes.md#class-stringwritert-where-t--outputstream) 的其他接口，否则会造成非预期现象。

#### func isClosed()

```cangjie
public func isClosed(): Bool
```

功能：判断当前流是否关闭。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果当前流已经被关闭，返回 true，否则返回 false。

### extend\<T> StringWriter\<T> <: Seekable where T <: Seekable

```cangjie
extend<T> StringWriter<T> <: Seekable where T <: Seekable
```

功能：为 [StringWriter](./io_package_classes.md#class-stringwritert-where-t--outputstream) 实现 [Seekable](./io_package_interfaces.md#interface-seekable) 接口，支持查询数据长度，移动光标等操作。

父类型：

- [Seekable](io_package_interfaces.md#interface-seekable)

#### func seek(SeekPosition)

```cangjie
public func seek(sp: SeekPosition): Int64
```

功能：移动光标到指定的位置。

> **说明：**
>
> - 指定的位置不能位于流中数据头部之前。
> - 指定位置可以超过流中数据末尾。

参数：

- sp: [SeekPosition](io_package_enums.md#enum-seekposition) - 指定光标移动后的位置。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回流中数据的起点到移动后位置的偏移量（以字节为单位）。

异常：

- [IOException](io_package_exceptions.md#class-ioexception) - 当指定的位置位于流中数据头部之前时，抛出异常。