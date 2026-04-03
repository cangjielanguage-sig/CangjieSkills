## class AuthParam

```cangjie
public class AuthParam {
    public AuthParam(
        public let challenge: Array<Byte>,
        public let authType: Array<UserAuthType>,
        public let authTrustLevel: AuthTrustLevel,
        public let reuseUnlockResult!: ?ReuseUnlockResult = Option.None
    )
}
```

**功能：** 用户认证相关参数。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

### let authTrustLevel

```cangjie
public let authTrustLevel: AuthTrustLevel
```

**功能：** 认证信任等级。

**类型：** [AuthTrustLevel](#enum-authtrustlevel)

**读写能力：** 只读

**起始版本：** 19

### let authType

```cangjie
public let authType: Array<UserAuthType>
```

**功能：** 认证类型列表，用来指定用户认证界面提供的认证方法。

**类型：** Array\<[UserAuthType](#enum-userauthtype)>

**读写能力：** 只读

**起始版本：** 19

### let challenge

```cangjie
public let challenge: Array<Byte>
```

**功能：** 挑战值，用来防重放攻击。最大长度为32字节，可传Array[]。

**类型：** Array\<Byte>

**读写能力：** 只读

**起始版本：** 19

### let reuseUnlockResult

```cangjie
public let reuseUnlockResult: ?ReuseUnlockResult = Option.None
```

**功能：** 表示可以复用设备解锁结果。

**类型：** ?[ReuseUnlockResult](#class-reuseunlockresult)

**读写能力：** 只读

**起始版本：** 19

### AuthParam(Array\<Byte>, Array\<UserAuthType>, AuthTrustLevel, ?ReuseUnlockResult)

```cangjie
public AuthParam(
    public let challenge: Array<Byte>,
    public let authType: Array<UserAuthType>,
    public let authTrustLevel: AuthTrustLevel,
    public let reuseUnlockResult!: ?ReuseUnlockResult = Option.None
)
```

**功能：** 创建[AuthParam](#class-authparam)实例。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|challenge|Array\<Byte>|是|-|挑战值，用来防重放攻击。最大长度为32字节，可传Array[]。|
|authType|Array\<[UserAuthType](#enum-userauthtype)>|是|-|认证类型列表，用来指定用户认证界面提供的认证方法。|
|authTrustLevel|[AuthTrustLevel](#enum-authtrustlevel)|是|-|认证信任等级。|
|reuseUnlockResult|?[ReuseUnlockResult](#class-reuseunlockresult)|否|Option.None| **命名参数。** 表示可以复用设备解锁结果。|