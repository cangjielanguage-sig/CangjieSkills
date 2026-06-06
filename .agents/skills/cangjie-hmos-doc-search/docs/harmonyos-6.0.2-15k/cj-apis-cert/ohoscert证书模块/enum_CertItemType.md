## enum CertItemType

```cangjie
public enum CertItemType <: Equatable<CertItemType> & ToString {
    | CERT_ITEM_TYPE_TBS
    | CERT_ITEM_TYPE_PUBLIC_KEY
    | CERT_ITEM_TYPE_ISSUER_UNIQUE_ID
    | CERT_ITEM_TYPE_SUBJECT_UNIQUE_ID
    | CERT_ITEM_TYPE_EXTENSIONS
    | ...
}
```

**功能：** 表示获取证书字段。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- Equatable\<CertItemType>
- ToString

### CERT_ITEM_TYPE_EXTENSIONS

```cangjie
CERT_ITEM_TYPE_EXTENSIONS
```

**功能：** 表示获取证书的扩展域信息。

**起始版本：** 19

### CERT_ITEM_TYPE_ISSUER_UNIQUE_ID

```cangjie
CERT_ITEM_TYPE_ISSUER_UNIQUE_ID
```

**功能：** 表示获取证书的颁发者唯一编号。

**起始版本：** 19

### CERT_ITEM_TYPE_PUBLIC_KEY

```cangjie
CERT_ITEM_TYPE_PUBLIC_KEY
```

**功能：** 表示获取证书的公钥信息。

**起始版本：** 19

### CERT_ITEM_TYPE_SUBJECT_UNIQUE_ID

```cangjie
CERT_ITEM_TYPE_SUBJECT_UNIQUE_ID
```

**功能：** 表示获取证书的主体唯一编号。

**起始版本：** 19

### CERT_ITEM_TYPE_TBS

```cangjie
CERT_ITEM_TYPE_TBS
```

**功能：** 表示获取证书的待签名信息。

**起始版本：** 19

### func !=(CertItemType)

```cangjie
public operator func !=(other: CertItemType): Bool
```

**功能：** 对授权状态进行判不等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CertItemType](#enum-certitemtype)|是|获取证书字段。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果获取证书字段不同，返回true，否则返回false。|

### func ==(CertItemType)

```cangjie
public operator func ==(other: CertItemType): Bool
```

**功能：** 对获取证书字段进行判等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CertItemType](#enum-certitemtype)|是|获取证书字段。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果获取证书字段相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回获取证书字段的字符串表示。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|获取证书字段的字符串表示。|