## enum SignSpecItem

```cangjie
public enum SignSpecItem <: Equatable<SignSpecItem> & ToString {
    | PSS_MD_NAME_STR
    | PSS_MGF_NAME_STR
    | PSS_MGF1_MD_STR
    | PSS_SALT_LEN_NUM
    | PSS_TRAILER_FIELD_NUM
    | SM2_USER_ID_UINT8ARR
    | ...
}
```

**功能：** 表示签名验签参数的枚举，这些签名验签参数支持通过setSignSpec、setVerifySpec接口设置/通过getSignSpec、getVerifySpec接口获取。

当前只支持RSA算法，SM2算法。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- Equatable\<SignSpecItem>
- ToString

### PSS_MD_NAME_STR

```cangjie
PSS_MD_NAME_STR
```

**功能：** 表示RSA算法中，使用PSS模式时，消息摘要功能的算法名。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### PSS_MGF1_MD_STR

```cangjie
PSS_MGF1_MD_STR
```

**功能：** 表示RSA算法中，使用PSS模式时，MGF1掩码生成功能的消息摘要参数。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### PSS_MGF_NAME_STR

```cangjie
PSS_MGF_NAME_STR
```

**功能：** 表示RSA算法中，使用PSS模式时，掩码生成算法（目前仅支持MGF1）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### PSS_SALT_LEN_NUM

```cangjie
PSS_SALT_LEN_NUM
```

**功能：** 表示RSA算法中，使用PSS模式时，盐值的长度，长度以字节为单位。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### PSS_TRAILER_FIELD_NUM

```cangjie
PSS_TRAILER_FIELD_NUM
```

**功能：** 表示RSA算法中，使用PSS模式时，用于编码操作的整数。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### SM2_USER_ID_UINT8ARR

```cangjie
SM2_USER_ID_UINT8ARR
```

**功能：** 表示SM2算法中，用户身份标识字段。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### func !=(SignSpecItem)

```cangjie
public operator func !=(other: SignSpecItem): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SignSpecItem](#enum-signspecitem)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(SignSpecItem)

```cangjie
public operator func ==(other: SignSpecItem): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SignSpecItem](#enum-signspecitem)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|