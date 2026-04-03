## class CryptoParam

```cangjie
public class CryptoParam {
    public var encryptionKey: Array<UInt8>
    public var iterationCount: Int32
    public var encryptionAlgo: EncryptionAlgo
    public var hmacAlgo: HmacAlgo
    public var kdfAlgo:?KdfAlgo
    public var cryptoPageSize: UInt32

    public init(encryptionKey: Array<UInt8>, iterationCount!: Int32 = 10000,
        encryptionAlgo!: EncryptionAlgo = EncryptionAlgo.Aes256Gcm,
        hmacAlgo!: HmacAlgo = HmacAlgo.Sha256, kdfAlgo!: ?KdfAlgo = None,
        cryptoPageSize!: UInt32 = 1024)
}
```

**功能：** 数据库加密参数配置。此配置只有在StoreConfig的encrypt选项设置为true或密钥非空时有效。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var cryptoPageSize

```cangjie
public var cryptoPageSize: UInt32
```

**功能：** 整数类型，指定数据库加解密使用的页大小。

用户指定的页大小应为1024到65536范围内的整数，并且为2<sup>n</sup>。若指定值非整数，则向下取整。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var encryptionAlgo

```cangjie
public var encryptionAlgo: EncryptionAlgo
```

**功能：** 指定数据库加解密使用的加密算法。

**类型：** [EncryptionAlgo](#enum-encryptionalgo)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var encryptionKey

```cangjie
public var encryptionKey: Array<UInt8>
```

**功能：** 指定数据库加/解密使用的密钥。

如传入密钥为空，则由数据库负责生成并保存密钥，并使用生成的密钥打开数据库文件。

使用完后用户需要将密钥内容全部置为零。

**类型：** Array\<UInt8>

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var hmacAlgo

```cangjie
public var hmacAlgo: HmacAlgo
```

**功能：** 指定数据库加解密使用的HMAC算法。

**类型：** [HmacAlgo](#enum-hmacalgo)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var iterationCount

```cangjie
public var iterationCount: Int32
```

**功能：** 整数类型，指定数据库PBKDF2算法的迭代次数。

迭代次数应当为大于零的整数。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var kdfAlgo

```cangjie
public var kdfAlgo:?KdfAlgo
```

**功能：** 指定数据库加解密使用的PBKDF2算法。

**类型：** ?[KdfAlgo](#enum-kdfalgo)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22