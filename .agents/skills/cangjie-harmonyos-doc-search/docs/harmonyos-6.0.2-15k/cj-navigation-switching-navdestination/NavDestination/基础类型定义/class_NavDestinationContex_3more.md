### class NavDestinationContext

```cangjie
public class NavDestinationContext {
    public var pathInfo: NavPathInfo
    public var pathStack: NavPathStack
    public var navDestinationId: String
    public init(
        pathInfo: NavPathInfo,
        pathStack: NavPathStack,
        navDestinationId: String
    )
}
```

**功能：** NavDestination上下文信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var navDestinationId

```cangjie
public var navDestinationId: String
```

**功能：** 当前NavDestination的唯一ID，由系统自动生成，和组件通用属性id无关。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

#### var pathInfo

```cangjie
public var pathInfo: NavPathInfo
```

**功能：** 跳转NavDestination时指定的参数。

**类型：** [NavPathInfo](./cj-navigation-switching-navigation.md#class-navpathinfo)

**读写能力：** 可读写

**起始版本：** 19

#### var pathStack

```cangjie
public var pathStack: NavPathStack
```

**功能：** 当前NavDestination所处的页面栈。

**类型：** [NavPathStack](./cj-navigation-switching-navigation.md#class-navpathstack)

**读写能力：** 可读写

**起始版本：** 19

#### init(NavPathInfo, NavPathStack, String)

```cangjie
public init(
    pathInfo: NavPathInfo,
    pathStack: NavPathStack,
    navDestinationId: String
)
```

**功能：** 构造一个NavDestinationContext类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pathInfo|[NavPathInfo](./cj-navigation-switching-navigation.md#class-navpathinfo)|是|-|跳转NavDestination时指定的参数。|
|pathStack|[NavPathStack](./cj-navigation-switching-navigation.md#class-navpathstack)|是|-|当前NavDestination所处的页面栈。|
|navDestinationId|String|是|-|当前NavDestination的唯一ID，由系统自动生成，和组件通用属性id无关。|

### class NavDestinationCommonTitle

```cangjie
public class NavDestinationCommonTitle {
    public var `main`: String
    public var sub: String
    public init(
        `main`: String,
        sub: String
    )
}
```

**功能：** NavDestination通用标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var main

```cangjie
public var `main`: String
```

**功能：** 设置主标题。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

#### var sub

```cangjie
public var sub: String
```

**功能：** 设置副标题。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

#### init(String,String)

```cangjie
public init(
    `main`: String,
    sub: String
)
```

**功能：** 构造一个NavDestinationCommonTitle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|main|String|是|-|设置主标题。|
|sub|String|是|-|设置副标题。|

### enum NavDestinationMode

```cangjie
public enum NavDestinationMode {
    Standard |
    Dialog |
}
```

**功能：** 设置NavDestination类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Standard

```cangjie
Standard
```

**功能：** 标准模式的NavDestination。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Dialog

```cangjie
Dialog
```

**功能：** 默认透明，进出页面栈不影响下层NavDestination的生命周期。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20