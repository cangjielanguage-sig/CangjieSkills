### func autoHide(Bool)

```cangjie
public func autoHide(value: Bool): This
```

**功能：** 设置当侧边栏拖拽到小于最小宽度后，是否自动隐藏。

> **说明：**
>
> - 受minSideBarWidth属性方法影响，当minSideBarWidth属性方法未设置值时使用初始值。
> - 拖拽过程中判断是否要自动隐藏。小于最小宽度时需要阻尼效果触发隐藏（越界一段距离）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|侧边栏拖拽到小于最小宽度后，是否自动隐藏。<br>true：会自动隐藏。<br>false：不会自动隐藏。<br>初始值：true。|

### func controlButton(ButtonStyle)

```cangjie
public func controlButton(value: ButtonStyle): This
```

**功能：** 设置侧边栏控制按钮的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ButtonStyle](#class-buttonstyle)|是|-|侧边栏控制按钮的属性。|

### func divider(?SideBarDividerStyle)

```cangjie
public func divider(value!: ?SideBarDividerStyle = None): This
```

**功能：** 设置分割线的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[SideBarDividerStyle](#class-sidebardividerstyle)|否|None| **命名参数。** 分割线的样式，默认显示分割线。输入为None时行为不做处理，分割线样式与默认保持一致。|

### func maxSideBarWidth(Length)

```cangjie
public func maxSideBarWidth(value: Length): This
```

**功能：** 设置侧边栏最大宽度。

> **说明：**
>
> - 设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过使用侧边栏容器本身宽度。
> - maxSideBarWidth优先于侧边栏子组件maxWidth，maxSideBarWidth未设置时默认值优先级高于侧边栏子组件maxWidth。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|设置侧边栏最大宽度。<br>初始值：280.vp。<br>单位：vp。|

### func minContentWidth(Length)

```cangjie
public func minContentWidth(value: Length): This
```

**功能：** 设置SideBarContainer组件内容区可显示的最小宽度。

> **说明：**
>
> - 当最小宽度设置为小于0，内容区显示的最小宽度为360.vp；未设置该属性时，组件内容区的可缩小到0。
> - Embed场景下，增大组件尺寸时仅增大内容区的尺寸。
> - 缩小组件尺寸时，先缩小内容区的尺寸至minContentWidth。继续缩小组件尺寸时，保持内容区宽度minContentWidth不变，优先缩小侧边栏的尺寸。当缩小侧边栏的尺寸至minSideBarWidth后，继续缩小组件尺寸时：
>
>     - 如果autoHide属性为false，则会保持侧边栏宽度minSideBarWidth和内容区宽度minContentWidth不变，但内容区会被截断显示；
>     - 如果autoHide属性为true，则会优先隐藏侧边栏，然后继续缩小至内容区宽度minContentWidth后，内容区宽度保持不变，但内容区会被截断显示。
>
> - minContentWidth优先于侧边栏的maxSideBarWidth与sideBarWidth属性，minContentWidth未设置时，默认值优先级低于设置的minSideBarWidth与maxSideBarWidth属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|SideBarContainer组件内容区可显示的最小宽度。<br>初始值：360.vp。<br>单位：vp。|