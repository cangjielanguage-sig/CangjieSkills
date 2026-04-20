## enum CipherSpecItem

```cangjie
public enum CipherSpecItem <: Equatable<CipherSpecItem> & ToString {
    | OaepMdNameStr
    | OaepMgfNameStr
    | OaepMgf1MdStr
    | OaepMgf1PsrcUint8Arr
    | ...
}
```

**功能：** 表示加解密参数的枚举。

当前只支持RSA算法和SM2算法。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**父类型：**

- Equatable\<CipherSpecItem>
- ToString

### OaepMdNameStr

```cangjie
OaepMdNameStr
```

**功能：** 表示RSA算法中，使用PKCS1_OAEP模式时，消息摘要功能的算法名。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### OaepMgfNameStr

```cangjie
OaepMgfNameStr
```

**功能：** 表示RSA算法中，使用PKCS1_OAEP模式时，掩码生成算法（目前仅支持MGF1）。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### OaepMgf1MdStr

```cangjie
OaepMgf1MdStr
```

**功能：** 表示RSA算法中，使用PKCS1_OAEP模式时，MGF1掩码生成功能的消息摘要算法。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### OaepMgf1PsrcUint8Arr

```cangjie
OaepMgf1PsrcUint8Arr
```

**功能：** 表示RSA算法中，使用PKCS1_OAEP模式时，pSource的字节流。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### func !=(CipherSpecItem)

```cangjie
public operator func !=(other: CipherSpecItem): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

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

**起始版本：** 22

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|