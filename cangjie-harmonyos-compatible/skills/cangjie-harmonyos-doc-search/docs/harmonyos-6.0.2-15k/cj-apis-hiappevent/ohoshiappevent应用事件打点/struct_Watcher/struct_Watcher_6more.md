## struct Watcher

```cangjie
public struct Watcher {
    public let name: String
    public let triggerCondition: TriggerCondition
    public let appEventFilters: Array<AppEventFilter>
    public let onTrigger: Option<(Int32, Int32, AppEventPackageHolder) -> Unit>
    public let onReceive: Option<(String, Array<AppEventGroup>) -> Unit>
    public init(name: String, triggerCondition!: TriggerCondition = TriggerCondition(), appEventFilters!: Array<AppEventFilter> = [],
                onTrigger!: Option<(Int32, Int32, AppEventPackageHolder) -> Unit> = None,
                onReceive!: Option<(String, Array<AppEventGroup>) -> Unit> = None)
}
```

**功能：** 提供了应用事件观察者的参数选项。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### let appEventFilters

```cangjie
public let appEventFilters: Array<AppEventFilter>
```

**功能：** 订阅过滤条件，在需要对订阅事件进行过滤时传入。

**类型：** Array\<[AppEventFilter](#struct-appeventfilter)>

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 观察者名称，用于唯一标识观察者。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let onReceive

```cangjie
public let onReceive: Option<(String, Array<AppEventGroup>) -> Unit>
```

**功能：** 订阅实时回调函数，与回调函数onTrigger同时存在时，只触发此回调。回调函数的第一个参数表示回调事件的领域名称，回调函数的第二个参数表示回调事件集合。

**类型：** Option\<(String, Array\<[AppEventGroup](#struct-appeventgroup)>) -> Unit>

**读写能力：** 只读

**起始版本：** 12

### let onTrigger

```cangjie
public let onTrigger: Option<(Int32, Int32, AppEventPackageHolder) -> Unit>
```

**功能：** 订阅回调函数，需要与回调触发条件triggerCondition一同传入才会生效。回调函数的第一个参数表示在本次回调触发时的订阅事件总数量。回调函数的第二个参数表示在本次回调触发时的订阅事件总大小，单位为byte。回调函数的第三个参数表示订阅数据持有者对象，可以通过其对订阅事件进行处理。

**类型：** Option\<(Int32, Int32, [AppEventPackageHolder](#class-appeventpackageholder)) -> Unit>

**读写能力：** 只读

**起始版本：** 12

### let triggerCondition

```cangjie
public let triggerCondition: TriggerCondition
```

**功能：** 订阅回调触发条件，需要与回调函数onTrigger一同传入才会生效。

**类型：** [TriggerCondition](#struct-triggercondition)

**读写能力：** 只读

**起始版本：** 12