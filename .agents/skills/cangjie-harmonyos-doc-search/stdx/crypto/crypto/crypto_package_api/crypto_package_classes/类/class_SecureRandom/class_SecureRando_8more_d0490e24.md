## class SecureRandom

```cangjie
public class SecureRandom {
    public init(priv!: Bool = false)
}
```

功能：用于生成加密安全的伪随机数。

和 Random 相比，主要有三个方面不同：

- 随机数种子： Random 使用系统时钟作为默认的种子，时间戳一样，结果就相同；[SecureRandom](crypto_package_classes.md#class-securerandom) 使用操作系统或者硬件提供的随机数种子，生成的是真随机数。

- 随机数生成： Random 使用了梅森旋转伪随机生成器；[SecureRandom](crypto_package_classes.md#class-securerandom) 则使用了 openssl 库提供的 [MD5](../../digest/digest_package_api/digest_package_classes.md#class-md5) 等随机算法，使用熵源生成真随机数；如果硬件支持，还可以使用硬件随机数生成器来生成安全性更强的随机数。
- 安全性： Random 不能用于加密安全的应用或者隐私数据的保护，可以使用 [SecureRandom](crypto_package_classes.md#class-securerandom)。

使用示例见 [SecureRandom 使用](../crypto_samples/sample_secure_random.md)。

### init(Bool)

```cangjie
public init(priv!: Bool = false)
```

功能：创建 [SecureRandom](crypto_package_classes.md#class-securerandom) 实例，可指定是否使用更加安全的加密安全伪随机生成器，加密安全伪随机生成器可用于会话密钥和证书私钥等加密场景。

参数：

- priv!: Bool - 设置为 true 表示使用加密安全伪随机生成器。

### func nextBits(UInt64)

```cangjie
public func nextBits(bits: UInt64): UInt64
```

功能：生成一个指定位长的随机整数。

参数：

- bits: UInt64 - 要生成的随机数的位数，取值范围 (0, 64]。

返回值：

- UInt64 - 生成的用户指定位长的随机数。

异常：

- IllegalArgumentException - 如果 `bits` 等于 0，或大于 64，超过所能截取的 UInt64 长度，则抛出异常。
- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextBool()

```cangjie
public func nextBool(): Bool
```

功能：获取一个随机的 Bool 类型实例。

返回值：

- Bool - 一个随机的 Bool 类型实例。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextBytes(Array\<Byte>)

```cangjie
public func nextBytes(bytes: Array<Byte>): Unit
```

功能：生成随机数替换入参数组中的每个元素。

参数：

- bytes: Array\<Byte> - 被替换的数组。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextBytes(Int32)

```cangjie
public func nextBytes(length: Int32): Array<Byte>
```

功能：获取一个指定长度的随机字节的数组。

参数：

- length: Int32 - 要生成的随机字节数组的长度。

返回值：

- Array\<Byte> - 一个随机字节数组。

异常：

- IllegalArgumentException - 当参数 length 小于等于 0，抛出异常。
- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextFloat16()

```cangjie
public func nextFloat16(): Float16
```

功能：获取一个 Float16 类型且在区间 [0.0, 1.0) 内的随机数。

返回值：

- Float16 - 一个 Float16 类型的随机数。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextFloat32()

```cangjie
public func nextFloat32(): Float32
```

功能：获取一个 Float32 类型且在区间 [0.0, 1.0) 内的随机数。

返回值：

- Float32 - 一个 Float32 类型的随机数。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。