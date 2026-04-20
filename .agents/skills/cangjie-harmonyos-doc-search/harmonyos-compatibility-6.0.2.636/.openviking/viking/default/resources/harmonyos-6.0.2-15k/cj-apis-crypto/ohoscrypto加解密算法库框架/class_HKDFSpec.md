## class HKDFSpec

```cangjie
public class HKDFSpec <: KdfSpec {
    public init(algName!: String, key!: Array<UInt8>, salt!: Array<UInt8>, info!: Array<UInt8>, keySize!: Int32)
}
```

**功能：** 密钥派生函数参数[KdfSpec](#interface-kdfspec)的子类，作为HKDF密钥派生函数进行密钥派生时的输入。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- [KdfSpec](#interface-kdfspec)

### prop algName

```cangjie
public mut prop algName: String
```

**功能：** 指明密钥派生函数的算法名。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### prop info

```cangjie
public mut prop info: Array<UInt8>
```

**功能：** 拓展信息。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### prop key

```cangjie
public mut prop key: Array<UInt8>
```

**功能：** 密钥材料。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### prop keySize

```cangjie
public mut prop keySize: Int32
```

**功能：** 派生得到的密钥字节长度。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### prop salt

```cangjie
public mut prop salt: Array<UInt8>
```

**功能：** 盐值。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### init(String, Array\<UInt8>, Array\<UInt8>, Array\<UInt8>, Int32)

```cangjie
public init(algName!: String, key!: Array<UInt8>, salt!: Array<UInt8>, info!: Array<UInt8>, keySize!: Int32)
```

**功能：** 创建HKDFSpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-| **命名参数。** 指明密钥派生函数的算法名。|
|key|Array\<UInt8>|是|-| **命名参数。** 密钥材料。|
|salt|Array\<UInt8>|是|-| **命名参数。** 盐值。|
|info|Array\<UInt8>|是|-| **命名参数。** 拓展信息。|
|keySize|Int32|是|-| **命名参数。** 派生得到的密钥字节长度。|