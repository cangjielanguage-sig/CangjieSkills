## class PolicyErrorResult

```cangjie
public class PolicyErrorResult {
    public let uri: String
    public let code: PolicyErrorCode
    public let message: String
}
```

**功能：** 授予或使能权限失败的URI策略结果。支持persistPermission、revokePermission、activatePermission、deactivatePermission接口抛出错误时使用。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

### let code

```cangjie
public let code: PolicyErrorCode
```

**功能：** 授权策略失败的URI对应的错误码。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**类型：** [PolicyErrorCode](#enum-policyerrorcode)

**读写能力：** 只读

**起始版本：** 20

### let message

```cangjie
public let message: String
```

**功能：** 授权策略失败的URI对应的原因。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### let uri

```cangjie
public let uri: String
```

**功能：** 需要授予或使能权限的URI。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**类型：** String

**读写能力：** 只读

**起始版本：** 20

## class PolicyInfo

```cangjie
public class PolicyInfo {
    public let uri: String
    public let operationMode: OperationMode
    public init(uri: String, operationMode: OperationMode)
}
```

**功能：** 需要授予或使能权限URI的策略信息。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

### let operationMode

```cangjie
public let operationMode: operationMode
```

**功能：** 授予或使能权限的URI访问模式，参考OperationMode。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**类型：** [OperationMode](#enum-operationmode)

**读写能力：** 只读

**起始版本：** 20

### let uri

```cangjie
public let uri: String
```

**功能：** 需要授予或使能权限的URI。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### init(String, OperationMode)

```cangjie
public init(uri: String, operationMode: OperationMode)
```

**功能：** 构造需要授予或使能权限URI的策略信息。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|需要授予或使能权限的URI。|
|operationMode|[OperationMode](#enum-operationmode)|是|-|授予或使能权限的URI访问模式，参考OperationMode。|