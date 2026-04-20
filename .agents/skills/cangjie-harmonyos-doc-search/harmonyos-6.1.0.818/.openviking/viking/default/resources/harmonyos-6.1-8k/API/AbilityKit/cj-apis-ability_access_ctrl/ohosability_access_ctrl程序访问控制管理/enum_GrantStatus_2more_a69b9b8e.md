## enum GrantStatus

```cangjie
public enum GrantStatus <: Equatable<GrantStatus> & ToString {
    | PermissionDenied
    | PermissionGranted
    | ...
}
```

**功能：** 表示授权状态的枚举。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 22

**父类型：**

- Equatable\<GrantStatus>
- ToString

### PermissionDenied

```cangjie
PermissionDenied
```

**功能：** 表示未授权。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 22

### PermissionGranted

```cangjie
PermissionGranted
```

**功能：** 表示已授权。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 22

### func !=(GrantStatus)

```cangjie
public operator func !=(other: GrantStatus): Bool
```

**功能：** 对授权状态进行判不等。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GrantStatus](#enum-grantstatus)|是|-|授权状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果授权状态不同，返回true，否则返回false。|

### func ==(GrantStatus)

```cangjie
public operator func ==(other: GrantStatus): Bool
```

**功能：** 对授权状态进行判等。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GrantStatus](#enum-grantstatus)|是|-|授权状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果授权状态相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回授权状态的字符串表示。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|授权状态的字符串表示。|

## type Permissions

```cangjie
public type Permissions = String
```

**功能：** 表示权限名称，是String类型的别名。