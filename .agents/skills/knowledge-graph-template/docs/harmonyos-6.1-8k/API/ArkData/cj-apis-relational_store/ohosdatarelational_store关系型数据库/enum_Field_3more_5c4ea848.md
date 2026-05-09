## enum Field

```cangjie
public enum Field {
    | CursorField
    | OriginField
    | DeletedFlagField
    | OwnerField
    | PrivilegeField
    | SharingResourceField
    | ...
}
```

**功能：** 用于谓词查询条件的特殊字段。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### CursorField

```cangjie
CursorField
```

**功能：** 用于cursor查找的字段名。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### DeletedFlagField

```cangjie
DeletedFlagField
```

**功能：** 用于cursor查找的结果集返回时填充的字段，表示云端删除的数据同步到本地后数据是否清理。

返回的结果集中，该字段对应的value为false表示数据未清理，true表示数据已清理。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### OriginField

```cangjie
OriginField
```

**功能：** 用于cursor查找时指定数据来源的字段名。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### OwnerField

```cangjie
OwnerField
```

**功能：** 用于共享表中查找owner时返回的结果集中填充的字段，表示当前共享记录的共享发起者。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### PrivilegeField

```cangjie
PrivilegeField
```

**功能：** 用于共享表中查找共享数据权限时，返回的结果集中填充的字段，表示当前共享记录的允许的操作权限。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### SharingResourceField

```cangjie
SharingResourceField
```

**功能：** 用于数据共享查找共享数据的共享资源时，返回的结果集中填充的字段，表示共享数据的共享资源标识。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

## enum HmacAlgo

```cangjie
public enum HmacAlgo {
    | Sha1
    | Sha256
    | Sha512
    | ...
}
```

**功能：** 数据库的HMAC算法枚举。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### Sha1

```cangjie
Sha1
```

**功能：** HMAC_SHA1算法。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### Sha256

```cangjie
Sha256
```

**功能：** HMAC_SHA256算法。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### Sha512

```cangjie
Sha512
```

**功能：** HMAC_SHA512算法。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

## enum KdfAlgo

```cangjie
public enum KdfAlgo {
    | KdfSha1
    | KdfSha256
    | KdfSha512
    | ...
}
```

**功能：** 数据库的PBKDF2算法枚举。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### KdfSha1

```cangjie
KdfSha1
```

**功能：** PBKDF2_HMAC_SHA1算法。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### KdfSha256

```cangjie
KdfSha256
```

**功能：** PBKDF2_HMAC_SHA256算法。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### KdfSha512

```cangjie
KdfSha512
```

**功能：** PBKDF2_HMAC_SHA512算法。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22