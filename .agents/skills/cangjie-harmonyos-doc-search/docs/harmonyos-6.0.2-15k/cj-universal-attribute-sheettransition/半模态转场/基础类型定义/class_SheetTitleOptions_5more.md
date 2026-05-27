### class SheetTitleOptions

```cangjie
public class SheetTitleOptions {
    public init(title!: String, subtitle!: Option<String>)
}
```

**功能：** 半模态面板的标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(String, Option\<String>)

```cangjie
public init(title!: String, subtitle!: Option<String>)
```

**功能：** 半模态面板的标题的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| title | String | 是 | \-  | **命名参数。**  半模态面板的主标题。|
| subtitle | Option\<String> | 否 | \- | **命名参数。**  半模态面板的副标题。|

### class SpringBackAction

```cangjie
public class SpringBackAction {
    public SpringBackAction()
}
```

**功能：** 控制半模态关闭前的回弹类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SpringBackAction()

```cangjie
public SpringBackAction()
```

**功能：** 控制半模态关闭前的回弹类型的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func springBack()

```cangjie
public func springBack()
```

**功能：** 半模态页面关闭前控制回弹函数，开发者需要半模态回弹时调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum ScrollSizeMode

```cangjie
public enum ScrollSizeMode {
    | FOLLOW_DETENT
    | CONTINUOUS
}
```

**功能：** 设置半模态面板滑动时，内容区域刷新时机。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### FOLLOW_DETENT

```cangjie
FOLLOW_DETENT
```

**功能：** 设置半模态面板跟手滑动结束后更新内容显示区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### CONTINUOUS

```cangjie
CONTINUOUS
```

**功能：** 设置半模态面板在滑动过程中持续更新内容显示区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum SheetMode

```cangjie
public enum SheetMode {
    | OVERLAY
    | EMBEDDED
}
```

**功能：** 设置半模态页面的显示层级。

**起始版本：** 19

#### OVERLAY

```cangjie
OVERLAY
```

**功能：** 设置半模态面板在当前UIContext内顶层显示，在所有页面之上。和弹窗类组件显示在一个层级。

**起始版本：** 19

#### EMBEDDED

```cangjie
EMBEDDED
```

**功能：** 设置半模态面板在当前页面内的顶层显示。

**起始版本：** 19

> **说明：**
>
> 目前只支持挂载在Page或者NavDestination节点上，若有NavDestination优先挂载在NavDestination上。只支持在这两种页面内顶层显示。<br>该模式下新起的页面可以覆盖在半模态弹窗上，页面返回后该半模态依旧存在，半模态面板内容不丢失。<br>该模式下需确保目标页面节点如Page节点已挂载上树，再拉起半模态，否则半模态将无法挂载到对应的页面节点内。

### enum SheetSize

```cangjie
public enum SheetSize {
    | MEDIUM
    | LARGE
    | FIT_CONTENT
}
```

**功能：** 设置半模态页面的切换高度档位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### MEDIUM

```cangjie
MEDIUM
```

**功能：** 指定半模态高度为屏幕高度一半。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### LARGE

```cangjie
LARGE
```

**功能：** 指定半模态高度几乎为屏幕高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### FIT_CONTENT

```cangjie
FIT_CONTENT
```

**功能：** 指定半模态高度为适应内容的高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12