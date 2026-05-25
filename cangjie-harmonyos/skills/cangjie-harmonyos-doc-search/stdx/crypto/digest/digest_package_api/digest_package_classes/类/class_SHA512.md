## class SHA512

```cangjie
public class SHA512 <: Digest {
    public init()
}
```

功能：提供 [SHA512](digest_package_classes.md#class-sha512) 算法的实现接口。使用示例见 [SHA512 算法示例](../digest_samples/sample_digest.md#sha512-算法示例)。

父类型：

- Digest

### prop algorithm

```cangjie
public prop algorithm: String
```

功能：[SHA512](digest_package_classes.md#class-sha512) 摘要算法的算法名称。

类型：String

### prop blockSize

```cangjie
public prop blockSize: Int64
```

功能：[SHA512](digest_package_classes.md#class-sha512) 信息块长度，单位字节。

类型：Int64

### prop size

```cangjie
public prop size: Int64
```

功能：[SHA512](digest_package_classes.md#class-sha512) 摘要信息长度，单位字节。

类型：Int64

### init()

```cangjie
public init()
```

功能：无参构造函数，创建 [SHA512](digest_package_classes.md#class-sha512) 对象。

### func finish()

```cangjie
public func finish(): Array<Byte>
```

功能：返回生成的 [SHA512](digest_package_classes.md#class-sha512) 值，注意调用 finish 后 [SHA512](digest_package_classes.md#class-sha512) 上下文会发生改变，finish 后不可以再进行摘要计算，如重新计算需要 reset 重置上下文。

返回值：

- Array\<Byte> - 生成的 [SHA512](digest_package_classes.md#class-sha512) 字节序列。

异常：

- [CryptoException](digest_package_exceptions.md#class-cryptoexception) - 未重置上下文再次调用 finish 进行摘要计算，抛此异常。

### func finish(Array\<Byte>)

```cangjie
public func finish(to!: Array<Byte>): Unit
```

功能：获取生成的信息摘要值，注意调用 finish 后不可以再进行摘要计算，如重新计算需要 reset 重置上下文。

参数：

- to!: Array\<Byte> - 目标数组。

异常：

- [CryptoException](digest_package_exceptions.md#class-cryptoexception) - 未重置上下文再次调用 finish 进行摘要计算或者指定输出数组大小不等于摘要算法信息长度，抛此异常。

### func reset()

```cangjie
public func reset(): Unit
```

功能：重置 [SHA512](digest_package_classes.md#class-sha512) 对象到初始状态，清理 [SHA512](digest_package_classes.md#class-sha512) 上下文。

### func write(Array\<Byte>)

```cangjie
public func write(buffer: Array<Byte>): Unit
```

功能：使用给定的 buffer 更新 [SHA512](digest_package_classes.md#class-sha512) 对象，在调用 finish 前可以多次更新。

参数：

- buffer: Array\<Byte> - 输入字节序列。

异常：

- [CryptoException](digest_package_exceptions.md#class-cryptoexception) - 已经调用 finish 进行摘要计算后未重置上下文，抛此异常。