### init(Array\<UInt8>, Int32, EncryptionAlgo, HmacAlgo, ?KdfAlgo, UInt32)

```cangjie
public init(encryptionKey: Array<UInt8>, iterationCount!: Int32 = 10000,
    encryptionAlgo!: EncryptionAlgo = EncryptionAlgo.Aes256Gcm,
    hmacAlgo!: HmacAlgo = HmacAlgo.Sha256, kdfAlgo!: ?KdfAlgo = None,
    cryptoPageSize!: UInt32 = 1024)
```

**功能：** CryptoParam类的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|encryptionKey|Array\<UInt8>|是|-|指定数据库加/解密使用的密钥。|
|iterationCount|Int32|否|10000|**命名参数。** 整数类型，指定数据库PBKDF2算法的迭代次数，默认值为10000。|
|encryptionAlgo|[EncryptionAlgo](#enum-encryptionalgo)|否|EncryptionAlgo.Aes256Gcm|**命名参数。** 指定数据库加解密使用的加密算法。如不指定，默认值为EncryptionAlgo.Aes256Gcm。|
|hmacAlgo|[HmacAlgo](#enum-hmacalgo)|否|HmacAlgo.Sha256|**命名参数。** 指定数据库加解密使用的HMAC算法。如不指定，默认值为HmacAlgo.Sha256。|
|kdfAlgo|?[KdfAlgo](#enum-kdfalgo)|否|None|**命名参数。** 指定数据库加解密使用的PBKDF2算法。如不指定，默认使用和HMAC算法相等的算法。|
|cryptoPageSize|UInt32|否|1024|**命名参数。** 整数类型，指定数据库加解密使用的页大小，单位为字节。如不指定，默认值为1024字节。|