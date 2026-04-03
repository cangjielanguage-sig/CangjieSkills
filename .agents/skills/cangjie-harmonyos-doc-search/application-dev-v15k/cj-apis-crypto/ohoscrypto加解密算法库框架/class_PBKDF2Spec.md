## class PBKDF2Spec

```cangjie
public class PBKDF2Spec <: KdfSpec {
    public init(algName!: String, password!: Array<UInt8>, salt!: Array<UInt8>, iterations!: Int32, keySize!: Int32)
}
```

**功能：** 密钥派生函数参数[KdfSpec](#interface-kdfspec)的子类，作为PBKDF2密钥派生函数进行密钥派生时的输入。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- [KdfSpec](#interface-kdfspec)

### prop algName

```cangjie
public mut prop algName: String
```

**功能：** 指定密钥派生函数的算法名。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### prop iterations

```cangjie
public mut prop iterations: Int32
```

**功能：** 迭代次数，需要为正整数。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** Int32

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

### prop password

```cangjie
public mut prop password: Array<UInt8>
```

**功能：** 用户输入的原始密码。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** Array\<UInt8>

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

### init(String, Array\<UInt8>, Array\<UInt8>, Int32, Int32)

```cangjie
public init(algName!: String, password!: Array<UInt8>, salt!: Array<UInt8>, iterations!: Int32, keySize!: Int32)
```

**功能：** 创建PBKDF2Spec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-| **命名参数。** 指明密钥派生函数的算法名。|
|password|Array\<UInt8>|是|-| **命名参数。** 用户输入的原始密码。|
|salt|Array\<UInt8>|是|-| **命名参数。** 盐值。|
|iterations|Int32|是|-| **命名参数。** 迭代次数，需要为正整数。|
|keySize|Int32|是|-| **命名参数。** 派生得到的密钥字节长度。|