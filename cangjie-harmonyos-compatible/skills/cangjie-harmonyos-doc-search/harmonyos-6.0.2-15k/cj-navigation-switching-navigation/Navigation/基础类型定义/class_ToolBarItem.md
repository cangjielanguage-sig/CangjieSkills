### class ToolBarItem

```cangjie
public class ToolBarItem {
    public var value: String = ""
    public var icon: String = ""
    public var action:() -> Unit = { => }
    public var status: ToolbarItemStatus = ToolbarItemStatus.NORMAL
    public var activeIcon: String = ""
    public init(
        value!: String,
        icon!: ?String = None,
        action!: ?() -> Unit = None,
        status!: ?ToolbarItemStatus = None,
        activeIcon!: ?String = None
    )
    public init(
        value!: AppResource,
        icon!: ?AppResource = None,
        action!: ?() -> Unit = None,
        status!: ?ToolbarItemStatus = None,
        activeIcon!: ?AppResource = None
    )
}
```

**功能：** 设置工具栏选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var action

```cangjie
public var action: () -> Unit = {=>}
```

**功能：** 当前选项被选中的事件回调。

**类型：** ()->Unit

**读写能力：** 可读写

**起始版本：** 20

#### var activeIcon

```cangjie
public var activeIcon: String = ""
```

**功能：** 工具栏单个选项处于ACTIVE态时的图标资源路径。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

#### var icon

```cangjie
public var icon: String = ""
```

**功能：** 工具栏单个选项的图标资源路径。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

#### var status

```cangjie
public var status: ToolbarItemStatus = ToolbarItemStatus.NORMAL
```

**功能：** 设置工具栏单个选项的状态。初始值：ToolbarItemStatus.NORMAL

**类型：** [ToolbarItemStatus](#enum-toolbaritemstatus)

**读写能力：** 可读写

**起始版本：** 20

#### var value

```cangjie
public var value: String = ""
```

**功能：** 工具栏单个选项的显示文本。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

#### init(String, ?String, ?() -> Unit, ?ToolbarItemStatus, ?String)

```cangjie
public init(
    value!: String,
    icon!: ?String = None,
    action!: ?() -> Unit = None,
    status!: ?ToolbarItemStatus = None,
    activeIcon!: ?String = None
)
```

**功能：** 创建ToolBarItem。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|工具栏单个选项的显示文本。|
|icon|?String|否|None|工具栏单个选项的图标资源路径。|
|action|?()->Unit|否|None|当前选项被选中的事件回调。|
|status|?[ToolbarItemStatus](#enum-toolbaritemstatus)|否|None|工具栏单个选项的状态。|
|activeIcon|?String|否|None|工具栏单个选项处于ACTIVE态时的图标资源路径。|

#### init(AppResource, ?AppResource, ?() -> Unit, ?ToolbarItemStatus, ?AppResource)

```cangjie
public init(
    value!: AppResource,
    icon!: ?AppResource = None,
    action!: ?() -> Unit = None,
    status!: ?ToolbarItemStatus = None,
    activeIcon!: ?AppResource = None
)
```

**功能：** 创建ToolBarItem。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|工具栏单个选项的显示文本。|
|icon|?[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|否|None|工具栏单个选项的图标资源路径。|
|action|?()->Unit|否|None|当前选项被选中的事件回调。|
|status|?[ToolbarItemStatus](#enum-toolbaritemstatus)|否|None|工具栏单个选项的状态。|
|activeIcon|?[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|否|None|工具栏单个选项处于ACTIVE态时的图标资源路径。|