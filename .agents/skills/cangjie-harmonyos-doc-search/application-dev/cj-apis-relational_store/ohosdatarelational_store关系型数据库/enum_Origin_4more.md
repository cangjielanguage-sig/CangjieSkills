## enum Origin

```cangjie
public enum Origin {
    | Local
    | Cloud
    | Remote
    | ...
}
```

**功能：** 表示数据来源。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### Cloud

```cangjie
Cloud
```

**功能：** 表示云端同步的数据。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### Local

```cangjie
Local
```

**功能：** 表示本地数据。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### Remote

```cangjie
Remote
```

**功能：** 表示端端同步的数据。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

## enum Progress

```cangjie
public enum Progress {
    | SyncBegin
    | SyncInProgress
    | SyncFinish
    | ...
}
```

**功能：** 描述端云同步过程的枚举。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### SyncBegin

```cangjie
SyncBegin
```

**功能：** 表示端云同步过程开始。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### SyncFinish

```cangjie
SyncFinish
```

**功能：** 表示端云同步过程已完成。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### SyncInProgress

```cangjie
SyncInProgress
```

**功能：** 表示正在端云同步过程中。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

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

**功能：** 数据库的安全级别枚举。数据库的安全等级仅支持由低向高设置，不支持由高向低设置。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### S1

```cangjie
S1
```

**功能：** 表示数据库的安全级别为低级别，当数据泄露时会产生较低影响。例如，包含壁纸等系统数据的数据库。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### S2

```cangjie
S2
```

**功能：** 表示数据库的安全级别为中级别，当数据泄露时会产生较大影响。例如，包含录音、视频等用户生成数据或通话记录等信息的数据库。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### S3

```cangjie
S3
```

**功能：** 表示数据库的安全级别为高级别，当数据泄露时会产生重大影响。例如，包含用户运动、健康、位置等信息的数据库。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### S4

```cangjie
S4
```

**功能：** 表示数据库的安全级别为关键级别，当数据泄露时会产生严重影响。例如，包含认证凭据、财务数据等信息的数据库。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

## enum SubscribeType

```cangjie
public enum SubscribeType {
    | SubscribeTypeRemote
    | SubscribeTypeCloud
    | SubscribeTypeCloudDetails
    | ...
}
```

**功能：** 描述订阅类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### SubscribeTypeCloud

```cangjie
SubscribeTypeCloud
```

**功能：** 订阅云端数据更改。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### SubscribeTypeCloudDetails

```cangjie
SubscribeTypeCloudDetails
```

**功能：** 订阅云端数据更改详情。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### SubscribeTypeRemote

```cangjie
SubscribeTypeRemote
```

**功能：** 订阅远程数据更改。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22