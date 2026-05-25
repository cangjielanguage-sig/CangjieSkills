### func columnsTemplate(String)

```cangjie
public func columnsTemplate(value: String): This
```

**功能：** 设置当前网格布局列的数量、固定列宽或最小列宽值，不设置时默认1列。

例如,&nbsp;'1fr&nbsp;1fr&nbsp;2fr'&nbsp;是将父组件分3列，将父组件允许的宽分为4等份，第一列占1份，第二列占1份，第三列占2份。

columnsTemplate('repeat(auto-fit, track-size)')是设置最小列宽值为track-size，自动计算列数和实际列宽。

columnsTemplate('repeat(auto-fill, track-size)')是设置固定列宽值为track-size，自动计算列数。

columnsTemplate('repeat(auto-stretch, track-size)')是设置固定列宽值为track-size，使用columnsGap为最小列间距，自动计算列数和实际列间距。

其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为列宽，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包括一个有效列宽。<br/>
auto-stretch模式只支持track-size为一个有效列宽值，并且track-size只支持px、vp和有效数字，不支持%。

使用效果可以参考[示例3](#示例3grid拖拽场景)。

设置为'0fr'时，该列的列宽为0，不显示GridItem。设置为其他非法值时，GridItem显示为固定1列。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|当前网格布局列的数量或最小列宽值。|

### func edgeEffect(EdgeEffect)

```cangjie
public func edgeEffect(value: EdgeEffect): This
```

**功能：** 设置边缘滑动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[EdgeEffect](cj-common-types.md#enum-edgeeffect)|是|-|Grid组件的边缘滑动效果，支持弹簧效果和阴影效果。<br>初始值：EdgeEffect.None|

### func edgeEffect(EdgeEffect, EdgeEffectOptions)

```cangjie
public func edgeEffect(value: EdgeEffect, options: EdgeEffectOptions): This
```

**功能：** 设置边缘滑动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[EdgeEffect](cj-common-types.md#enum-edgeeffect)|是|-|Grid组件的边缘滑动效果，支持弹簧效果和阴影效果。<br>初始值：EdgeEffect.None|
|options|[EdgeEffectOptions](cj-scroll-swipe-common.md#class-edgeeffectoptions)|是|-|组件内容大小小于组件自身时，是否开启滑动效果。设置为{ alwaysEnabled: true }会开启滑动效果，{ alwaysEnabled: false }不开启。<br>初始值：{ alwaysEnabled: false }|

### func editMode(Bool)

```cangjie
public func editMode(isEditMode: Bool): This
```

**功能：** 设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部[GridItem](./cj-scroll-swipe-griditem.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isEditMode|Bool|是|-|Grid是否进入编辑模式。<br/>初始值：false，当前Grid组件不处于可编辑模式。|

### func enableScrollInteraction(Bool)

```cangjie
public func enableScrollInteraction(isEnable: Bool): This
```

**功能：** 设置是否支持滚动手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isEnable|Bool|是|-|是否支持滚动手势，当设置为false时，无法通过手指或者鼠标滚动，但不影响控制器的滚动接口。<br/>初始值：true|