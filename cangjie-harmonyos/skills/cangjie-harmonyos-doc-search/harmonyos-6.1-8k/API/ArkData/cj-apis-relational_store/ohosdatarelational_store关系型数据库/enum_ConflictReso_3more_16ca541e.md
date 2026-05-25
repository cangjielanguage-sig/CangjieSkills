## enum ConflictResolution

```cangjie
public enum ConflictResolution {
    | OnConflictNone
    | OnConflictRollback
    | OnConflictAbort
    | OnConflictFail
    | OnConflictIgnore
    | OnConflictReplace
    | ...
}
```

**功能：** 插入和修改接口的冲突解决方式。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### OnConflictAbort

```cangjie
OnConflictAbort
```

**功能：** 表示当冲突发生时，中止当前SQL语句，并撤销当前 SQL 语句所做的任何更改，但是由同一事务中先前的 SQL 语句引起的更改被保留并且事务保持活动状态。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### OnConflictFail

```cangjie
OnConflictFail
```

**功能：** 表示当冲突发生时，中止当前 SQL 语句。但它不会撤销失败的 SQL 语句的先前更改，也不会结束事务。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### OnConflictIgnore

```cangjie
OnConflictIgnore
```

**功能：** 表示当冲突发生时，跳过包含违反约束的行并继续处理 SQL 语句的后续行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### OnConflictNone

```cangjie
OnConflictNone
```

**功能：** 表示当冲突发生时，不做任何处理。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### OnConflictReplace

```cangjie
OnConflictReplace
```

**功能：** 表示当冲突发生时，在插入或更新当前行之前删除导致约束违例的预先存在的行，并且命令会继续正常执行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### OnConflictRollback

```cangjie
OnConflictRollback
```

**功能：** 表示当冲突发生时，中止SQL语句并回滚当前事务。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

## enum DistributedType

```cangjie
public enum DistributedType {
    | DistributedDevice
    | DistributedCloud
    | ...
}
```

**功能：** 表示在不同设备之间分布式的数据库表。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### DistributedCloud

```cangjie
DistributedCloud
```

**功能：** 表示在设备和云端之间分布式的数据库表。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### DistributedDevice

```cangjie
DistributedDevice
```

**功能：** 表示在不同设备之间分布式的数据库表。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

## enum EncryptionAlgo

```cangjie
public enum EncryptionAlgo {
    | Aes256Gcm
    | Aes256Cbc
    | ...
}
```

**功能：** 数据库的加密算法枚举。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### Aes256Cbc

```cangjie
Aes256Cbc
```

**功能：** 数据库使用AES_256_CBC加密。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### Aes256Gcm

```cangjie
Aes256Gcm
```

**功能：** 数据库使用AES_256_GCM加密。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22