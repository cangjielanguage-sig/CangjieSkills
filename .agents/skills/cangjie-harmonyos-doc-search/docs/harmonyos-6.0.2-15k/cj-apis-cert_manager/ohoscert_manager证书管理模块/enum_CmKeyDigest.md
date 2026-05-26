## enum CmKeyDigest

```cangjie
public enum CmKeyDigest <: Equatable<CmKeyDigest> & ToString {
    | CM_DIGEST_NONE
    | CM_DIGEST_MD5
    | CM_DIGEST_SHA1
    | CM_DIGEST_SHA224
    | CM_DIGEST_SHA256
    | CM_DIGEST_SHA384
    | CM_DIGEST_SHA512
    | ...
}
```

**功能：** 表示签名、验签使用的摘要算法。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**父类型：**

- Equatable\<CmKeyDigest>
- ToString

### CM_DIGEST_MD5

```cangjie
CM_DIGEST_MD5
```

**功能：** MD5摘要算法。

**起始版本：** 19

### CM_DIGEST_NONE

```cangjie
CM_DIGEST_NONE
```

**功能：** 不需要摘要算法，选用此项时，需要业务传入已经计算过摘要的数据进行签名、验签。

**起始版本：** 19

### CM_DIGEST_SHA1

```cangjie
CM_DIGEST_SHA1
```

**功能：** SHA1摘要算法。

**起始版本：** 19

### CM_DIGEST_SHA224

```cangjie
CM_DIGEST_SHA224
```

**功能：** SHA224摘要算法。

**起始版本：** 19

### CM_DIGEST_SHA256

```cangjie
CM_DIGEST_SHA256
```

**功能：** SHA256摘要算法。

**起始版本：** 19

### CM_DIGEST_SHA384

```cangjie
CM_DIGEST_SHA384
```

**功能：** SHA384摘要算法。

**起始版本：** 19

### CM_DIGEST_SHA512

```cangjie
CM_DIGEST_SHA512
```

**功能：** SHA512摘要算法。

**起始版本：** 19

### func !=(CmKeyDigest)

```cangjie
public operator func !=(other: CmKeyDigest): Bool
```

**功能：** 对签名、验签使用的摘要算法进行判不等。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CmKeyDigest](#enum-cmkeydigest)|是|签名、验签使用的摘要算法。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果签名、验签使用的摘要算法不同，返回true，否则返回false。|

### func ==(CmKeyDigest)

```cangjie
public operator func ==(other: CmKeyDigest): Bool
```

**功能：** 对签名、验签使用的摘要算法进行判等。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CmKeyDigest](#enum-cmkeydigest)|是|签名、验签使用的摘要算法。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果签名、验签使用的摘要算法相同，返回true，否则返回false。|

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