## class HuksExceptionErrCode

```cangjie
public class HuksExceptionErrCode {
    public static const HUKS_ERR_CODE_PERMISSION_FAIL: Int32 = 201
    public static const HUKS_ERR_CODE_NOT_SYSTEM_APP: Int32 = 202
    public static const HUKS_ERR_CODE_ILLEGAL_ARGUMENT: Int32 = 401
    public static const HUKS_ERR_CODE_NOT_SUPPORTED_API: Int32 = 801
    public static const HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED: Int32 = 12000001
    public static const HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT: Int32 = 12000002
    public static const HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT: Int32 = 12000003
    public static const HUKS_ERR_CODE_FILE_OPERATION_FAIL: Int32 = 12000004
    public static const HUKS_ERR_CODE_COMMUNICATION_FAIL: Int32 = 12000005
    public static const HUKS_ERR_CODE_CRYPTO_FAIL: Int32 = 12000006
    public static const HUKS_ERR_CODE_KEY_AUTH_PERMANENTLY_INVALIDATED: Int32 = 12000007
    public static const HUKS_ERR_CODE_KEY_AUTH_VERIFY_FAILED: Int32 = 12000008
    public static const HUKS_ERR_CODE_KEY_AUTH_TIME_OUT: Int32 = 12000009
    public static const HUKS_ERR_CODE_SESSION_LIMIT: Int32 = 12000010
    public static const HUKS_ERR_CODE_ITEM_NOT_EXIST: Int32 = 12000011
    public static const HUKS_ERR_CODE_EXTERNAL_ERROR: Int32 = 12000012
    public static const HUKS_ERR_CODE_CREDENTIAL_NOT_EXIST: Int32 = 12000013
    public static const HUKS_ERR_CODE_INSUFFICIENT_MEMORY: Int32 = 12000014
    public static const HUKS_ERR_CODE_CALL_SERVICE_FAILED: Int32 = 12000015
}
```

**功能：** 表示错误码的枚举以及对应的错误信息，错误码表示错误类型，错误信息展示错误详情。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### static const HUKS_ERR_CODE_CALL_SERVICE_FAILED

```cangjie
public static const HUKS_ERR_CODE_CALL_SERVICE_FAILED: Int32 = 12000015
```

**功能：** 调用其他系统服务失败。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Int32

**起始版本：** 15

### static const HUKS_ERR_CODE_COMMUNICATION_FAIL

```cangjie
public static const HUKS_ERR_CODE_COMMUNICATION_FAIL: Int32 = 12000005
```

**功能：** 通信失败。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Int32

**起始版本：** 15

### static const HUKS_ERR_CODE_CREDENTIAL_NOT_EXIST

```cangjie
public static const HUKS_ERR_CODE_CREDENTIAL_NOT_EXIST: Int32 = 12000013
```

**功能：** 缺失所需凭据。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Int32

**起始版本：** 15

### static const HUKS_ERR_CODE_CRYPTO_FAIL

```cangjie
public static const HUKS_ERR_CODE_CRYPTO_FAIL: Int32 = 12000006
```

**功能：** 算法库操作失败。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Int32

**起始版本：** 15

### static const HUKS_ERR_CODE_EXTERNAL_ERROR

```cangjie
public static const HUKS_ERR_CODE_EXTERNAL_ERROR: Int32 = 12000012
```

**功能：** 外部错误。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Int32

**起始版本：** 15

### static const HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED

```cangjie
public static const HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED: Int32 = 12000001
```

**功能：** 不支持的功能/特性。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Int32

**起始版本：** 15

### static const HUKS_ERR_CODE_FILE_OPERATION_FAIL

```cangjie
public static const HUKS_ERR_CODE_FILE_OPERATION_FAIL: Int32 = 12000004
```

**功能：** 文件操作失败。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Int32

**起始版本：** 15

### static const HUKS_ERR_CODE_ILLEGAL_ARGUMENT

```cangjie
public static const HUKS_ERR_CODE_ILLEGAL_ARGUMENT: Int32 = 401
```

**功能：** 参数错误导致失败。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Int32

**起始版本：** 15