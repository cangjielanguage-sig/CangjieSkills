### func barOverlap(Bool)

```cangjie
public func barOverlap(isOverlap: Bool): This
```

**功能：** 设置TabBar是否背后变模糊并叠加在TabContent之上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isOverlap|Bool|是|-|TabBar是否背后变模糊并叠加在TabContent之上。当barOverlap设置为true时，TabBar背后变模糊并叠加在TabContent之上，并且TabBar默认模糊材质的BlurStyle值修改为'BlurStyle.COMPONENT_THICK'。当barOverlap设置为false时，无模糊和叠加效果。<br> 初始值：false|

### func barPosition(BarPosition)

```cangjie
public func barPosition(barPosition: BarPosition): This
```

**功能：** 设置Tabs的页签位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|barPosition|[BarPosition](#enum-barposition)|是|-|设置Tabs的页签位置。<br> 初始值：BarPosition.Start|

### func barWidth(Length)

```cangjie
public func barWidth(width: Length): This
```

**功能：** 设置TabBar的宽度值。设置为小于0或大于Tabs宽度值时，按初始值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](cj-common-types.md#interface-length)|是|-|TabBar 的宽度值。<br>初始值：<br> 未设置[SubTabBarStyle](cj-navigation-switching-tabcontent.md#class-subtabbarstyle)和[BottomTabBarStyle](cj-navigation-switching-tabcontent.md#class-bottomtabbarstyle)的TabBar且vertical属性为false时，初始值为Tabs的宽度。<br> 未设置SubTabBarStyle和BottomTabBarStyle的TabBar且vertical属性为true时，初始值为56.vp。<br>设置SubTabBarStyle样式且vertical属性为false时，初始值为Tabs的宽度。<br> 设置SubTabBarStyle样式且vertical属性为true时，初始值为56.vp。<br> 设置BottomTabBarStyle样式且vertical属性为true时，初始值为96.vp。<br> 设置BottomTabBarStyle样式且vertical属性为false时，初始值为Tabs的宽度。|

### func divider(?DividerStyle)

```cangjie
public func divider(divider: ?DividerStyle): This
```

**功能：** 设置区分TabBar和TabContent的分割线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|divider|?[DividerStyle](#class-dividerstyle)|是|-|分割线样式，默认不显示分割线。<br>DividerStyle：分割线的样式；<br>Option.None：不显示分割线。|

### func edgeEffect(EdgeEffect)

```cangjie
public func edgeEffect(edgeEffect: EdgeEffect): This
```

**功能：** 设置边缘回弹效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|edgeEffect|[EdgeEffect](cj-common-types.md#enum-edgeeffect)|是|-|边缘滑动效果。<br> 初始值：EdgeEffect.Spring|

### func fadingEdge(Bool)

```cangjie
public func fadingEdge(isFading: Bool): This
```

**功能：** 设置页签超过容器宽度时是否渐隐消失。建议配合barBackgroundColor属性一起使用，如果barBackgroundColor属性没有定义，会默认显示页签末端为白色的渐隐效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isFading|Bool|是|-|页签超过容器宽度时是否渐隐消失。<br> 初始值：true，页签超过容器宽度时会渐隐消失。设置为false时，页签超过容器宽度直接截断显示，不产生任何渐变效果‌。|