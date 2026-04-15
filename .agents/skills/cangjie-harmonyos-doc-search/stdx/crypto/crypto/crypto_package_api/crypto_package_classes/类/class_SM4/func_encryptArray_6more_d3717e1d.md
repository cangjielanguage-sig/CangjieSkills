### func encrypt(Array\<Byte>)

```cangjie
public func encrypt(input: Array<Byte>): Array<Byte>
```

功能：加密一段数据数据。

参数：

- input: Array\<Byte> - 输入字节序列。

返回值：

- Array\<Byte> - 加密后的结果。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 加密失败，抛出异常。

### func encrypt(Array\<Byte>, Array\<Byte>)

```cangjie
public func encrypt(input: Array<Byte>, to!: Array<Byte>): Int64
```

功能：加密一段数据数据，指定输出数组长度会影响加解密结果。一般而言选填充模式，指定的密文数组长度不能小于明文数组长度加上一个 blockSize。

参数：

- input: Array\<Byte> - 待进行加密的数据。
- to!: Array\<Byte> - 输出数组。

返回值：

- Int64 - 输出长度。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 加密失败，抛出异常。
- IllegalArgumentException - 当 to 的 size = 0 时，抛出异常。

### func encrypt(InputStream, OutputStream)

```cangjie
public func encrypt(input: InputStream, output: OutputStream): Unit
```

功能：对输入流进行加密，一般如果数据过大无法一次对其加密，可以对数据流进行加密。

参数：

- input:InputStream  - 待加密的输入数据流。
- output: OutputStream - 解密后的输出数据流。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 加密失败，抛出异常。

### func decrypt(Array\<Byte>)

```cangjie
public func decrypt(input: Array<Byte>): Array<Byte>
```

功能：解密一段数据数据。

参数：

- input: Array\<Byte> - 输入字节序列。

返回值：

- Array\<Byte> - 解密后的结果。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解密失败，抛出异常。

### func decrypt(Array\<Byte>, Array\<Byte>)

```cangjie
public func decrypt(input: Array<Byte>,  to!: Array<Byte>): Int64
```

功能：解密一段数据数据，指定输出数组长度会影响加解密结果。一般而言，指定的明文数组长度不能小于密文数组长度减去一个 blockSize。

参数：

- input: Array\<Byte> - 待进行解密的数据。
- to!: Array\<Byte> - 输出数组。

返回值：

- Int64 - 输出长度。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解密失败，抛出异常。
- IllegalArgumentException - 当 to 的 size = 0 时，抛出异常。

### func decrypt(InputStream, OutputStream)

```cangjie
public func decrypt(input: InputStream, output: OutputStream): Unit
```

功能：对输入流进行解密，一般如果数据过大无法一次对其解密，可以对数据流进行解密。

参数：

- input:InputStream  - 待解密的输入数据流。
- output: OutputStream - 解密后的输出数据流。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解密失败，抛出异常。