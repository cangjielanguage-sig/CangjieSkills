## class OsAccountInfo

```cangjie
public class OsAccountInfo {
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
        public var constraints!: Array<String>= Array<String>(),
        public var photo!: String = "",
        public var lastLoginTime!: Int64 = 0,
        public var distributedInfo!: DistributedInfo,
        public var domainInfo!: DomainAccountInfo
    )
}
```

**功能：** 表示系统账号信息。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

### var constraints

```cangjie
public var constraints: Array<String> = Array<String>()
```

**功能：** 系统账号约束，默认为空。详见[系统账号约束列表](#系统账号约束列表)。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var distributedInfo

```cangjie
public var distributedInfo: DistributedInfo
```

**功能：** 分布式账号信息，默认为空。

**类型：** [DistributedInfo](cj-apis-account_distributedAccount.md#class-distributedinfo)

**读写能力：** 可读写

**起始版本：** 19

### var domainInfo

```cangjie
public var domainInfo: DomainAccountInfo
```

**功能：** 域账号信息，默认为空。

**类型：** [DomainAccountInfo](#class-domainaccountinfo)

**读写能力：** 可读写

**起始版本：** 19

### var lastLoginTime

```cangjie
public var lastLoginTime: Int64 = 0
```

**功能：** 系统账号最后一次登录时间，默认为空。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var photo

```cangjie
public var photo: String = ""
```

**功能：** 系统账号头像，默认为空。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### let \`type`

```cangjie
public let `type`: OsAccountType
```

**功能：** 系统账号类型。

**类型：** [OsAccountType](#enum-osaccounttype)

**读写能力：** 只读

**起始版本：** 19

### let createTime

```cangjie
public let createTime: Int64
```

**功能：** 系统账号创建时间。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19

### let isActivated

```cangjie
public let isActivated: Bool
```

**功能：** 系统账号激是否激活。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isActived

```cangjie
public let isActived: Bool
```

**功能：** 系统账号激活状态。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isCreateCompleted

```cangjie
public let isCreateCompleted: Bool
```

**功能：** 系统账号创建是否完整。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isUnlocked

```cangjie
public let isUnlocked: Bool
```

**功能：** 账号是否已解锁（EL2级别目录是否解密）。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isVerified

```cangjie
public let isVerified: Bool
```

**功能：** 账号是否验证。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let localId

```cangjie
public let localId: Int32
```

**功能：** 系统账号ID。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let localName

```cangjie
public let localName: String
```

**功能：** 系统账号名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let serialNumber

```cangjie
public let serialNumber: Int64
```

**功能：** 系统账号SN码。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19