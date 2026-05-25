### func toolbarConfiguration(() -> Unit, NavigationToolbarOptions)

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
| builder |() -> Unit|是|-|工具栏内容，<br/>用户自定义工具栏选项。|
| options |?[NavigationToolbarOptions](#class-navigationtoolbaroptions)|否|-| 工具栏选项。|

### func hideToolBar(Bool)

```cangjie
public func hideToolBar(isHide: Bool): This
```

**功能：** 设置是否隐藏工具栏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| isHide |Bool|是|-|是否隐藏工具栏。<br/>初始值：false<br/>true: 隐藏工具栏。<br/>false: 显示工具栏。|

### func hideToolBar(Bool, Bool)

```cangjie
public func hideToolBar(isHide: Bool, animated!: Bool): This
```

**功能：** 设置是否隐藏工具栏。新增工具栏显隐时是否使用动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| isHide |Bool|是|-|是否隐藏工具栏。<br/>初始值：false。<br/>true: 隐藏工具栏。<br/>false: 显示工具栏。|
| animated |Bool|是|-|是否使用动画显隐工具栏。<br/>初始值：false。<br/>true: 使用动画显示隐藏工具栏。<br/>false: 不使用动画显示隐藏工具栏。|

### func hideTitleBar(Bool)

```cangjie
public func hideTitleBar(isHide: Bool): This
```

**功能：** 设置是否隐藏标题栏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| isHide |Bool|是|-|是否隐藏标题栏。<br/>初始值：false。<br/>true: 隐藏标题栏。<br/>false: 显示标题栏。|

### func hideTitleBar(Bool, Bool)

```cangjie
public func hideTitleBar(isHide: Bool, animated!: Bool): This
```

**功能：** 设置是否隐藏标题栏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| isHide |Bool|是|-|是否隐藏标题栏。<br/>初始值：false。<br/>true: 隐藏标题栏。<br/>false: 显示标题栏。|
| animated |Bool|是|-|是否使用动画显隐标题栏。<br/>初始值：false。<br/>true: 使用动画显示隐藏标题栏。<br/>false: 不使用动画显示隐藏标题栏。|

### func hideBackButton(Bool)

```cangjie
public func hideBackButton(isHide: Bool): This
```

**功能：** 设置是否隐藏标题栏中的返回键。返回键仅针对[titleMode](#enum-navigationtitlemode)为NavigationTitleMode.Mini时才生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| isHide |Bool|是|-|是否隐藏标题栏中的返回键。<br/>初始值：false。<br/>true: 隐藏返回键。<br/>false: 显示返回键。|

### func navBarWidth(Length)

```cangjie
public func navBarWidth(width: Length): This
```

**功能：** 设置导航栏宽度。仅在Navigation组件分栏时生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| width |[Length](./cj-common-types.md#interface-length)|是|-|导航栏宽度。<br/>初始值：240.vp。<br/>undefined：行为不做处理，导航栏宽度与初始值值保持一致。|