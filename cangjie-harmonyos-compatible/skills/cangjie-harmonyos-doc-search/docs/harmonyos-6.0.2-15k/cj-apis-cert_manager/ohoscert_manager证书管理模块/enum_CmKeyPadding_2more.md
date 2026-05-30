## enum CmKeyPadding

```cangjie
public enum CmKeyPadding <: Equatable<CmKeyPadding> & ToString {
    | CM_PADDING_NONE
    | CM_PADDING_PSS
    | CM_PADDING_PKCS1_V1_5
    | ...
}
```

**功能：** 表示签名、验签使用的填充方式。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**父类型：**

- Equatable\<CmKeyPadding>
- ToString

### CM_PADDING_NONE

```cangjie
CM_PADDING_NONE
```

**功能：** 无填充。

**起始版本：** 19

### CM_PADDING_PKCS1_V1_5

```cangjie
CM_PADDING_PKCS1_V1_5
```

**功能：** PSS方式填充。

**起始版本：** 19

### CM_PADDING_PSS

```cangjie
CM_PADDING_PSS
```

**功能：** PKCS1_V1_5方式填充。

**起始版本：** 19

### func !=(CmKeyPadding)

```cangjie
public operator func !=(other: CmKeyPadding): Bool
```

**功能：** 对签名、验签使用的填充方式进行判不等。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CmKeyPadding](#enum-cmkeypadding)|是|签名、验签使用的填充方式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果签名、验签使用的填充方式不同，返回true，否则返回false。|

### func ==(CmKeyPadding)

```cangjie
public operator func ==(other: CmKeyPadding): Bool
```

**功能：** 对签名、验签使用的填充方式进行判等。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CmKeyPadding](#enum-cmkeypadding)|是|签名、验签使用的填充方式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果签名、验签使用的填充方式相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 当前实例转换为字符串。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前实例的字符串。|

## enum CmKeyPurpose

```cangjie
public enum CmKeyPurpose <: Equatable<CmKeyPurpose> & ToString {
    | CM_KEY_PURPOSE_SIGN
    | CM_KEY_PURPOSE_VERIFY
    | ...
}
```

**功能：** 表示密钥使用目的的枚举，用于签名、验签。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**父类型：**

- Equatable\<CmKeyPurpose>
- ToString

### CM_KEY_PURPOSE_SIGN

```cangjie
CM_KEY_PURPOSE_SIGN
```

**功能：** 签名。

**起始版本：** 19

### CM_KEY_PURPOSE_VERIFY

```cangjie
CM_KEY_PURPOSE_VERIFY
```

**功能：** 验签。

**起始版本：** 19

### func !=(CmKeyPurpose)

```cangjie
public operator func !=(other: CmKeyPurpose): Bool
```

**功能：** 对密钥使用目的进行判不等。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CmKeyPurpose](#enum-cmkeypurpose)|是|密钥使用目的。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果密钥使用目的不同，返回true，否则返回false。|

### func ==(CmKeyPurpose)

```cangjie
public operator func ==(other: CmKeyPurpose): Bool
```

**功能：** 对密钥使用目的进行判等。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CmKeyPurpose](#enum-cmkeypurpose)|是|密钥使用目的。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果密钥使用目的相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 当前实例转换为字符串。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前实例的字符串。|