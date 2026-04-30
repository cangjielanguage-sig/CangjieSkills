## class AuthTokenInfo

```cangjie
public class AuthTokenInfo {
    public AuthTokenInfo (
        public var authType: String,
        public var token: String,
        public var account!: ?AppAccountInfo = None
    )
}
```

**功能：** 表示Auth令牌信息。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

### var authType

```cangjie
public var authType: String
```

**功能：** 令牌的鉴权类型。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var token

```cangjie
public var token: String
```

**功能：** 令牌的取值。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var account

```cangjie
public var account: ?AppAccountInfo = None
```

**功能：** 令牌所属的账号信息，默认为空。

**类型：** ?[AppAccountInfo](#class-appaccountinfo)

**读写能力：** 可读写

**起始版本：** 19

### AuthTokenInfo(String, String, ?AppAccountInfo)

```cangjie
public AuthTokenInfo (
    public var authType: String,
    public var token: String,
    public var account!: ?AppAccountInfo = None
)
```

**功能：** 构建AuthTokenInfo实例。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|authType|String|是|-|令牌的鉴权类型。|
|token|String|是|-|令牌的取值。|
|account|?[AppAccountInfo](#class-appaccountinfo)|否|None| **命名参数。** 令牌所属的账号信息，默认为空。|

## class AuthenticatorInfo

```cangjie
public class AuthenticatorInfo{
    public AuthenticatorInfo(
        public var owner: String,
        public var iconId: Int32,
        public var labelId: Int32
    )
}
```

**功能：** 表示OAuth认证器信息。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

### var owner

```cangjie
public var owner: String
```

**功能：** 认证器的所有者的包名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var iconId

```cangjie
public var iconId: Int32
```

**功能：** 认证器的图标标识。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var labelId

```cangjie
public var labelId: Int32
```

**功能：** 认证器的标签标识。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### AuthenticatorInfo(String, Int32, Int32)

```cangjie
public AuthenticatorInfo (
    public var owner: String,
    public var iconId: Int32,
    public var labelId: Int32
)
```

**功能：** 构建AuthenticatorInfo实例。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|owner|String|是|-|认证器的所有者的包名。|
|iconId|Int32|是|-|认证器的图标标识。|
|labelId|Int32|是|-|认证器的标签标识。|