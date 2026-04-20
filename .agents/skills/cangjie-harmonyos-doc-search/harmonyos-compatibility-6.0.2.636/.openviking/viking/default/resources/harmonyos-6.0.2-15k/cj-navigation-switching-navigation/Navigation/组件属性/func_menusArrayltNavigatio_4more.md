### func menus(Array&lt;NavigationMenuItem&gt;)

```cangjie
public func menus(array: Array<NavigationMenuItem>): This
```

> **说明：**
>
> 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**功能：** 设置页面右上角菜单。不设置时不显示菜单项。使用Array<[NavigationMenuItem](#class-navigationmenuitem)>写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| array |Array<[NavigationMenuItem](#class-navigationmenuitem)>|是|-|页面右上角菜单。|

### func menus(() -> Unit)

```cangjie
public func menus(builder: () -> Unit): This
```

> **说明：**
>
> 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**功能：** 设置页面右上角菜单。不设置时不显示菜单项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| builder |() -> Unit|是|-|页面右上角菜单。|

### func titleMode(NavigationTitleMode)

```cangjie
public func titleMode(titleMode: NavigationTitleMode): This
```

**功能：** 设置页面标题栏显示模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| titleMode |[NavigationTitleMode](#enum-navigationtitlemode)|是|-|页面标题栏显示模式。|

### func toolbarConfiguration(Array\<ToolBarItem>, NavigationToolbarOptions)

```cangjie
public func toolbarConfiguration(array: Array<ToolBarItem>, options!: ?NavigationToolbarOptions = None): This
```

> **说明：**
>
> 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**功能：** 设置工具栏内容。不设置时不显示工具栏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| array |Array<[ToolBarItem](#class-toolbaritem)>|是|-|工具栏内容，使用Array&lt;[ToolbarItem](#class-toolbaritem)&gt;写法设置的工具栏有如下特性：<br/>工具栏所有选项均分底部工具栏，在每个均分内容区布局文本和图标。<br/>文本超长时，若工具栏选项个数小于5个，优先拓展选项的宽度，最大宽度与屏幕等宽，其次逐级缩小，缩小之后换行，最后截断。<br/>竖屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。横屏时，如果为[Split](#enum-navigationmode)模式，仍按照竖屏规则显示，如果为[Stack](#enum-navigationmode)模式需配合menus属性的Array&lt;[NavigationMenuItem](#class-navigationmenuitem)&gt;使用，底部工具栏会自动隐藏，同时底部工具栏所有选项移动至页面右上角菜单。|
| options |?[NavigationToolbarOptions](#class-navigationtoolbaroptions)|否|-| 工具栏选项。|