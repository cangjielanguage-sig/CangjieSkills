### func nextUInt64()

```cangjie
public func nextUInt64(): UInt64
```

功能：获取一个 UInt64 类型的随机数。

返回值：

- UInt64 - 一个 UInt64 类型的随机数。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextUInt64(UInt64)

```cangjie
public func nextUInt64(max: UInt64): UInt64
```

功能：获取一个 UInt64 类型且在区间 [0, max) 内的随机数。

参数：

- max: UInt64 - 区间最大值。

返回值：

- UInt64 - 一个 UInt64 类型的随机数。

异常：

- IllegalArgumentException - 当 max 为 0 时，抛出异常。
- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextUInt8()

```cangjie
public func nextUInt8(): UInt8
```

功能：获取一个 UInt8 类型的随机数。

返回值：

- UInt8 - 一个 UInt8 类型的随机数。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextUInt8(UInt8)

```cangjie
public func nextUInt8(max: UInt8): UInt8
```

功能：获取一个 UInt8 类型且在区间 [0, max) 内的随机数。

参数：

- max: UInt8 - 区间最大值。

返回值：

- UInt8 - 一个 UInt8 类型的随机数。

异常：

- IllegalArgumentException - 当 max 为 0 时，抛出异常。
- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。