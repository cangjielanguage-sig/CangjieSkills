### var isDeepIdle

```cangjie
public var isDeepIdle: ?Bool = None
```

**功能：** 是否要求设备进入空闲状态。<br>- true表示需要。<br>- false表示不需要。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 12

### var isPersisted

```cangjie
public var isPersisted: ?Bool = None
```

**功能：** 注册的延迟任务是否可保存在系统中。<br>- true表示可保存，即系统重启后。<br>- false表示不可保存。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 12

### var isRepeat

```cangjie
public var isRepeat: ?Bool = None
```

**功能：** 是否循环任务。<br>- true表示循环任务。<br>- false表示非循环任务。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 12

### var netWorkType

```cangjie
public var netWorkType: ?NetworkType = None
```

**功能：** 网络类型。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** ?[NetworkType](#enum-networktype)

**读写能力：** 可读写

**起始版本：** 12

### var parameters

```cangjie
public var parameters: HashMap<String, WorkSchedulerValueType> = HashMap<String, WorkSchedulerValueType>()
```

**功能：** 携带参数信息。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** HashMap\<String, [WorkSchedulerValueType](#enum-workschedulervaluetype)>

**读写能力：** 可读写

**起始版本：** 19

### var repeatCount

```cangjie
public var repeatCount: ?Int32 = None
```

**功能：** 循环次数。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 12

### var repeatCycvarime

```cangjie
public var repeatCycvarime: ?Int32 = None
```

**功能：** 循环间隔，单位为毫秒。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 12

### var storageRequest

```cangjie
public var storageRequest: ?StorageRequest = None
```

**功能：** 存储状态。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** ?[StorageRequest](#enum-storagerequest)

**读写能力：** 可读写

**起始版本：** 12

### var workId

```cangjie
public var workId: Int32
```

**功能：** 延迟任务ID。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12