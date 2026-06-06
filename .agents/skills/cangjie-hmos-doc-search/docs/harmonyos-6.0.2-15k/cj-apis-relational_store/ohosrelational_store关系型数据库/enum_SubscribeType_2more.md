## enum SubscribeType

```cangjie
public enum SubscribeType {
    | SUBSCRIBE_TYPE_REMOTE
    | SUBSCRIBE_TYPE_CLOUD
    | SUBSCRIBE_TYPE_CLOUD_DETAILS
    | ...
}
```

**功能：** 描述订阅类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### SUBSCRIBE_TYPE_CLOUD

```cangjie
SUBSCRIBE_TYPE_CLOUD
```

**功能：** 订阅云端数据更改。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 12

### SUBSCRIBE_TYPE_CLOUD_DETAILS

```cangjie
SUBSCRIBE_TYPE_CLOUD_DETAILS
```

**功能：** 订阅云端数据更改详情。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 12

### SUBSCRIBE_TYPE_REMOTE

```cangjie
SUBSCRIBE_TYPE_REMOTE
```

**功能：** 订阅远程数据更改。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取该SubscribeType实例的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回该SubscribeType实例的值。|

## enum SyncMode

```cangjie
public enum SyncMode {
    | SYNC_MODE_PUSH
    | SYNC_MODE_PULL
    | SYNC_MODE_TIME_FIRST
    | SYNC_MODE_NATIVE_FIRST
    | SYNC_MODE_CLOUD_FIRST
    | ...
}
```

**功能：** 指数据库同步模式。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### SYNC_MODE_CLOUD_FIRST

```cangjie
SYNC_MODE_CLOUD_FIRST
```

**功能：** 表示数据从云端同步到本地设备。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 12

### SYNC_MODE_NATIVE_FIRST

```cangjie
SYNC_MODE_NATIVE_FIRST
```

**功能：** 表示数据从本地设备同步到云端。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 12

### SYNC_MODE_PULL

```cangjie
SYNC_MODE_PULL
```

**功能：** 表示数据从远程设备拉至本地设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### SYNC_MODE_PUSH

```cangjie
SYNC_MODE_PUSH
```

**功能：** 表示数据从本地设备推送到远程设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### SYNC_MODE_TIME_FIRST

```cangjie
SYNC_MODE_TIME_FIRST
```

**功能：** 表示数据从修改时间较近的一端同步到修改时间较远的一端。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取该SyncMode实例的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回该SyncMode实例的值。|