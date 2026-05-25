## class AppEventGroup

```cangjie
public class AppEventGroup {
    public var name: String
    public var appEventInfos: Array<AppEventInfo>
}
```

**功能：** 提供订阅返回的事件组的参数定义。可用于获取事件组的详细信息，事件组常在[Watcher](#class-watcher)的onReceive回调中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var appEventInfos

```cangjie
public var appEventInfos: Array<AppEventInfo>
```

**功能：** 事件对象集合。

**类型：** Array\<[AppEventInfo](#class-appeventinfo)>

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 事件名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22