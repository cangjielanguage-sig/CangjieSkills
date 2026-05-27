### func minContentWidth(Length)

```cangjie
public func minContentWidth(min: Length): This
```

**功能：** 设置导航栏内容区最小宽度（双栏模式下生效）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|min|Length|是|-|导航栏内容区最小宽度。<br/>初始值：360.vp。|

> **说明：**
>
> - 仅设置navBarWidth，不支持Navigation分割线拖拽。
> - navBarWidthRange指定分割线可以拖拽范围。如果不设置值，则按照默认值处理。拖拽范围需要满足navBarWidthRange设置的范围和minContentWidth限制。
> - Navigation显示范围缩小：a. 缩小内容区大小。如果不设置minContentWidth属性，则可以缩小内容区至0，否则最小缩小至minContentWidth。b. 缩小导航栏大小，缩小时需要满足导航栏宽度大于navBarRange的下限。c. 对显示内容进行裁切。

### func ignoreLayoutSafeArea(Array\<LayoutSafeAreaType>, Array\<LayoutSafeAreaEdge>)

```cangjie
public func ignoreLayoutSafeArea(types!: ?Array<LayoutSafeAreaType> = None, edges!: ?Array<LayoutSafeAreaEdge> = None): This
```

**功能：** 控制组件的布局，使其扩展到非安全区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| types  | Array<[LayoutSafeAreaType](./cj-common-types.md#enum-layoutsafeareatype)> | 否 | None | 配置扩展安全区域的类型。<br />初始值: <br />LayoutSafeAreaType.SYSTEM |
| edges  | Array<[LayoutSafeAreaEdge](./cj-common-types.md#enum-layoutsafeareaedge)> | 否 | None | 配置扩展安全区域的方向。<br /> 初始值: <br />LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM。|

> **说明：**
>
> - 组件设置LayoutSafeArea之后生效的条件为:
> - 设置LayoutSafeAreaType.SYSTEM时，组件的边界与非安全区域重合时组件能够延伸到非安全区域下。例如：设备顶部状态栏高度100，组件在屏幕中纵向方位的绝对偏移需要在0到100之间。
> - 若组件延伸到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。

### func systemBarStyle(ResourceColor)

```cangjie
public func systemBarStyle(color: ResourceColor): This
```

**功能：** 当Navigation中显示Navigation首页时，设置对应系统状态栏的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| color  | [ResourceColor](./cj-common-types.md#interface-resourcecolor) | 是 | - | 系统状态栏样式。 |

> **使用说明：**
>
> - 不建议混合使用systemBarStyle属性和window设置状态栏样式的相关接口，例如：[setWindowSystemBarProperties](./cj-apis-window.md#func-setwindowsystembarpropertiessystembarproperties)。
> - 初次设置Navigation/NavDestination的systemBarStyle属性时，会备份当前状态栏样式用于后续的恢复场景。
> - Navigation总是以首页（页面栈内没有NavDestination时）或者栈顶NavDestination设置的状态栏样式为准。
> - Navigation首页或者任何栈顶NavDestination页面，如果设置了有效的systemBarStyle，则会使用设置的样式，反之如果之前已经备份了样式，则使用备份的样式，否则不做任何处理。
> - [Split](#enum-navigationmode)模式下的Navigation，如果内容区没有NavDestination，则遵从Navigation首页的设置，反之则遵从栈顶NavDestination的设置。
> - 仅支持在主窗口的主页面中使用systemBarStyle设置状态栏样式。
> - 仅当Navigation占满整个页面时，设置的样式才会生效，当Navigation没有占满整个页面时，如果有备份的样式，则恢复备份的样式。
> - 当页面设置不同样式时，在页面转场开始时生效。
> - 非全屏窗口下，Navigation/NavDestination设置的状态栏不生效。