## 组件事件

### func onBackPressed(?() -> Bool)

```cangjie
public func onBackPressed(callback: ?() -> Bool): This
```

**功能：** 当与Navigation绑定的页面栈中存在内容时，此回调生效。当点击返回键时，触发该事件。返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?() -> Bool|是|-|回调函数，当点击返回键时，触发该回调。返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。初始值：{ => true }。|

### func onReady(?Callback\<NavDestinationContext, Unit>)

```cangjie
public func onReady(callback: ?Callback<NavDestinationContext, Unit>): This
```

**功能：** 当NavDestination即将构建子组件之前会触发此事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback](./cj-common-types.md#type-callbackt-v)\<[NavDestinationContext](#class-navdestinationcontext), Unit>|是|-|回调函数，即将构建子组件之前会触发此回调。初始值：{ _ => }。|

## 基础类型定义

### class NavDestinationContext

```cangjie
public class NavDestinationContext {
    public var pathInfo: NavPathInfo
    public var pathStack: NavPathStack
    public var navDestinationId: String
}
```

**功能：** NavDestination上下文信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var navDestinationId

```cangjie
public var navDestinationId: String
```

**功能：** 当前NavDestination的唯一ID，由系统自动生成，和组件通用属性id无关。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var pathInfo

```cangjie
public var pathInfo: NavPathInfo
```

**功能：** 跳转NavDestination时指定的参数。

**类型：** [NavPathInfo](./cj-navigation-switching-navigation.md#class-navpathinfo)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var pathStack

```cangjie
public var pathStack: NavPathStack
```

**功能：** 当前NavDestination所处的页面栈。

**类型：** [NavPathStack](./cj-navigation-switching-navigation.md#class-navpathstack)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

## 示例代码

NavDestination用法可参考[Navigation示例](./cj-navigation-switching-navigation.md#示例代码)。