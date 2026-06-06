### class NavigationCommonTitle

```cangjie
public class NavigationCommonTitle {
    public var `main`: String
    public var sub: String
    public init(`main`: String, sub: String)
}
```

**功能：** 表示Navigaiton主副标题类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var main

```cangjie
public var `main`: String,
```

**功能：** 设置主标题

**类型：** String

**读写能力：** 可读

**起始版本：** 20

#### var sub

```cangjie
public var sub: String
```

**功能：** 设置副标题

**类型：** String

**读写能力：** 可读

**起始版本：** 20

#### init(String, String)

```cangjie
public init(`main`: String, sub: String)
```

**功能：** 创建Navigaiton主副标题类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

### enum NavigationMode

```cangjie
public enum NavigationMode {
    | Stack
    | Split
    | Auto
}
```

**功能：** 导航栏显示模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Auto

```cangjie
Auto
```

**功能：** 窗口宽度>=600.vp时，采用Split模式显示；窗口宽度<600.vp时，采用Stack模式显示，600.vp等于minNavBarWidth(240.vp) + minContentWidth (360.vp)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Split

```cangjie
Split
```

**功能：** 导航栏与内容区分两栏显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Stack

```cangjie
Stack
```

**功能：** 导航栏与内容区独立显示，相当于两个页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum ToolbarItemStatus

```cangjie
public enum ToolbarItemStatus {
    | Normal
    | Disabled
    | Active
}
```

**功能：** 工具栏单个选项状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Normal

```cangjie
Normal
```

**功能：** 设置工具栏单个选项为Normal态，该选项显示默认样式，可以触发Hover，Press，Focus事件并显示对应的多态样式。

**起始版本：** 20

#### Disabled

```cangjie
Disabled
```

**功能：** 设置工具栏单个选项为Disabled态， 该选项显示Disabled态样式，并且不可交互。

**起始版本：** 20

#### Active

```cangjie
Active
```

**功能：** 设置工具栏单个选项为Active态， 该选项通过点击事件可以将icon图标更新为activeIcon对应的图片资源。

**起始版本：** 20

### enum NavBarPosition

```cangjie
public enum NavBarPosition {
    | Start
    | End
}
```

**功能：** NavBar位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Start

```cangjie
ACTIVE
```

**功能：** 双栏显示时，主列在主轴方向首部。

**起始版本：** 20

#### End

```cangjie
ACTIVE
```

**功能：** 双栏显示时，主列在主轴方向尾部。

**起始版本：** 20

### enum LaunchMode

```cangjie
public enum LaunchMode {
    | Standard
    | MoveToTopSingleTon
    | PopToSingleTon
    | NewInstance
}
```

**功能：** 路由栈操作模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Standard

```cangjie
Standard
```

**功能：** 系统默认的栈操作模式。push操作会将指定的NavDestination入栈；replace操作会将当前栈顶NavDestination替换。

**起始版本：** 20

#### MoveToTopSingleTon

```cangjie
MoveToTopSingleTon
```

**功能：** 从栈底向栈顶查找，如果指定的名称已经存在，则将对应的NavDestination页面移到栈顶（replace操作会将最后的栈顶替换成指定的NavDestination），否则行为和Standard一致。

**起始版本：** 20

#### PopToSingleTon

```cangjie
PopToSingleTon
```

**功能：** 从栈底向栈顶查找，如果指定的名称已经存在，则将其上方的NavDestination页面全部移除（replace操作会将最后的栈顶替换成指定的NavDestination），否则行为和Standard一致。

**起始版本：** 20

#### NewInstance

```cangjie
NewInstance
```

**功能：** 创建新的NavDestination实例。与Standard模式相比，该方法不会复用栈中同名实例。

**起始版本：** 20