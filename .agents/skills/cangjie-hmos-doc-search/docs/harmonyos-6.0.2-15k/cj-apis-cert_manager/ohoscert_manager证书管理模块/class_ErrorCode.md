## class ErrorCode

```cangjie
public class ErrorCode {
    public static const HAS_NO_PERMISSION: Int32 = 201
    public static const PARAM_ERROR: Int32 = 401
    public static const INNER_FAILURE: Int32 = 17500001
    public static const NOT_FOUND: Int32 = 17500002
    public static const INVALID_CERT_FORMAT: Int32 = 17500003
    public static const MAX_CERT_COUNT_REACHED: Int32 = 17500004
    public static const NO_AUTHORIZATION: Int32 = 17500005
    public static const NOT_SYSTEM_APP: Int32 = 202
    public static const ALIAS_LENGTH_REACHED_LIMIT: Int32 = 17500006
    public static const DEVICE_ENTER_ADVSECMODE: Int32 = 17500007
    public static const PASSWORD_IS_ERROR: Int32 = 17500008
}
```

**功能：** 表示调用证书管理相关API的错误码。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

### static const ALIAS_LENGTH_REACHED_LIMIT

```cangjie
public static const ALIAS_LENGTH_REACHED_LIMIT: Int32 = 17500006
```

**功能：** 表示输入的别名超过长度限制。

**类型：** Int32

**起始版本：** 19

### static const DEVICE_ENTER_ADVSECMODE

```cangjie
public static const DEVICE_ENTER_ADVSECMODE: Int32 = 17500007
```

**功能：** 表示设备进入高级安全模式。

**类型：** Int32

**起始版本：** 19

### static const HAS_NO_PERMISSION

```cangjie
public static const HAS_NO_PERMISSION: Int32 = 201
```

**功能：** 表示应用程序无权限调用接口。

**类型：** Int32

**起始版本：** 19

### static const INNER_FAILURE

```cangjie
public static const INNER_FAILURE: Int32 = 17500001
```

**功能：** 表示调用接口时发生内部错误。

**类型：** Int32

**起始版本：** 19

### static const INVALID_CERT_FORMAT

```cangjie
public static const INVALID_CERT_FORMAT: Int32 = 17500003
```

**功能：** 表示输入证书或凭据的数据格式无效。

**类型：** Int32

**起始版本：** 19

### static const MAX_CERT_COUNT_REACHED

```cangjie
public static const MAX_CERT_COUNT_REACHED: Int32 = 17500004
```

**功能：** 表示证书或凭据数量达到上限。

**类型：** Int32

**起始版本：** 19

### static const NOT_FOUND

```cangjie
public static const NOT_FOUND: Int32 = 17500002
```

**功能：** 表示证书或凭据不存在。

**类型：** Int32

**起始版本：** 19

### static const NOT_SYSTEM_APP

```cangjie
public static const NOT_SYSTEM_APP: Int32 = 202
```

**功能：** 表示当前应用不是系统应用。

**类型：** Int32

**起始版本：** 19

### static const NO_AUTHORIZATION

```cangjie
public static const NO_AUTHORIZATION: Int32 = 17500005
```

**功能：** 表示应用未经用户授权。

**类型：** Int32

**起始版本：** 19

### static const PARAM_ERROR

```cangjie
public static const PARAM_ERROR: Int32 = 401
```

**功能：** 表示输入参数无效。

**类型：** Int32

**起始版本：** 19

### static const PASSWORD_IS_ERROR

```cangjie
public static const PASSWORD_IS_ERROR: Int32 = 17500008
```

**功能：** 表示输入的密码错误。

**类型：** Int32

**起始版本：** 19