## class NavDestinationSwitchObserverOptions

```cangjie
public class NavDestinationSwitchObserverOptions {
    public NavDestinationSwitchObserverOptions(
        public let navigationId: String
    )
}
```

**功能：** Navigation组件页面切换事件的监听选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let navigationId

```cangjie
public let navigationId: String
```

**功能：** 表示指定需要监听的Navigation的ID。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### NavDestinationSwitchObserverOptions(String)

```cangjie
public NavDestinationSwitchObserverOptions(
    public let navigationId: String
)
```

**功能：** 构造Navigation组件页面切换事件的监听选项对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|navigationId|String|是|-|指定需要监听的Navigation的ID。|

## class ObserverOptions

```cangjie
public class ObserverOptions {
    public ObserverOptions(
        public let id: String
    )
}
```

**功能：** Observer选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let id

```cangjie
public let id: String
```

**功能：** 表示组件的id。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### ObserverOptions(String)

```cangjie
public ObserverOptions(
    public let id: String
)
```

**功能：** 构造Observer选项对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|组件的id。|

## class ScrollEventInfo

```cangjie
public class ScrollEventInfo {
    public ScrollEventInfo(
        public let id: String,
        public let uniqueId: Int32,
        public let scrollEvent: ScrollEventType,
        public let offset: Float32
    )
}
```

**功能：** ScrollEvent滚动信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let id

```cangjie
public let id: String
```

**功能：** 表示滚动组件的id。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let offset

```cangjie
public let offset: Float32
```

**功能：** 表示滚动组件的当前偏移量。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### let scrollEvent

```cangjie
public let scrollEvent: ScrollEventType
```

**功能：** 表示滚动事件的类型。

**类型：** [ScrollEventType](#enum-scrolleventtype)

**读写能力：** 只读

**起始版本：** 19

### let uniqueId

```cangjie
public let uniqueId: Int32
```

**功能：** 表示滚动组件的uniqueId。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### ScrollEventInfo(String, Int32, ScrollEventType, Float32)

```cangjie
public ScrollEventInfo(
    public let id: String,
    public let uniqueId: Int32,
    public let scrollEvent: ScrollEventType,
    public let offset: Float32
)
```

**功能：** 构造ScrollEvent滚动信息对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|滚动组件的id。|
|uniqueId|Int32|是|-|滚动组件的uniqueId。|
|scrollEvent|[ScrollEventType](#enum-scrolleventtype)|是|-|滚动事件的类型。|
|offset|Float32|是|-|滚动组件的当前偏移量。|