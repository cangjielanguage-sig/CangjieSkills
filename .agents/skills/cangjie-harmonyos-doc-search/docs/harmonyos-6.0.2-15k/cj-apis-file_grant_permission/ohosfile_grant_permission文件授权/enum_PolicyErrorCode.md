## enum PolicyErrorCode

```cangjie
public enum PolicyErrorCode <: Equatable<PolicyErrorCode> & ToString {
    | PersistenceForbidden
    | InvalidMode
    | InvalidPath
    | PermissionNotPersisted
    | ...
}
```

**功能：** 枚举，授予或使能权限策略失败的URI对应的错误码。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**父类型：**

- Equatable\<PolicyErrorCode>
- ToString

### InvalidMode

```cangjie
InvalidMode
```

**功能：** 无效的模式。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

### InvalidPath

```cangjie
InvalidPath
```

**功能：** 无效的路径。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

### PermissionNotPersisted

```cangjie
PermissionNotPersisted
```

**功能：** URI禁止被持久化。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

### PersistenceForbidden

```cangjie
PersistenceForbidden
```

**功能：** 权限没有被持久化。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

### prop value

```cangjie
public prop value: UInt8
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**类型：** UInt8

**读写能力：** 只读

### func !=(PolicyErrorCode)

```cangjie
public operator func !=(other: PolicyErrorCode): Bool
```

**功能：** 对错误码进行判不等。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PolicyErrorCode](#enum-policyerrorcode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果错误码不同，返回true，否则返回false。|

### func ==(PolicyErrorCode)

```cangjie
public operator func ==(other: PolicyErrorCode): Bool
```

**功能：** 对错误码进行判等。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PolicyErrorCode](#enum-policyerrorcode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果错误码相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回错误码的字符串表示。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|错误码的字符串表示。|