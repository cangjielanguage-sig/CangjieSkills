### class NavigationMenuItem

```cangjie
public class NavigationMenuItem {
    public var value: String = ""
    public var icon: String = ""
    public var isEnable: Bool = true
    public var action:() -> Unit = { => }
    public init(
        value!: String,
        icon!: ?String = None,
        isEnable!: ?Bool = None,
        action!: Option<() -> Unit> = None
    )
    public init(
        value!: AppResource,
        icon!: ?AppResource = None,
        isEnable!: ?Bool = None,
        action!: Option<() -> Unit> = None
    )
}
```

**功能：** 表示Navigation菜单选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var action

```cangjie
public var action: () -> Unit = {=>}
```

**功能：** 表示当前选项被选中的事件回调。

**类型：** () -> Unit

**读写能力：** 可读写

**起始版本：** 20

#### var icon

```cangjie
public var icon: String = ""
```

**功能：** 菜单栏单个选项的图标资源路径。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

#### var isEnable

```cangjie
public var isEnable: Bool = true
```

**功能：** 使能状态，默认使能（false未使能，true使能）。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

#### var value

```cangjie
public var value: String = ""
```

**功能：** 显示菜单栏单个选项的文本。不显示菜单栏单个选项的文本。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

#### init(String, ?String, ?Bool, Option\<() -> Unit>)

```cangjie
public init(
    value!: String,
    icon!: ?String = None,
    isEnable!: ?Bool = None,
    action!: Option<() -> Unit> = None
)
```

**功能：** 创建NavigationMenuItem。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|菜单栏单个选项的文本。|
|icon|?String|否|None| 菜单栏单个选项的图标资源路径。|
|isEnable|?Bool|否|None| 使能状态，默认使能（false未使能，true使能）。|
|action|()->Unit|否|None|当前选项被选中的事件回调。|

#### init(AppResource, ?AppResource, ?Bool, Option\<() -> Unit>)

```cangjie
public init(
    value!: AppResource,
    icon!: ?AppResource = None,
    isEnable!: ?Bool = None,
    action!: Option<() -> Unit> = None
)
```

**功能：** 创建NavigationMenuItem。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|菜单栏单个选项的文本。|
|icon|?[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|否|None|菜单栏单个选项的图标资源路径。|
|isEnable|?Bool|否|None|使能状态，默认使能（false未使能，true使能）。|
|action|?<()->Unit>|否|None|当前选项被选中的事件回调。|