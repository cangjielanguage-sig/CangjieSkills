## enum KeyUsageType

```cangjie
public enum KeyUsageType <: Equatable<KeyUsageType> & ToString {
    | KEYUSAGE_DIGITAL_SIGNATURE
    | KEYUSAGE_NON_REPUDIATION
    | KEYUSAGE_KEY_ENCIPHERMENT
    | KEYUSAGE_DATA_ENCIPHERMENT
    | KEYUSAGE_KEY_AGREEMENT
    | KEYUSAGE_KEY_CERT_SIGN
    | KEYUSAGE_CRL_SIGN
    | KEYUSAGE_ENCIPHER_ONLY
    | KEYUSAGE_DECIPHER_ONLY
    | ...
}
```

**功能：** 表示证书中密钥用途。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- Equatable\<KeyUsageType>
- ToString

### KEYUSAGE_CRL_SIGN

```cangjie
KEYUSAGE_CRL_SIGN
```

**功能：** 证书持有者可以使用证书中包含的私钥对证书吊销列表（CRL）进行签名。

**起始版本：** 19

### KEYUSAGE_DATA_ENCIPHERMENT

```cangjie
KEYUSAGE_DATA_ENCIPHERMENT
```

**功能：** 证书持有者可以使用证书中包含的公钥进行数据加密操作。

**起始版本：** 19

### KEYUSAGE_DECIPHER_ONLY

```cangjie
KEYUSAGE_DECIPHER_ONLY
```

**功能：** 证书持有者只能进行解密操作，不能进行加密操作。

**起始版本：** 19

### KEYUSAGE_DIGITAL_SIGNATURE

```cangjie
KEYUSAGE_DIGITAL_SIGNATURE
```

**功能：** 证书持有者可以用证书中包含的私钥进行数字签名操作。

**起始版本：** 19

### KEYUSAGE_ENCIPHER_ONLY

```cangjie
KEYUSAGE_ENCIPHER_ONLY
```

**功能：** 证书持有者只能进行加密操作，不能进行解密操作。

**起始版本：** 19

### KEYUSAGE_KEY_AGREEMENT

```cangjie
KEYUSAGE_KEY_AGREEMENT
```

**功能：** 证书持有者可以使用证书中包含的私钥进行密钥协商操作。

**起始版本：** 19

### KEYUSAGE_KEY_CERT_SIGN

```cangjie
KEYUSAGE_KEY_CERT_SIGN
```

**功能：** 证书持有者可以使用证书中包含的私钥对其他证书进行签名。

**起始版本：** 19

### KEYUSAGE_KEY_ENCIPHERMENT

```cangjie
KEYUSAGE_KEY_ENCIPHERMENT
```

**功能：** 证书持有者可以使用证书中包含的公钥进行密钥加密操作。

**起始版本：** 19

### KEYUSAGE_NON_REPUDIATION

```cangjie
KEYUSAGE_NON_REPUDIATION
```

**功能：** 证书持有者不可否认使用证书中包含的私钥进行的数字签名操作。

**起始版本：** 19

### func !=(KeyUsageType)

```cangjie
public operator func !=(other: KeyUsageType): Bool
```

**功能：** 对证书中密钥用途进行判不等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[KeyUsageType](#enum-keyusagetype)|是|证书中密钥用途。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果证书中密钥用途不同，返回true，否则返回false。|

### func ==(KeyUsageType)

```cangjie
public operator func ==(other: KeyUsageType): Bool
```

**功能：** 对证书中密钥用途进行判等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[KeyUsageType](#enum-keyusagetype)|是|证书中密钥用途。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果证书中密钥用途相同，返回true，否则返回false。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取当前枚举的所表示的值。用于表示处理Want的方式。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|当前枚举所表示的值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回证书中密钥用途的字符串表示。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|证书中密钥用途的字符串表示。|