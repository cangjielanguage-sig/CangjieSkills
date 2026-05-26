## enum AssetStatus

```cangjie
public enum AssetStatus {
    | ASSET_NORMAL
    | ASSET_INSERT
    | ASSET_UPDATE
    | ASSET_DELETE
    | ASSET_ABNORMAL
    | ASSET_DOWNLOADING
    | ...
}
```

**功能：** 描述资产附件的状态枚举。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### ASSET_ABNORMAL

```cangjie
ASSET_ABNORMAL
```

**功能：** 表示资产状态异常。

**起始版本：** 12

### ASSET_DELETE

```cangjie
ASSET_DELETE
```

**功能：** 表示资产需要在云端删除。

**起始版本：** 12

### ASSET_DOWNLOADING

```cangjie
ASSET_DOWNLOADING
```

**功能：** 表示资产正在下载到本地设备。

**起始版本：** 12

### ASSET_INSERT

```cangjie
ASSET_INSERT
```

**功能：** 表示资产需要插入到云端。

**起始版本：** 12

### ASSET_NORMAL

```cangjie
ASSET_NORMAL
```

**功能：** 表示资产状态正常。

**起始版本：** 12

### ASSET_UPDATE

```cangjie
ASSET_UPDATE
```

**功能：** 表示资产需要更新到云端。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取该AssetStatus实例的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回该AssetStatus实例的值。|

## enum ChangeType

```cangjie
public enum ChangeType {
    | DATA_CHANGE
    | ASSET_CHANGE
    | ...
}
```

**功能：** 描述数据变更类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### ASSET_CHANGE

```cangjie
ASSET_CHANGE
```

**功能：** 表示是资产附件发生了变更。

**起始版本：** 12

### DATA_CHANGE

```cangjie
DATA_CHANGE
```

**功能：** 表示是数据发生变更。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取该ChangeType实例的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回该ChangeType实例的值。|

## enum ConflictResolution

```cangjie
public enum ConflictResolution {
    | ON_CONFLICT_NONE
    | ON_CONFLICT_ROLLBACK
    | ON_CONFLICT_ABORT
    | ON_CONFLICT_FAIL
    | ON_CONFLICT_IGNORE
    | ON_CONFLICT_REPLACE
    | ...
}
```

**功能：** 插入和修改接口的冲突解决方式。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### ON_CONFLICT_ABORT

```cangjie
ON_CONFLICT_ABORT
```

**功能：** 表示当冲突发生时，中止当前SQL语句，并撤销当前SQL语句所做的任何更改，但是由同一事务中先前的SQL语句引起的更改被保留并且事务保持活动状态。

**起始版本：** 12

### ON_CONFLICT_FAIL

```cangjie
ON_CONFLICT_FAIL
```

**功能：** 表示当冲突发生时，中止当前SQL语句。但它不会撤销失败的SQL语句的先前更改，也不会结束事务。

**起始版本：** 12

### ON_CONFLICT_IGNORE

```cangjie
ON_CONFLICT_IGNORE
```

**功能：** 表示当冲突发生时，跳过包含违反约束的行并继续处理SQL语句的后续行。

**起始版本：** 12

### ON_CONFLICT_NONE

```cangjie
ON_CONFLICT_NONE
```

**功能：** 表示当冲突发生时，不做任何处理。

**起始版本：** 12

### ON_CONFLICT_REPLACE

```cangjie
ON_CONFLICT_REPLACE
```

**功能：** 表示当冲突发生时，在插入或更新当前行之前删除导致约束违例的预先存在的行，并且命令会继续正常执行。

**起始版本：** 12

### ON_CONFLICT_ROLLBACK

```cangjie
ON_CONFLICT_ROLLBACK
```

**功能：** 表示当冲突发生时，中止SQL语句并回滚当前事务。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取该ConflictResolution实例的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回该ConflictResolution实例的值。|