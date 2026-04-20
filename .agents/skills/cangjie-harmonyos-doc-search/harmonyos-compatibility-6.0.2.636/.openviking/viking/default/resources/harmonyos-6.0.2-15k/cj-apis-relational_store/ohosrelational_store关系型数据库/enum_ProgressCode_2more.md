## enum ProgressCode

```cangjie
public enum ProgressCode {
    | SUCCESS
    | UNKNOWN_ERROR
    | NETWORK_ERROR
    | CLOUD_DISABLED
    | LOCKED_BY_OTHERS
    | RECORD_LIMIT_EXCEEDED
    | NO_SPACE_FOR_ASSET
    | ...
}
```

**功能：** 表示端云同步过程的状态。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### CLOUD_DISABLED

```cangjie
CLOUD_DISABLED
```

**功能：** 表示云端不可用。

**起始版本：** 12

### LOCKED_BY_OTHERS

```cangjie
LOCKED_BY_OTHERS
```

**功能：** 表示有其他设备正在端云同步，本设备无法进行端云同步。请确保无其他设备占用云端资源后，再使用本设备进行端云同步任务。

**起始版本：** 12

### NETWORK_ERROR

```cangjie
NETWORK_ERROR
```

**功能：** 表示端云同步过程遇到网络错误。

**起始版本：** 12

### NO_SPACE_FOR_ASSET

```cangjie
NO_SPACE_FOR_ASSET
```

**功能：** 表示云空间剩余空间小于待同步的资产大小。

**起始版本：** 12

### RECORD_LIMIT_EXCEEDED

```cangjie
RECORD_LIMIT_EXCEEDED
```

**功能：** 表示本次端云同步需要同步的条目或大小超出最大值。由云端配置最大值。

**起始版本：** 12

### SUCCESS

```cangjie
SUCCESS
```

**功能：** 表示端云同步过程成功。

**起始版本：** 12

### UNKNOWN_ERROR

```cangjie
UNKNOWN_ERROR
```

**功能：** 表示端云同步过程遇到未知错误。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取该ProgressCode实例的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回该ProgressCode实例的值。|

## enum RelationalStoreSecurityLevel

```cangjie
public enum RelationalStoreSecurityLevel {
    | S1
    | S2
    | S3
    | S4
    | ...
}
```

**功能：** 数据库的安全级别枚举。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### S1

```cangjie
S1
```

**功能：** 表示数据库的安全级别为低级别，当数据泄露时会产生较低影响。例如，包含壁纸等系统数据的数据库。

**起始版本：** 12

### S2

```cangjie
S2
```

**功能：** 表示数据库的安全级别为中级别，当数据泄露时会产生较大影响。例如，包含录音、视频等用户生成数据或通话记录等信息的数据库。

**起始版本：** 12

### S3

```cangjie
S3
```

**功能：** 表示数据库的安全级别为高级别，当数据泄露时会产生重大影响。例如，包含用户运动、健康、位置等信息的数据库。

**起始版本：** 12

### S4

```cangjie
S4
```

**功能：** 表示数据库的安全级别为关键级别，当数据泄露时会产生严重影响。例如，包含认证凭据、财务数据等信息的数据库。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取该SecurityLevel实例的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回该SecurityLevel实例的值。|