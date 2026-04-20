## enum ValidationPolicyType

```cangjie
public enum ValidationPolicyType <: Equatable<ValidationPolicyType> & ToString {
    | VALIDATION_POLICY_TYPE_X509
    | VALIDATION_POLICY_TYPE_SSL
    | ...
}
```

**功能：** 表示证书链在线校验策略。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- Equatable\<ValidationPolicyType>
- ToString

### VALIDATION_POLICY_TYPE_SSL

```cangjie
VALIDATION_POLICY_TYPE_SSL
```

**功能：** 需要校验证书中的sslHostname或dNSName。

**起始版本：** 19

### VALIDATION_POLICY_TYPE_X509

```cangjie
VALIDATION_POLICY_TYPE_X509
```

**功能：** 默认值，不需要校验证书中的sslHostname或dNSName。

**起始版本：** 19

### func !=(ValidationPolicyType)

```cangjie
public operator func !=(other: ValidationPolicyType): Bool
```

**功能：** 对证书链在线校验策略进行判不等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ValidationPolicyType](#enum-validationpolicytype)|是|证书链在线校验策略。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果证书链在线校验策略不同，返回true，否则返回false。|

### func ==(ValidationPolicyType)

```cangjie
public operator func ==(other: ValidationPolicyType): Bool
```

**功能：** 对证书链在线校验策略进行判等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ValidationPolicyType](#enum-validationpolicytype)|是|证书链在线校验策略。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果证书链在线校验策略相同，返回true，否则返回false。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取当前枚举的所表示的值。

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

**功能：** 返回证书链在线校验策略的字符串表示。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|证书链在线校验策略的字符串表示。|