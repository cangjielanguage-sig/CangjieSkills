## class CreateAccountOptions

```cangjie
public class CreateAccountOptions {
    public CreateAccountOptions (
        public var customData!: ?HashMap<String, String> = None
    )
}
```

**功能：** 表示创建账号的选项。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

### var customData

```cangjie
public var customData: ?HashMap<String, String> = None
```

**功能：** 自定义数据，默认为空。

**类型：** ?HashMap\<String, String>

**读写能力：** 可读写

**起始版本：** 19

### CreateAccountOptions(?HashMap\<String, String>)

```cangjie
public CreateAccountOptions (
    public var customData!: ?HashMap<String, String> = None
)
```

**功能：** 构造CreateAccountOptions对象。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|customData|?HashMap\<String, String>|否|None| **命名参数。** 自定义数据，默认为空。|

## class SelectAccountsOptions

```cangjie
public class SelectAccountsOptions {
    public SelectAccountsOptions (
        public var allowedAccounts!: ?Array<AppAccountInfo>= None,
        public var allowedOwners!: ?Array<String>= None,
        public var requiredLabels!: ?Array<String>= None
    )
}
```

**功能：** 表示用于选择账号的选项。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

### var allowedAccounts

```cangjie
public var allowedAccounts: ?Array<AppAccountInfo> = None
```

**功能：** 允许的账号数组，默认为空。

**类型：** ?Array\<[AppAccountInfo](#class-appaccountinfo)>

**读写能力：** 可读写

**起始版本：** 19

### var allowedOwners

```cangjie
public var allowedOwners: ?Array<String> = None
```

**功能：** 允许的账号所有者数组，默认为空。

**类型：** ?Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var requiredLabels

```cangjie
public var requiredLabels: ?Array<String> = None
```

**功能：** 认证器的标签标识，默认为空。

**类型：** ?Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### SelectAccountsOptions(?Array\<AppAccountInfo>, ?Array\<String>, ?Array\<String>)

```cangjie
public SelectAccountsOptions (
    public var  allowedAccounts!: ?Array<AppAccountInfo> = None,
    public var allowedOwners!: ?Array<String> = None,
    public var requiredLabels!: ?Array<String> = None
)
```

**功能：** 构建SelectAccountsOptions实例。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|allowedAccounts|?Array\<[AppAccountInfo](#class-appaccountinfo)>|否|None| **命名参数。** 允许的账号数组，默认为空。|
|allowedOwners|?Array\<String>|否|None| **命名参数。** 允许的账号所有者数组，默认为空。|
|requiredLabels|?Array\<String>|否|None| **命名参数。** 认证器的标签标识，默认为空。|