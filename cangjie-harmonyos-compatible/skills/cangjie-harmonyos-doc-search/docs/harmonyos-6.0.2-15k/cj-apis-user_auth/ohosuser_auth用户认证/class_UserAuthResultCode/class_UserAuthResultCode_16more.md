## class UserAuthResultCode

```cangjie
public class UserAuthResultCode {
    public static const OHOS_CHECK_PERMISSION_FAILED: Int32 = 201
    public static const OHOS_CHECK_SYSTEM_APP_FAILED: Int32 = 202
    public static const OHOS_INVALID_PARAM: Int32 = 401
    public static const SUCCESS: Int32 = 12500000
    public static const FAIL: Int32 = 12500001
    public static const GENERAL_ERROR: Int32 = 12500002
    public static const CANCELED: Int32 = 12500003
    public static const TIMEOUT: Int32 = 12500004
    public static const TYPE_NOT_SUPPORT: Int32 = 12500005
    public static const TRUST_LEVEL_NOT_SUPPORT: Int32 = 12500006
    public static const BUSY: Int32 = 12500007
    public static const LOCKED: Int32 = 12500009
    public static const NOT_ENROLLED: Int32 = 12500010
    public static const CANCELED_FROM_WIDGET: Int32 = 12500011
    public static const HARDWARE_NOT_SUPPORTED: Int32 = 12500012
    public static const PIN_EXPIRED: Int32 = 12500013
}
```

**功能：** 表示返回码。

关于错误码的具体信息，可在[用户认证错误码](../../errorcodes/cj-errorcode-user-auth.md)中查看。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

### static const BUSY

```cangjie
public static const BUSY: Int32 = 12500007
```

**功能：** 忙碌状态。

**类型：** Int32

**起始版本：** 19

### static const CANCELED

```cangjie
public static const CANCELED: Int32 = 12500003
```

**功能：** 操作取消。

**类型：** Int32

**起始版本：** 19

### static const CANCELED_FROM_WIDGET

```cangjie
public static const CANCELED_FROM_WIDGET: Int32 = 12500011
```

**功能：** 当前的认证操作被用户从组件取消。返回这个错误码，表示使用应用自定义认证。

**类型：** Int32

**起始版本：** 19

### static const FAIL

```cangjie
public static const FAIL: Int32 = 12500001
```

**功能：** 认证失败。

**类型：** Int32

**起始版本：** 19

### static const GENERAL_ERROR

```cangjie
public static const GENERAL_ERROR: Int32 = 12500002
```

**功能：** 操作通用错误。

**类型：** Int32

**起始版本：** 19

### static const HARDWARE_NOT_SUPPORTED

```cangjie
public static const HARDWARE_NOT_SUPPORTED: Int32 = 12500012
```

**功能：** 当前硬件不支持该认证操作。

**类型：** Int32

**起始版本：** 19

### static const LOCKED

```cangjie
public static const LOCKED: Int32 = 12500009
```

**功能：** 认证器已锁定。

**类型：** Int32

**起始版本：** 19

### static const NOT_ENROLLED

```cangjie
public static const NOT_ENROLLED: Int32 = 12500010
```

**功能：** 用户未录入认证信息。

**类型：** Int32

**起始版本：** 19

### static const OHOS_CHECK_PERMISSION_FAILED

```cangjie
public static const OHOS_CHECK_PERMISSION_FAILED: Int32 = 201
```

**功能：** 权限校验失败。

**类型：** Int32

**起始版本：** 19

### static const OHOS_CHECK_SYSTEM_APP_FAILED

```cangjie
public static const OHOS_CHECK_SYSTEM_APP_FAILED: Int32 = 202
```

**功能：** 非系统应用调用。

**类型：** Int32

**起始版本：** 19

### static const OHOS_INVALID_PARAM

```cangjie
public static const OHOS_INVALID_PARAM: Int32 = 401
```

**功能：** 参数错误。

**类型：** Int32

**起始版本：** 19

### static const PIN_EXPIRED

```cangjie
public static const PIN_EXPIRED: Int32 = 12500013
```

**功能：** 当前的认证操作执行失败。返回这个错误码，表示系统锁屏密码过期。

**类型：** Int32

**起始版本：** 19

### static const SUCCESS

```cangjie
public static const SUCCESS: Int32 = 12500000
```

**功能：** 执行成功。

**类型：** Int32

**起始版本：** 19

### static const TIMEOUT

```cangjie
public static const TIMEOUT: Int32 = 12500004
```

**功能：** 操作超时。

**类型：** Int32

**起始版本：** 19

### static const TRUST_LEVEL_NOT_SUPPORT

```cangjie
public static const TRUST_LEVEL_NOT_SUPPORT: Int32 = 12500006
```

**功能：** 不支持的认证等级。

**类型：** Int32

**起始版本：** 19