## struct ErrorCode

```cangjie
public struct ErrorCode {
    public static const ASSET_SUCCESS: Int32 = 0
    public static const PERMISSION_DENIED: Int32 = 201
    public static const NOT_SYSTEM_APPLICATION: Int32 = 202
    public static const INVALID_ARGUMENT: Int32 = 401
    public static const SERVICE_UNAVAILABLE: Int32 = 24000001
    public static const NOT_FOUND: Int32 = 24000002
    public static const DUPLICATED: Int32 = 24000003
    public static const ACCESS_DENIED: Int32 = 24000004
    public static const STATUS_MISMATCH: Int32 = 24000005
    public static const OUT_OF_MEMORY: Int32 = 24000006
    public static const DATA_CORRUPTED: Int32 = 24000007
    public static const DATABASE_ERROR: Int32 = 24000008
    public static const CRYPTO_ERROR: Int32 = 24000009
    public static const IPC_ERROR: Int32 = 24000010
    public static const BMS_ERROR: Int32 = 24000011
    public static const ACCOUNT_ERROR: Int32 = 24000012
    public static const ACCESS_TOKEN_ERROR: Int32 = 24000013
    public static const FILE_OPERATION_ERROR: Int32 = 24000014
    public static const GET_SYSTEM_TIME_ERROR: Int32 = 24000015
    public static const LIMIT_EXCEEDED: Int32 = 24000016
    public static const UNSUPPORTED: Int32 = 24000017
}
```

**功能：** 表示错误码。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### static const ACCESS_DENIED

```cangjie
public static const ACCESS_DENIED: Int32 = 24000004
```

**功能：** 拒绝访问关键资产。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19

### static const ACCESS_TOKEN_ERROR

```cangjie
public static const ACCESS_TOKEN_ERROR: Int32 = 24000013
```

**功能：** 访问控制服务异常。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19

### static const ACCOUNT_ERROR

```cangjie
public static const ACCOUNT_ERROR: Int32 = 24000012
```

**功能：** 账号系统异常。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19

### static const ASSET_SUCCESS

```cangjie
public static const ASSET_SUCCESS: Int32 = 0
```

**功能：** 调用成功。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19

### static const BMS_ERROR

```cangjie
public static const BMS_ERROR: Int32 = 24000011
```

**功能：** 包管理服务异常。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19

### static const CRYPTO_ERROR

```cangjie
public static const CRYPTO_ERROR: Int32 = 24000009
```

**功能：** 算法库操作失败。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19

### static const DATABASE_ERROR

```cangjie
public static const DATABASE_ERROR: Int32 = 24000008
```

**功能：** 数据库操作失败。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19

### static const DATA_CORRUPTED

```cangjie
public static const DATA_CORRUPTED: Int32 = 24000007
```

**功能：** 关键资产损坏。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19

### static const DUPLICATED

```cangjie
public static const DUPLICATED: Int32 = 24000003
```

**功能：** 关键资产已存在。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19

### static const FILE_OPERATION_ERROR

```cangjie
public static const FILE_OPERATION_ERROR: Int32 = 24000014
```

**功能：** 文件操作失败。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19

### static const GET_SYSTEM_TIME_ERROR

```cangjie
public static const GET_SYSTEM_TIME_ERROR: Int32 = 24000015
```

**功能：** 获取系统时间失败。

**系统能力：** SystemCapability.Security.Asset

**类型：** Int32

**起始版本：** 19