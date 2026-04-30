### init(String, TriggerCondition, Array\<AppEventFilter>, Option\<(Int32, Int32, AppEventPackageHolder) -> Unit>, Option\<(String, Array\<AppEventGroup>) -> Unit>)

```cangjie
public init(name: String, triggerCondition!: TriggerCondition = TriggerCondition(), appEventFilters!: Array<AppEventFilter> = [],
            onTrigger!: Option<(Int32, Int32, AppEventPackageHolder) -> Unit> = None,
            onReceive!: Option<(String, Array<AppEventGroup>) -> Unit> = None)
```

**功能：** 创建[Watcher](#struct-watcher)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|观察者名称，用于唯一标识观察者。|
|triggerCondition|[TriggerCondition](#struct-triggercondition)|否|TriggerCondition()| **命名参数。** 订阅回调触发条件，需要与回调函数onTrigger一同传入才会生效。|
|appEventFilters|Array\<[AppEventFilter](#struct-appeventfilter)>|否|[]| **命名参数。** 订阅过滤条件，在需要对订阅事件进行过滤时传入。|
|onTrigger|Option\<(Int32, Int32, [AppEventPackageHolder](#class-appeventpackageholder)) -> Unit>|否|None| **命名参数。** 订阅回调函数，需要与回调触发条件triggerCondition一同传入才会生效，函数入参说明如下：<br>curRow：在本次回调触发时的订阅事件总数量； <br>curSize：在本次回调触发时的订阅事件总大小，单位为byte；<br/>holder：订阅数据持有者对象，可以通过其对订阅事件进行处理。|
|onReceive|Option\<(String, Array\<[AppEventGroup](#struct-appeventgroup)>) -> Unit>|否|None| **命名参数。** 订阅实时回调函数，与回调函数onTrigger同时存在时，只触发此回调，函数入参说明如下：<br>domain：回调事件的领域名称；<br>appEventGroups：回调事件集合。|