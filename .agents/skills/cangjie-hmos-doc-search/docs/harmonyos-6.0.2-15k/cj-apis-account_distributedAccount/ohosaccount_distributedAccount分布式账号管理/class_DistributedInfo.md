## class DistributedInfo

```cangjie
public class DistributedInfo {
    public let name: String
    public let id: String
    public let event: OhosAccountEvent
    public let nickname: String
    public let avatar: String
    public let status: DistributedAccountStatus
    public let scalableData: String
    public init(name: String, id: String, event: OhosAccountEvent, nickname!: String = "", avatar!: String = "",
        status!: DistributedAccountStatus = NOT_LOGGED_IN, scalableData!: String = "")
}
```

**功能：** 提供操作系统账号的分布式信息。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

### let name

```cangjie
public let name: String
```

**功能：** 分布式账号名称，非空字符串。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let id

```cangjie
public let id: String
```

**功能：** 分布式账号UID，非空字符串。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let event

```cangjie
public let event: OhosAccountEvent
```

**功能：** 分布式账号登录状态，包括登录、登出、Token失效和注销，分别对应以下字符串：

- Ohos.account.event.LOGIN
- Ohos.account.event.LOGOUT
- Ohos.account.event.TOKEN_INVALID
- Ohos.account.event.LOGOFF

**类型：** [OhosAccountEvent](#enum-ohosaccountevent)

**读写能力：** 只读

**起始版本：** 19

### let nickname

```cangjie
public let nickname: String
```

**功能：** 分布式账号的昵称，默认为空。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let avatar

```cangjie
public let avatar: String
```

**功能：** 分布式账号的头像，默认为空。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let status

```cangjie
public let status: DistributedAccountStatus
```

**功能：** 分布式账号的状态，枚举类型，默认为未登录状态。

**类型：** [DistributedAccountStatus](#enum-distributedaccountstatus)

**读写能力：** 只读

**起始版本：** 19

### let scalableData

```cangjie
public let scalableData: String
```

**功能：** 分布式账号扩展信息，根据业务所需，以k-v形式传递定制化信息，默认为空字符串。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### init(String, String, OhosAccountEvent, String, String, DistributedAccountStatus, String)

```cangjie
public init(name: String, id: String, event: OhosAccountEvent, nickname!: String = "", avatar!: String = "", status!: DistributedAccountStatus = NOT_LOGGED_IN, scalableData!: String = "")
```

**功能：** 创建DistributedInfo实例。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|分布式账号名称，非空字符串。|
|id|String|是|-|分布式账号UID，非空字符串。|
|event|[OhosAccountEvent](#enum-ohosaccountevent)|是|-|分布式账号登录状态，包括登录、登出、Token失效和注销，分别对应以下字符串：<br/>-&nbsp;Ohos.account.event.LOGIN<br/>-&nbsp;Ohos.account.event.LOGOUT<br/>-&nbsp;Ohos.account.event.TOKEN_INVALID<br/>-&nbsp;Ohos.account.event.LOGOFF|
|nickname|String|否|""| **命名参数。** 分布式账号的昵称，默认为空。|
|avatar|String|否|""| **命名参数。** 分布式账号的头像，默认为空。|
|status|[DistributedAccountStatus](#enum-distributedaccountstatus)|否|NOT_LOGGED_IN| **命名参数。** 分布式账号的状态，枚举类型，默认为未登录状态。|
|scalableData|String|否|""| **命名参数。** 分布式账号扩展信息，根据业务所需，以k-v形式传递定制化信息，默认为空字符串。|