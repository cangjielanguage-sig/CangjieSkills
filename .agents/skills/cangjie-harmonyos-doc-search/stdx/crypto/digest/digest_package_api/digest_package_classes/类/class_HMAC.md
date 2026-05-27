## class HMAC

```cangjie
public class HMAC <: Digest {
    public init(key: Array<Byte>, digest: () -> Digest)
    public init(key: Array<Byte>, algorithm: HashType)
}
```

功能：提供 [HMAC](digest_package_classes.md#class-hmac) 算法的实现。目前支持的摘要算法包括 MD5、SHA1、SHA224、SHA256、SHA384、SHA512、SM3。

父类型：

- Digest

### prop algorithm

```cangjie
public prop algorithm: String
```

功能：[HMAC](digest_package_classes.md#class-hmac) 所选 Hash 算法的算法名称。

类型：String

### prop blockSize

```cangjie
public prop blockSize: Int64
```

功能：[HMAC](digest_package_classes.md#class-hmac) 所选 Hash 算法信息块长度，单位字节。

类型：Int64

### prop size

```cangjie
public prop size: Int64
```

功能：[HMAC](digest_package_classes.md#class-hmac) 所选 Hash 算法的摘要信息长度，单位字节。

类型：Int64

### init(Array\<Byte>, () -> Digest)

```cangjie
public init(key: Array<Byte>, digest: () -> Digest)
```

功能：构造函数，创建 [HMAC](digest_package_classes.md#class-hmac) 对象。

参数：

- key: Array\<Byte> - 密钥，建议该参数不小于所选 Hash 算法摘要的长度。
- digest: () -> Digest - hash 算法。

异常：

- [CryptoException](digest_package_exceptions.md#class-cryptoexception) - key 值为空时，抛出异常。

### init(Array\<Byte>, HashType)

```cangjie
public init(key: Array<Byte>, algorithm: HashType)
```

功能：构造函数，创建 [HMAC](digest_package_classes.md#class-hmac) 对象。

参数：

- key: Array\<Byte> - 密钥，建议该参数不小于所选 Hash 算法摘要的长度。
- algorithm: [HashType](digest_package_structs.md#struct-hashtype) - hash 算法。

异常：

- [CryptoException](digest_package_exceptions.md#class-cryptoexception) - key 值为空时，抛出异常。

### static func equal(Array\<Byte>, Array\<Byte>)

```cangjie
public static func equal(mac1: Array<Byte>, mac2: Array<Byte>): Bool
```

功能：比较两个信息摘要是否相等，且不泄露比较时间，即比较不采用传统短路原则，从而防止 timing attack 类型的攻击。

参数：

- mac1: Array\<Byte> - 需要比较的信息摘要序列。
- mac2: Array\<Byte> - 需要比较的信息摘要序列。

返回值：

- Bool - 信息摘要是否相同，true 相同，false 不相同。

### func finish()

```cangjie
public func finish(): Array<Byte>
```

功能：返回生成的信息摘要值，注意调用 finish 后不可以再进行摘要计算，如重新计算需要 reset 重置上下文。

返回值：

- Array\<Byte> - 生成的信息摘要字节序列。

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

功能：重置 [HMAC](digest_package_classes.md#class-hmac) 对象到初始状态，清理 [HMAC](digest_package_classes.md#class-hmac) 上下文。

异常：

- [CryptoException](digest_package_exceptions.md#class-cryptoexception) - 当内部错误，重置失败，抛此异常。

### func write(Array\<Byte>)

```cangjie
public func write(buffer: Array<Byte>): Unit
```

功能：使用给定的 buffer 更新 [HMAC](digest_package_classes.md#class-hmac) 对象，在调用 finish 前可以多次更新。

参数：

- buffer: Array\<Byte> - 需要追加的字节序列。

异常：

- [CryptoException](digest_package_exceptions.md#class-cryptoexception) - 当 buffer 为空、finish 已经调用生成信息摘要场景，抛此异常。