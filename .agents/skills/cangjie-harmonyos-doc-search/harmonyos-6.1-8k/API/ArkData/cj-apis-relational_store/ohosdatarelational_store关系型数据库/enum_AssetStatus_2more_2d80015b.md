## enum AssetStatus

```cangjie
public enum AssetStatus {
    | AssetNormal
    | AssetInsert
    | AssetUpdate
    | AssetDelete
    | AssetAbnormal
    | AssetDownloading
    | ...
}
```

**功能：** 描述资产附件的状态枚举。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### AssetAbnormal

```cangjie
AssetAbnormal
```

**功能：** 表示资产状态异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### AssetDelete

```cangjie
AssetDelete
```

**功能：** 表示资产需要在云端删除。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### AssetDownloading

```cangjie
AssetDownloading
```

**功能：** 表示资产正在下载到本地设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### AssetInsert

```cangjie
AssetInsert
```

**功能：** 表示资产需要插入到云端。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### AssetNormal

```cangjie
AssetNormal
```

**功能：** 表示资产状态正常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### AssetUpdate

```cangjie
AssetUpdate
```

**功能：** 表示资产需要更新到云端。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

## enum ChangeType

```cangjie
public enum ChangeType {
    | DataChange
    | AssetChange
    | ...
}
```

**功能：** 描述数据变更类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### AssetChange

```cangjie
AssetChange
```

**功能：** 表示是资产附件发生了变更。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### DataChange

```cangjie
DataChange
```

**功能：** 表示是数据发生变更。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22