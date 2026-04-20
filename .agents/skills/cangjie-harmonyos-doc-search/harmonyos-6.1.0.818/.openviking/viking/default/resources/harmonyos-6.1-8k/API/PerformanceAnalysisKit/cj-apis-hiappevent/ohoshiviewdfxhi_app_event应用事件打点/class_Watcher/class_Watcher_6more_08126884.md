## class Watcher

```cangjie
public class Watcher {
    public var name: String
    public var triggerCondition: TriggerCondition
    public var appEventFilters: Array<AppEventFilter>
    public var onTrigger: Option <(Int32, Int32, AppEventPackageHolder) -> Unit>
    public var onReceive: Option <(String, Array<AppEventGroup>) -> Unit>
    public init(name: String, triggerCondition!: TriggerCondition = TriggerCondition(),
        appEventFilters!: Array<AppEventFilter> = [],
        onTrigger!: Option<(Int32, Int32, AppEventPackageHolder) -> Unit> = None,
        onReceive!: Option<(String, Array<AppEventGroup>) -> Unit> = None)
}
```

**功能：** 提供事件观察者的参数选项。用于配置和管理事件的观察者，实现对特定事件的监听和处理。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var appEventFilters

```cangjie
public var appEventFilters: Array<AppEventFilter>
```

**功能：** 订阅过滤条件，在需要对订阅事件进行过滤时传入。

**类型：** Array\<[AppEventFilter](#class-appeventfilter)>

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 观察者名称，用于唯一标识观察者。首字符必须为字母字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。如testName1、crash_Watcher等。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var onReceive

```cangjie
public var onReceive: Option <(String, Array<AppEventGroup>) -> Unit>
```

**功能：** 订阅实时回调函数，与回调函数onTrigger同时存在时，只触发此回调，函数入参说明如下：

domain：回调事件的领域名称；

appEventGroups：回调事件集合。

**类型：** [AppEventGroup](#class-appeventgroup)->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var onTrigger

```cangjie
public var onTrigger: Option <(Int32, Int32, AppEventPackageHolder) -> Unit>
```

**功能：** 订阅回调函数，需要与回调触发条件triggerCondition一同传入才会生效，函数入参说明如下：

curRow：在本次回调触发时的订阅事件总数量；

curSize：在本次回调触发时的订阅事件总大小，单位为byte；

holder：订阅数据持有者对象，可以通过其对订阅事件进行处理。

**类型：** (Int32,Int32,[AppEventPackageHolder](#class-appeventpackageholder))->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var triggerCondition

```cangjie
public var triggerCondition: TriggerCondition
```

**功能：** 订阅回调触发条件，需要与回调函数onTrigger一同传入才会生效。

**类型：** [TriggerCondition](#class-triggercondition)

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22