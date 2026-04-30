## enum DistributedAccountStatus

```cangjie
public enum DistributedAccountStatus {
    | NOT_LOGGED_IN
    | LOGGED_IN
    | ...
}
```

**功能：** 分布式账号状态。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

### LOGGED_IN

```cangjie
LOGGED_IN
```

**功能：** 已登录状态。

**起始版本：** 19

### NOT_LOGGED_IN

```cangjie
NOT_LOGGED_IN
```

**功能：** 未登录状态。

**起始版本：** 19

## enum OhosAccountEvent

```cangjie
public enum OhosAccountEvent {
    | LOGIN
    | LOGOUT
    | TOKEN_INVALID
    | LOGOFF
    | ...
}
```

**功能：** 分布式账号登录状态。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

### LOGIN

```cangjie
LOGIN
```

**功能：** 登录。

**起始版本：** 19

### LOGOFF

```cangjie
LOGOFF
```

**功能：** 登出。

**起始版本：** 19

### LOGOUT

```cangjie
LOGOUT
```

**功能：** 注销。

**起始版本：** 19

### TOKEN_INVALID

```cangjie
TOKEN_INVALID
```

**功能：** Token失效。

**起始版本：** 19