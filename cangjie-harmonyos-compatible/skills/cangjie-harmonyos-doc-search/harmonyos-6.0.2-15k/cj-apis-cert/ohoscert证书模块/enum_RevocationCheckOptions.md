## enum RevocationCheckOptions

```cangjie
public enum RevocationCheckOptions <: Equatable<RevocationCheckOptions> & ToString {
    | REVOCATION_CHECK_OPTION_PREFER_OCSP
    | REVOCATION_CHECK_OPTION_ACCESS_NETWORK
    | REVOCATION_CHECK_OPTION_FALLBACK_NO_PREFER
    | REVOCATION_CHECK_OPTION_FALLBACK_LOCAL
    | ...
}
```

**功能：** 表示证书链在线校验证书吊销状态选项。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- Equatable\<RevocationCheckOptions>
- ToString

### REVOCATION_CHECK_OPTION_ACCESS_NETWORK

```cangjie
REVOCATION_CHECK_OPTION_ACCESS_NETWORK
```

**功能：** 支持通过访问网络获取CRL或OCSP响应进行吊销状态的校验，默认为关闭。

**起始版本：** 19

### REVOCATION_CHECK_OPTION_FALLBACK_LOCAL

```cangjie
REVOCATION_CHECK_OPTION_FALLBACK_LOCAL
```

**功能：** 当ACCESS_NETWORK选项打开时有效，如果在线获取CRL和OCSP响应都由于网络的原因导致无法校验证书状态，则采用本地设置的CRL和OCSP响应进行校验。

**起始版本：** 19

### REVOCATION_CHECK_OPTION_FALLBACK_NO_PREFER

```cangjie
REVOCATION_CHECK_OPTION_FALLBACK_NO_PREFER
```

**功能：** 当ACCESS_NETWORK选项打开时有效，如果优选的校验方法由于网络原因导致无法校验证书状态，则采用备选的方案进行校验。

**起始版本：** 19

### REVOCATION_CHECK_OPTION_PREFER_OCSP

```cangjie
REVOCATION_CHECK_OPTION_PREFER_OCSP
```

**功能：** 优先采用OCSP进行校验，默认采用CRL校验。

**起始版本：** 19

### func !=(RevocationCheckOptions)

```cangjie
public operator func !=(other: RevocationCheckOptions): Bool
```

**功能：** 对证书链在线校验证书吊销状态选项进行判不等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[RevocationCheckOptions](#enum-revocationcheckoptions)|是|证书链在线校验证书吊销状态选项。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果证书链在线校验证书吊销状态选项不同，返回true，否则返回false。|

### func ==(RevocationCheckOptions)

```cangjie
public operator func ==(other: RevocationCheckOptions): Bool
```

**功能：** 对证书链在线校验证书吊销状态选项进行判等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[RevocationCheckOptions](#enum-revocationcheckoptions)|是|证书链在线校验证书吊销状态选项。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果证书链在线校验证书吊销状态选项相同，返回true，否则返回false。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 当前枚举所表示的值。

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

**功能：** 返回证书链在线校验证书吊销状态选项的字符串表示。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|证书链在线校验证书吊销状态选项的字符串表示。|