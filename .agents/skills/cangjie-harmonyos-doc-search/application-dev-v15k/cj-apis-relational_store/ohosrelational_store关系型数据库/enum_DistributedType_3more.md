## enum DistributedType

```cangjie
public enum DistributedType {
    | DISTRIBUTED_DEVICE
    | DISTRIBUTED_CLOUD
    | ...
}
```

**功能：** 描述表的分布式类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core               |

**起始版本：** 12

### DISTRIBUTED_CLOUD

```cangjie
DISTRIBUTED_CLOUD
```

**功能：** 表示在设备和云端之间分布式的数据库表。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 12

### DISTRIBUTED_DEVICE

```cangjie
DISTRIBUTED_DEVICE
```

**功能：** 表示在不同设备之间分布式的数据库表。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取该DistributedType实例的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回该DistributedType实例的值。|

## enum Field

```cangjie
public enum Field {
    | CURSOR_FIELD
    | ORIGIN_FIELD
    | DELETED_FLAG_FIELD
    | OWNER_FIELD
    | PRIVILEGE_FIELD
    | SHARING_RESOURCE_FIELD
    | ...
}
```

**功能：** 用于谓词查询条件的特殊字段。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 12

### CURSOR_FIELD

```cangjie
CURSOR_FIELD
```

**功能：** 用于cursor查找的字段名。

**起始版本：** 12

### DELETED_FLAG_FIELD

```cangjie
DELETED_FLAG_FIELD
```

**功能：** 用于cursor查找的结果集返回时填充的字段，表示云端删除的数据同步到本地后数据是否清理。返回的结果集中，该字段对应的value为false表示数据未清理，true表示数据已清理。

**起始版本：** 12

### ORIGIN_FIELD

```cangjie
ORIGIN_FIELD
```

**功能：** 用于cursor查找时指定数据来源的字段名。

**起始版本：** 12

### OWNER_FIELD

```cangjie
OWNER_FIELD
```

**功能：** 用于共享表中查找owner时返回的结果集中填充的字段，表示当前共享记录的共享发起者。

**起始版本：** 12

### PRIVILEGE_FIELD

```cangjie
PRIVILEGE_FIELD
```

**功能：** 用于共享表中查找共享数据权限时返回的结果集中填充的字段，表示当前共享记录的允许的操作权限。

**起始版本：** 12

### SHARING_RESOURCE_FIELD

```cangjie
SHARING_RESOURCE_FIELD
```

**功能：** 用于数据共享时查找共享数据的共享资源时返回的结果集中填充的字段，表示共享数据的共享资源标识。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): String
```

**功能：** 获取该Field实例的值。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回该Field实例的值。|

## enum Origin

```cangjie
public enum Origin {
    | LOCAL
    | CLOUD
    | REMOTE
    | ...
}
```

**功能：** 表示数据来源。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 12

### CLOUD

```cangjie
CLOUD
```

**功能：** 表示云端同步的数据。

**起始版本：** 12

### LOCAL

```cangjie
LOCAL
```

**功能：** 表示本地数据。

**起始版本：** 12

### REMOTE

```cangjie
REMOTE
```

**功能：** 表示端端同步的数据。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取该Origin实例的值。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回该Origin实例的值。|