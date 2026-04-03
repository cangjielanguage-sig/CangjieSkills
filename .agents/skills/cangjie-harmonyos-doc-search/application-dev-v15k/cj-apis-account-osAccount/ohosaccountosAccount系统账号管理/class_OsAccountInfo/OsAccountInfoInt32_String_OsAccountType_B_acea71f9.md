### OsAccountInfo(Int32, String, OsAccountType, Bool, Bool, Int64, Int64, Bool, Bool, Bool, Array\<String>, String, Int64, DistributedInfo, DomainAccountInfo)

```cangjie
public OsAccountInfo(
    public let localId: Int32,
    public let localName: String,
    public let `type`: OsAccountType,
    public let isVerified: Bool,
    public let isUnlocked: Bool,
    public let createTime: Int64,
    public let serialNumber: Int64,
    public let isActived: Bool,
    public let isActivated: Bool,
    public let isCreateCompleted: Bool,
    public var constraints!: Array<String> = Array<String>(),
    public var photo!: String = "",
    public var lastLoginTime!: Int64 = 0,
    public var distributedInfo!: DistributedInfo,
    public var domainInfo!: DomainAccountInfo
)
```

**功能：** 构造OsAccountInfo对象。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|localId|Int32|是|-|系统账号ID。|
|localName|String|是|-|系统账号名称。|
|\`type`|[OsAccountType](#enum-osaccounttype)|是|-|系统账号类型。|
|isVerified|Bool|是|-|账号是否验证。|
|isUnlocked|Bool|是|-|账号是否已解锁（EL2级别目录是否解密）。|
|createTime|Int64|是|-|账号是否已解锁（EL2级别目录是否解密）。|
|serialNumber|Int64|是|-|系统账号SN码。|
|isActived|Bool|是|-|系统账号激活状态。|
|isActivated|Bool|是|-|系统账号激是否激活。|
|isCreateCompleted|Bool|是|-|系统账号创建是否完整。|
|constraints|Array\<String>|否|Array\<String>()| **命名参数。** 系统账号约束，默认为空。详见[系统账号约束列表](#系统账号约束列表)。|
|photo|String|否|""| **命名参数。** 系统账号头像，默认为空。|
|lastLoginTime|Int64|否|0| **命名参数。** 系统账号最后一次登录时间，默认为空。|
|distributedInfo|[DistributedInfo](cj-apis-account_distributedAccount.md#class-distributedinfo)|否|None| **命名参数。** 分布式账号信息，默认为空。|
|domainInfo|[DomainAccountInfo](#class-domainaccountinfo)|否|None| **命名参数。** 域账号信息，默认为空。|