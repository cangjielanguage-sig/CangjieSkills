## class NavDesitinationInfo

```cangjie
public class NavDesitinationInfo {
    public NavDesitinationInfo(
        public let navigationId: String,
        public let name: String,
        public let state: NavDestinationState,
        public let index: Int32,
        public let param: String,
        public let navDestinationId: String
    )
}
```

**功能：** NavDestination组件信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let index

```cangjie
public let index: Int32
```

**功能：** 表示NavDestination在页面栈中的索引。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let name

```cangjie
public let name: String
```

**功能：** 表示NavDestination组件的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let navDestinationId

```cangjie
public let navDestinationId: String
```

**功能：** 表示NavDestination组件的唯一标识ID。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let navigationId

```cangjie
public let navigationId: String
```

**功能：** 表示包含NavDestination组件的Navigation组件的id。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let param

```cangjie
public let param: String
```

**功能：** 表示NavDestination组件的参数。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let state

```cangjie
public let state: NavDestinationState
```

**功能：** 表示NavDestination组件的状态。

**类型：** [NavDestinationState](#enum-navdestinationstate)

**读写能力：** 只读

**起始版本：** 19

### NavDesitinationInfo(String, String, NavDestinationState, Int32, String, String)

```cangjie
public NavDesitinationInfo(
    public let navigationId: String,
    public let name: String,
    public let state: NavDestinationState,
    public let index: Int32,
    public let param: String,
    public let navDestinationId: String
)
```

**功能：** 构造NavDestination组件信息对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|navigationId|String|是|-|包含NavDestination组件的Navigation组件的id。|
|name|String|是|-|NavDestination组件的名称。|
|state|[NavDestinationState](#enum-navdestinationstate)|是|-|NavDestination组件的状态。|
|index|Int32|是|-|NavDestination在页面栈中的索引。取值范围：[0, +∞)|
|param|String|是|-|NavDestination组件的参数。|
|navDestinationId|String|是|-|NavDestination组件的唯一标识ID。|