### func cachedCount(Int32, Bool)

```cangjie
public func cachedCount(value: Int32, show: Bool): This
```

**功能：** 设置预加载的FlowItem数量，并配置是否显示预加载节点。

配合[裁剪](./cj-universal-attribute-shapclip.md)或[内容裁剪](./cj-scroll-swipe-common.md#func-clipcontentcontentclipmode)属性可以显示出预加载节点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|预加载的FlowItem的数量。<br/>初始值：根据屏幕内显示的节点个数设置，最大值为16。<br/>取值范围：[0, +∞)，设置为小于0的值时，按1处理。|
|show|Bool|是|-|被预加载的FlowItem是否需要显示。设置为true时显示预加载的FlowItem，设置为false时不显示预加载的FlowItem。<br/>初始值值：false。|

### func columnsGap(Length)

```cangjie
public func columnsGap(value: Length): This
```

**功能：** 设置列与列的间距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|列与列的间距。<br/>初始值：0。<br/>取值范围：[0, +∞)。|

### func columnsTemplate(String)

```cangjie
public func columnsTemplate(value: String): This
```

**功能：** 设置当前瀑布流组件布局列的数量，不设置时默认1列。

例如， '1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第一列占1份，第二列占1份，第三列占2份。

可使用columnsTemplate('repeat(auto-fill,track-size)')根据给定的列宽track-size自动计算列数，其中repeat、auto-fill为关键字，track-size为可设置的宽度，支持的单位包括px、vp、%或有效数字，默认单位为vp，使用方法参见示例2。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|当前瀑布流组件布局列的数量。<br/>初始值："1fr"。|

### func enableScrollInteraction(Bool)

```cangjie
public func enableScrollInteraction(value: Bool): This
```

**功能：** 设置是否支持滚动手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否支持滚动手势。设置为true时可以通过手指或者鼠标滚动，设置为false时无法通过手指或者鼠标滚动，但不影响控制器[Scroller](./cj-scroll-swipe-scroll.md#class-scroller)的滚动接口。<br/>初始值：true。|

### func friction(Float64)

```cangjie
public func friction(value: Float64): This
```

**功能：** 设置摩擦系数，手动划动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|摩擦系数。<br/>初始值：非可穿戴设备为0.75，可穿戴设备为0.9。<br/>取值范围：(0, +∞)，设置为小于等于0的值时，按初始值处理。|

### func friction(Int32)

```cangjie
public func friction(value: Int32): This
```

**功能：** 设置摩擦系数，手动划动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|摩擦系数。<br/>初始值：非可穿戴设备为0.75，可穿戴设备为0.9。<br/>取值范围：(0, +∞)，设置为小于等于0的值时，按初始值处理。|