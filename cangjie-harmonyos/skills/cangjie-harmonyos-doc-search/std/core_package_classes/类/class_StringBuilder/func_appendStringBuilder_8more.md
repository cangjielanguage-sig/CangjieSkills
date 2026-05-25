### func append(StringBuilder)

```cangjie
public func append(sb: StringBuilder): Unit
```

功能：在 [StringBuilder](core_package_classes.md#class-stringbuilder) 末尾插入参数 `sb` 指定的 [StringBuilder](core_package_classes.md#class-stringbuilder) 中的内容。

参数：

- sb: [StringBuilder](core_package_classes.md#class-stringbuilder) - 插入的 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例。

### func append(UInt16)

```cangjie
public func append(n: UInt16): Unit
```

功能：在 [StringBuilder](core_package_classes.md#class-stringbuilder) 末尾插入参数 `n` 的字符串表示。

参数：

- n: [UInt16](core_package_intrinsics.md#uint16) - 插入的 [UInt16](core_package_intrinsics.md#uint16) 类型的值。

### func append(UInt32)

```cangjie
public func append(n: UInt32): Unit
```

功能：在 [StringBuilder](core_package_classes.md#class-stringbuilder) 末尾插入参数 `n` 的字符串表示。

参数：

- n: [UInt32](core_package_intrinsics.md#uint32) - 插入的 [UInt32](core_package_intrinsics.md#uint32) 类型的值。

### func append(UInt64)

```cangjie
public func append(n: UInt64): Unit
```

功能：在 [StringBuilder](core_package_classes.md#class-stringbuilder) 末尾插入参数 `n` 的字符串表示。

参数：

- n: [UInt64](core_package_intrinsics.md#uint64) - 插入的 [UInt64](core_package_intrinsics.md#uint64) 类型的值。

### func append(UInt8)

```cangjie
public func append(n: UInt8): Unit
```

功能：在 [StringBuilder](core_package_classes.md#class-stringbuilder) 末尾插入参数 `n` 的字符串表示。

参数：

- n: [UInt8](core_package_intrinsics.md#uint8) - 插入的 [UInt8](core_package_intrinsics.md#uint8) 类型的值。

### func append\<T>(Array\<T>) where T <: ToString

```cangjie
public func append<T>(val: Array<T>): Unit where T <: ToString
```

功能：在 [StringBuilder](core_package_classes.md#class-stringbuilder) 末尾插入参数 `val` 指定的 [Array](core_package_structs.md#struct-arrayt)\<T> 的字符串表示，类型 `T` 需要实现 [ToString](core_package_interfaces.md#interface-tostring) 接口。

参数：

- val: [Array](core_package_structs.md#struct-arrayt)\<T> - 插入的 [Array](core_package_structs.md#struct-arrayt)\<T> 类型实例。

### func append\<T>(T) where T <: ToString

```cangjie
public func append<T>(v: T): Unit where T <: ToString
```

功能：在 [StringBuilder](core_package_classes.md#class-stringbuilder) 末尾插入参数 `v` 指定 `T` 类型的字符串表示，类型 `T` 需要实现 [ToString](core_package_interfaces.md#interface-tostring) 接口。

参数：

- v: T - 插入的 `T` 类型实例。

### func appendFromUtf8(Array\<Byte>)

```cangjie
public func appendFromUtf8(arr: Array<Byte>): Unit
```

功能：在 [StringBuilder](core_package_classes.md#class-stringbuilder) 末尾插入参数 `arr` 指向的字节数组。

该函数要求参数 `arr` 符合 UTF-8 编码，如果不符合，将抛出异常。

参数：

- arr: [Array](core_package_structs.md#struct-arrayt)\<[Byte](core_package_types.md#type-byte)> - 插入的字节数组。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当字节数组不符合 utf8 编码规则时，抛出异常。