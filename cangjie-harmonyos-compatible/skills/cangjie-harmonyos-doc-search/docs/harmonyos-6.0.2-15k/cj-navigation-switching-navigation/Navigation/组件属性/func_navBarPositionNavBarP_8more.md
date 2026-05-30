### func navBarPosition(NavBarPosition)

```cangjie
public func navBarPosition(position: NavBarPosition): This
```

**功能：** 设置导航栏位置。仅在Navigation组件分栏时生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| position |[NavBarPosition](#enum-navbarposition)|是|-|导航栏位置。<br/>初始值：NavBarPosition.Start。|

### func mode(NavigationMode)

```cangjie
public func mode(mode: NavigationMode): This
```

**功能：** 设置导航栏的显示模式。支持Stack、Split与Auto模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| mode |[NavigationMode](#enum-navigationmode)|是|-|导航栏的显示模式。<br/>初始值：NavigationMode.Auto。<br/>自适应：基于组件宽度自适应单栏和双栏。|

### func backButtonIcon(String)

```cangjie
public func backButtonIcon(icon: String): This
```

**功能：** 设置标题栏中返回键图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| icon |String|是|-|标题栏中返回键图标。|

### func backButtonIcon(PixelMap)

```cangjie
public func backButtonIcon(icon: PixelMap): This
```

**功能：** 设置标题栏中返回键图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| icon |PixelMap|是|-|标题栏中返回键图标。|

### func backButtonIcon(AppResource)

```cangjie
public func backButtonIcon(icon: AppResource): This
```

**功能：** 设置标题栏中返回键图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| icon |[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|标题栏中返回键图标。|

### func hideNavBar(Bool)

```cangjie
public func hideNavBar(isHide: Bool): This
```

**功能：** 设置是否隐藏导航栏。设置为true时，隐藏Navigation的导航栏，包括标题栏、内容区和工具栏。如果此时路由栈中存在NavDestination页面，则直接显示栈顶NavDestination页面，反之显示空白。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| isHide |Bool|是|-|是否隐藏导航栏。|

### func navDestination((String) -> Unit)

```cangjie
public func navDestination(builder: (String) -> Unit): This
```

**功能：** 创建NavDestination组件。使用builder函数，基于name构造NavDestination组件。builder下只能有一个根节点。builder中允许在NavDestination组件外包含一层自定义组件，但自定义组件不允许设置属性和事件，否则仅显示空白。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|(String)->Unit|是|-|NavDestination组件。参数：NavDestination页面名称。|

### func navBarWidthRange((Length, Length))

```cangjie
public func navBarWidthRange(value: (Length, Length)): This
```

**功能：** 设置导航栏最小和最大宽度（双栏模式下生效）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|(Length, Length)|是|-|导航栏最小和最大宽度。<br/>初始值：最小初始值240，最大初始值为组件宽度的40%，且不大于432，如果只设置一个值，则未设置的值按照初始值计算。<br/>单位：vp。 |