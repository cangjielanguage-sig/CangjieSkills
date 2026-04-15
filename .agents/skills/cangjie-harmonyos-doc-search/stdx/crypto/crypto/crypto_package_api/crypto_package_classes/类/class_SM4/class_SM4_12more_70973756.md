## class SM4

```cangjie
public class SM4 <: BlockCipher {
    public init(
        optMode: OperationMode,
        key: Array<Byte>,
        iv!: Array<Byte> = Array<Byte>(),
        paddingMode!: PaddingMode = PaddingMode.PKCS7Padding,
        aad!: Array<Byte> = Array<Byte>(),
        tagSize!: Int64 = 16
    )
}
```

功能：提供国密 SM4 对称加解密。

目前 SM4 支持 的加解密工作模式由 [OperationMode](crypto_package_structs.md#struct-operationmode) 定义，目前支持 ECB、CBC、OFB、CFB、CTR、GCM 模式。

不同的工作模式可能对应的加解密实现不同，安全性也不同。需要选择和场景适配的加解密工作模式。

iv 初始化向量在 GCM 模式下可以设置推荐长度是 12 字节，在 CBC、OFB、CFB、CTR 模式下 iv 长度是 16 字节，在 ECB 模式下 iv 可以不设置。

paddingMode 填充模式模式由 [PaddingMode](crypto_package_structs.md#struct-paddingmode) 定义， 目前支持 NoPadding 非填充、PKCS7Padding PKCS7 填充。默认是 PKCS7 填充。

paddingMode 设置对 ECB 和 CBC 有效，ECB 和 CBC 分组加解密需要分组长度等于 blockSize。会根据填充模式进行填充。 paddingMode 设置对 OFB、CFB、CTR、GCM 工作模式无效，这些工作模式均无需填充。

如果选择 NoPadding 模式，即不填充。则在 ECB 和 CBC 工作模式下用户需要对数据是否可以分组负责，如果数据不能分组，或者最后一组数据长度不足 blockSize 则会报错。

aad 附加数据，仅在 GCM 模式下使用，由用户填充，参与摘要计算，默认为空。

tagSize 设置摘要长度，仅在 GCM 模式下使用，默认值为 SM4_GCM_TAG_SIZE 16 字节，最小不能低于 12 字节，最大不能超过 16 字节。

如果是 GCM 工作模式。加密结果的后 tagSize 字节是摘要数据。

使用示例见 [SM4 使用](../crypto_samples/sample_crypto.md)。

> **注意：**
>
> GCM 模式需要 OpenSSL 3.2 或者以上版本。

父类型：

- BlockCipher

### init(OperationMode, Array\<Byte>, Array\<Byte>, PaddingMode, Array\<Byte>, Int64)

```cangjie
public init(
    optMode: OperationMode,
    key: Array<Byte>,
    iv!: Array<Byte> = Array<Byte>(),
    paddingMode!: PaddingMode = PaddingMode.PKCS7Padding,
    aad!: Array<Byte> = Array<Byte>(),
    tagSize!: Int64 = 16
)
```

功能：创建 [SM4](crypto_package_classes.md#class-sm4) 实例，可指定在不同工作模式下参数。

参数：

- optMode: [OperationMode](crypto_package_structs.md#struct-operationmode) - 设置加解密工作模式。
- key: Array\<Byte> - 密钥，长度为 16 字节。
- iv!: Array\<Byte> - 初始化向量。
- paddingMode!: [PaddingMode](crypto_package_structs.md#struct-paddingmode) - 设置填充模式。
- aad!: Array\<Byte> - 设置附加数据。
- tagSize!: Int64 - 设置摘要长度。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 参数设置不正确，实例化失败。

### prop aad

```cangjie
public prop aad: Array<Byte>
```

功能：附加数据。

类型：Array\<Byte>

### prop algorithm

```cangjie
public prop algorithm: String
```

功能：获取分组加解密算法的算法名称。

类型：String

### prop blockSize

```cangjie
public prop blockSize: Int64
```

功能：分组长度，单位字节。

类型：Int64

### prop keySize

```cangjie
public prop keySize: Int64
```

功能：密钥长度。

类型：Int64

### prop key

```cangjie
public prop key: Array<Byte>
```

功能：密钥。

类型：Array\<Byte>

### prop optMode

```cangjie
public prop optMode: OperationMode
```

功能：工作模式。

类型：[OperationMode](crypto_package_structs.md#struct-operationmode)

### prop paddingMode

```cangjie
public prop paddingMode: PaddingMode
```

功能：填充模式。

类型：[PaddingMode](crypto_package_structs.md#struct-paddingmode)

### prop iv

```cangjie
public prop iv: Array<Byte>
```

功能：初始化向量。

类型：Array\<Byte>

### prop ivSize

```cangjie
public prop ivSize: Int64
```

功能：初始化向量长度。

类型：Int64

### prop tagSize

```cangjie
public prop tagSize: Int64
```

功能：摘要长度。

类型：Int64