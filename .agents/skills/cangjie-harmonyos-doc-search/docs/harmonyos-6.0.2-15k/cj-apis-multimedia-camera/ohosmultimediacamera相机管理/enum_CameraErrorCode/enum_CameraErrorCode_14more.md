## enum CameraErrorCode

```cangjie
public enum CameraErrorCode <: Equatable<CameraErrorCode> & ToString {
    | INVALID_ARGUMENT
    | OPERATION_NOT_ALLOWED
    | SESSION_NOT_CONFIG
    | SESSION_NOT_RUNNING
    | SESSION_CONFIG_LOCKED
    | DEVICE_SETTING_LOCKED
    | CONFLICT_CAMERA
    | DEVICE_DISABLED
    | DEVICE_PREEMPTED
    | UNRESOLVED_CONFLICTS_WITH_CURRENT_CONFIGURATIONS
    | SERVICE_FATAL_ERROR
    | ...
}
```

**功能：** 相机错误码。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<CameraErrorCode>
- ToString

| 名称                       | 值          | 说明            |
| :------------------------  | :---       | :-----------    |
| INVALID_ARGUMENT           | 7400101    | 参数缺失或者参数类型不对。   |
| OPERATION_NOT_ALLOWED      | 7400102    | 操作流程不对，不允许。     |
| SESSION_NOT_CONFIG         | 7400103    | session 未配置返回。       |
| SESSION_NOT_RUNNING        | 7400104    | session 未运行返回。    |
| SESSION_CONFIG_LOCKED      | 7400105    | session 配置已锁定返回。     |
| DEVICE_SETTING_LOCKED      | 7400106    | 设备设置已锁定返回。     |
| CONFLICT_CAMERA            | 7400107    | 设备重复打开返回。     |
| DEVICE_DISABLED            | 7400108    | 安全原因摄像头被禁用。     |
| DEVICE_PREEMPTED           | 7400109    | 相机被抢占导致无法使用。     |
| UNRESOLVED_CONFLICTS_WITH_CURRENT_CONFIGURATIONS | 7400110   | 与当前配置存在冲突。     |
| SERVICE_FATAL_ERROR        | 7400201    | 相机服务错误返回。     |

### CONFLICT_CAMERA

```cangjie
CONFLICT_CAMERA
```

**功能：** 设备重复打开返回。

**起始版本：** 19

### DEVICE_DISABLED

```cangjie
DEVICE_DISABLED
```

**功能：** 安全原因摄像头被禁用。

**起始版本：** 19

### DEVICE_PREEMPTED

```cangjie
DEVICE_PREEMPTED
```

**功能：** 相机被抢占导致无法使用。

**起始版本：** 19

### DEVICE_SETTING_LOCKED

```cangjie
DEVICE_SETTING_LOCKED
```

**功能：** 设备设置已锁定返回。

**起始版本：** 19

### INVALID_ARGUMENT

```cangjie
INVALID_ARGUMENT
```

**功能：** 参数缺失或者参数类型不对。

**起始版本：** 19

### OPERATION_NOT_ALLOWED

```cangjie
OPERATION_NOT_ALLOWED
```

**功能：** 操作流程不对，不允许。

**起始版本：** 19

### SERVICE_FATAL_ERROR

```cangjie
SERVICE_FATAL_ERROR
```

**功能：** 相机服务错误返回。

**起始版本：** 19

### SESSION_CONFIG_LOCKED

```cangjie
SESSION_CONFIG_LOCKED
```

**功能：** session 配置已锁定返回。

**起始版本：** 19

### SESSION_NOT_CONFIG

```cangjie
SESSION_NOT_CONFIG
```

**功能：** session 未配置返回。

**起始版本：** 19

### SESSION_NOT_RUNNING

```cangjie
SESSION_NOT_RUNNING
```

**功能：** session 未运行返回。

**起始版本：** 19

### UNRESOLVED_CONFLICTS_WITH_CURRENT_CONFIGURATIONS

```cangjie
UNRESOLVED_CONFLICTS_WITH_CURRENT_CONFIGURATIONS
```

**功能：** 与当前配置存在冲突。

**起始版本：** 19

### func !=(CameraErrorCode)

```cangjie
public operator func !=(other: CameraErrorCode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraErrorCode](#enum-cameraerrorcode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CameraErrorCode)

```cangjie
public operator func ==(other: CameraErrorCode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraErrorCode](#enum-cameraerrorcode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|