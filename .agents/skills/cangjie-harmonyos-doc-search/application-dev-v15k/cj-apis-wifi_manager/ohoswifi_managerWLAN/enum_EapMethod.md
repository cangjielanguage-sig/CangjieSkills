## enum EapMethod

```cangjie
public enum EapMethod <: Equatable<EapMethod> & ToString {
    | EAP_NONE
    | EAP_PEAP
    | EAP_TLS
    | EAP_TTLS
    | EAP_PWD
    | EAP_SIM
    | EAP_AKA
    | EAP_AKA_PRIME
    | EAP_UNAUTH_TLS
    | ...
}
```

**功能：** 表示EAP认证方式。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- Equatable\<[EapMethod](#enum-eapmethod)>
- ToString

### EAP_AKA

```cangjie
EAP_AKA
```

**功能：** AKA类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### EAP_AKA_PRIME

```cangjie
EAP_AKA_PRIME
```

**功能：** AKA Prime类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### EAP_NONE

```cangjie
EAP_NONE
```

**功能：** 不指定。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### EAP_PEAP

```cangjie
EAP_PEAP
```

**功能：** PEAP类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### EAP_PWD

```cangjie
EAP_PWD
```

**功能：** PWD类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### EAP_SIM

```cangjie
EAP_SIM
```

**功能：** SIM类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### EAP_TLS

```cangjie
EAP_TLS
```

**功能：** TLS类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### EAP_TTLS

```cangjie
EAP_TTLS
```

**功能：** TTLS类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### EAP_UNAUTH_TLS

```cangjie
EAP_UNAUTH_TLS
```

**功能：** UNAUTH TLS类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|

### func ==(EapMethod)

```cangjie
public operator func ==(that: EapMethod): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|that|[EapMethod](#enum-eapmethod)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|