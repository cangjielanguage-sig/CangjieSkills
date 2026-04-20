## enum AuthTrustLevel

```cangjie
public enum AuthTrustLevel {
    | ATL1
    | ATL2
    | ATL3
    | ATL4
    | ...
}
```

**功能：** 表示认证结果的信任等级枚举。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

### ATL1

```cangjie
ATL1
```

**功能：** 认证结果的信任等级级别1，代表该认证方案能够识别用户个体，有一定的活体检测能力。常用的业务场景有业务风控、一般个人数据查询等。

**起始版本：** 19

### ATL2

```cangjie
ATL2
```

**功能：** 认证结果的信任等级级别2，代表该认证方案能够精确识别用户个体，有一定的活体检测能力。常用的业务场景有维持设备解锁状态，应用登录等。

**起始版本：** 19

### ATL3

```cangjie
ATL3
```

**功能：** 认证结果的信任等级级别3，代表该认证方案能够精确识别用户个体，有较强的活体检测能力。常用的业务场景有设备解锁等。

**起始版本：** 19

### ATL4

```cangjie
ATL4
```

**功能：** 认证结果的信任等级级别4，代表该认证方案能够高精度的识别用户个体，有很强的活体检测能力。常用的业务场景有小额支付等。

**起始版本：** 19

### func getValue()

```cangjie
public func getValue(): UInt32
```

**功能：** 获取信任等级对应的值。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回信任等级对应的整数值。|

## enum ReuseMode

```cangjie
public enum ReuseMode {
    | AUTH_TYPE_RELEVANT
    | AUTH_TYPE_IRRELEVANT
    | ...
}
```

**功能：** 表示复用设备解锁结果的模式。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

### AUTH_TYPE_IRRELEVANT

```cangjie
AUTH_TYPE_IRRELEVANT
```

**功能：** 与认证类型无关，只要解锁认证结果在有效时间内，就可以重复使用。

**起始版本：** 19

### AUTH_TYPE_RELEVANT

```cangjie
AUTH_TYPE_RELEVANT
```

**功能：** 与认证类型相关，只有当设备解锁结果在有效时间内，并且设备解锁的认证类型匹配上本次认证指定认证类型之一时，可以复用该结果。

**起始版本：** 19

### func getValue()

```cangjie
public func getValue(): UInt32
```

**功能：** 获取解锁结果是否复用对应的值。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回解锁结果是否复用对应的整数值。|

## enum UserAuthType

```cangjie
public enum UserAuthType {
    | PIN
    | FACE
    | FINGERPRINT
    | ...
}
```

**功能：** 表示身份认证的凭据类型枚举。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

### FACE

```cangjie
FACE
```

**功能：** 人脸认证。

**起始版本：** 19

### FINGERPRINT

```cangjie
FINGERPRINT
```

**功能：** 指纹认证。

**起始版本：** 19

### PIN

```cangjie
PIN
```

**功能：** 口令认证。

**起始版本：** 19

### func getValue()

```cangjie
public func getValue(): UInt32
```

**功能：** 获取凭据类型对应的值。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回凭据类型对应的整数值。|