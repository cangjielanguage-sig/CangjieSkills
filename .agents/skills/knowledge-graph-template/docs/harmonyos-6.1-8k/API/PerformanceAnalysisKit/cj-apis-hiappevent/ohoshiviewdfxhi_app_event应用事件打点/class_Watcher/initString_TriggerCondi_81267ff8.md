### init(String, TriggerCondition, Array\<AppEventFilter>, Option\<(Int32,Int32,AppEventPackageHolder) -> Unit>, Option\<(String,Array\<AppEventGroup>) -> Unit>)

```cangjie
public init(name: String, triggerCondition!: TriggerCondition = TriggerCondition(),
    appEventFilters!: Array<AppEventFilter> = [],
    onTrigger!: Option<(Int32, Int32, AppEventPackageHolder) -> Unit> = None,
    onReceive!: Option<(String, Array<AppEventGroup>) -> Unit> = None)
```

**功能：** 创建[Watcher](#class-watcher)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|观察者名称，用于唯一标识观察者。首字符必须为字母字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。如testName1、crash_Watcher等。|
|triggerCondition|[TriggerCondition](#class-triggercondition)|否|TriggerCondition()|**命名参数。** 订阅回调触发条件，需要与回调函数onTrigger一同传入才会生效。默认不触发。|
|appEventFilters|Array\<[AppEventFilter](#class-appeventfilter)>|否|[]|**命名参数。** 订阅过滤条件，在需要对订阅事件进行过滤时传入。默认不过滤事件。|
|onTrigger|Option\<(Int32,Int32,[AppEventPackageHolder](#class-appeventpackageholder))->Unit>|否|None|**命名参数。** 订阅回调函数，需要与回调触发条件triggerCondition一同传入才会生效。|
|onReceive|Option\<(String,Array\<[AppEventGroup](#class-appeventgroup)>)->Unit>|否|None|**命名参数。** 订阅实时回调函数，与回调函数onTrigger同时存在时，只触发此回调。|