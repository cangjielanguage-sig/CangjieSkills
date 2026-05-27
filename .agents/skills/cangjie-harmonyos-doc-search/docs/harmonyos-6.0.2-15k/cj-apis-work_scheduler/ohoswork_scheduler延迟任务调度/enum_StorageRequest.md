## enum StorageRequest

```cangjie
public enum StorageRequest {
    | STORAGE_LEVEL_LOW
    | STORAGE_LEVEL_OKAY
    | STORAGE_LEVEL_LOW_OR_OKAY
    |...
}
```

**功能：** 触发延迟回调的存储状态。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### STORAGE_LEVEL_LOW

```cangjie
STORAGE_LEVEL_LOW
```

**功能：** 表示这个触发条件是存储空间不足。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### STORAGE_LEVEL_LOW_OR_OKAY

```cangjie
STORAGE_LEVEL_LOW_OR_OKAY
```

**功能：** 表示这个触发条件是存储空间不足或者从存储空间不足恢复到正常。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### STORAGE_LEVEL_OKAY

```cangjie
STORAGE_LEVEL_OKAY
```

**功能：** 表示这个触发条件是从存储空间不足恢复到正常。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12