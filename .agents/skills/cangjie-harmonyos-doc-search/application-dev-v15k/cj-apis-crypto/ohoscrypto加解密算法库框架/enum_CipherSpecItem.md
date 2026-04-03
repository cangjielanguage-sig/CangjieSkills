## enum CipherSpecItem

```cangjie
public enum CipherSpecItem <: Equatable<CipherSpecItem> & ToString {
    | OAEP_MD_NAME_STR
    | OAEP_MGF_NAME_STR
    | OAEP_MGF1_MD_STR
    | OAEP_MGF1_PSRC_UINT8ARR
    | SM2_MD_NAME_STR
    | ...
}
```

**功能：** 表示加解密参数的枚举，这些加解密参数支持通过setCipherSpec接口设置/通过getCipherSpec接口获取。

当前只支持RSA算法和SM2算法。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**父类型：**

- Equatable\<CipherSpecItem>
- ToString

### OAEP_MD_NAME_STR

```cangjie
OAEP_MD_NAME_STR
```

**功能：** 表示RSA算法中，使用PKCS1_OAEP模式时，消息摘要功能的算法名。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### OAEP_MGF1_MD_STR

```cangjie
OAEP_MGF1_MD_STR
```

**功能：** 表示RSA算法中，使用PKCS1_OAEP模式时，MGF1掩码生成功能的消息摘要算法。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### OAEP_MGF1_PSRC_UINT8ARR

```cangjie
OAEP_MGF1_PSRC_UINT8ARR
```

**功能：** 表示RSA算法中，使用PKCS1_OAEP模式时，pSource的字节流。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### OAEP_MGF_NAME_STR

```cangjie
OAEP_MGF_NAME_STR
```

**功能：** 表示RSA算法中，使用PKCS1_OAEP模式时，掩码生成算法（目前仅支持MGF1）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### SM2_MD_NAME_STR

```cangjie
SM2_MD_NAME_STR
```

**功能：** 表示SM2算法中，使用的摘要算法名。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### func !=(CipherSpecItem)

```cangjie
public operator func !=(other: CipherSpecItem): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CipherSpecItem](#enum-cipherspecitem)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CipherSpecItem)

```cangjie
public operator func ==(other: CipherSpecItem): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CipherSpecItem](#enum-cipherspecitem)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|