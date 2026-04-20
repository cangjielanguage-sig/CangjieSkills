## enum OsAccountType

```cangjie
public enum OsAccountType {
    | ADMIN
    | NORMAL
    | GUEST
    | UNKNOWN
    | ...
}
```

**功能：** 表示系统账号类型。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

### ADMIN

```cangjie
ADMIN
```

**功能：** 管理员账号。

**起始版本：** 19

### GUEST

```cangjie
GUEST
```

**功能：** 访客账号。

**起始版本：** 19

### NORMAL

```cangjie
NORMAL
```

**功能：** 普通账号。

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知系统账号类型。

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|