## class TabContentInfo

```cangjie
public class TabContentInfo {
    public TabContentInfo(
        public let tabContentId: String,
        public let tabContentUniqueId: Int32,
        public let state: TabContentState,
        public let id: String,
        public let uniqueId: Int32
    )
}
```

**功能：** TabContent页面的切换信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let id

```cangjie
public let id: String
```

**功能：** 表示Tabs组件的id。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let state

```cangjie
public let state: TabContentState
```

**功能：** 表示TabContent组件的状态。

**类型：** [TabContentState](#enum-tabcontentstate)

**读写能力：** 只读

**起始版本：** 19

### let tabContentId

```cangjie
public let tabContentId: String
```

**功能：** 表示TabContent组件的id。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let tabContentUniqueId

```cangjie
public let tabContentUniqueId: Int32
```

**功能：** 表示TabContent组件的uniqueId。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let uniqueId

```cangjie
public let uniqueId: Int32
```

**功能：** 表示Tabs组件的uniqueId。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### TabContentInfo(String, Int32, TabContentState, String, Int32)

```cangjie
public TabContentInfo(
    public let tabContentId: String,
    public let tabContentUniqueId: Int32,
    public let state: TabContentState,
    public let id: String,
    public let uniqueId: Int32
)
```

**功能：** 构造TabContent页面的切换信息对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tabContentId|String|是|-|TabContent组件的id。|
|tabContentUniqueId|Int32|是|-|TabContent组件的uniqueId。|
|state|[TabContentState](#enum-tabcontentstate)|是|-|TabContent组件的状态。|
|id|String|是|-|Tabs组件的id。|
|uniqueId|Int32|是|-|Tabs组件的uniqueId。|