### func edgeEffect(EdgeEffect, EdgeEffectOptions)

```cangjie
public func edgeEffect(value: EdgeEffect, options: EdgeEffectOptions): This
```

**功能：** 设置边缘滑动效果。

> **说明：**
>
> 当List组件的内容区小于一屏时，默认没有回弹效果。若要启用回弹效果，可以通过设置edgeEffect属性的options参数来实现。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[EdgeEffect](cj-common-types.md#enum-EdgeEffect)|是|-|List组件的边缘滑动效果，支持弹簧效果和阴影效果。<br/>初始值：EdgeEffect.Spring。|
|options|[EdgeEffectOptions](./cj-scroll-swipe-common.md#class-edgeeffectoptions)|是|-|组件内容大小小于组件自身时，是否开启滑动效果。设置alwaysEnabled为true会开启滑动效果，alwaysEnabled为false不开启。<br/>初始值：alwaysEnabled为false。|

### func editMode(Bool)

```cangjie
public func editMode(flag: Bool): This
```

**功能：** 设置当前List组件是否处于可编辑模式。可参考[示例3](#示例3-设置编辑模式)实现删除选中的list项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|flag|Bool|是|-|当前List组件是否处于可编辑模式。<br/>初始值：false，当前List组件不处于可编辑模式。|

### func enableScrollInteraction(Bool)

```cangjie
public func enableScrollInteraction(flag: Bool): This
```

**功能：** 设置是否支持滚动手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|flag|Bool|是|-|是否支持滚动手势。设置为true时可以通过手指或者鼠标滚动，设置为false时无法通过手指或者鼠标滚动，但不影响控制器[Scroller](./cj-scroll-swipe-scroll.md#class-scroller)的滚动接口。<br/>初始值：true。|

### func friction(Float64)

```cangjie
public func friction(value: Float64): This
```

**功能：** 设置摩擦系数，手动划动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。设置为小于等于0的值时，按初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|摩擦系数。<br/>初始值：非可穿戴设备为0.75，可穿戴设备为0.9。|

### func lanes(Int32)

```cangjie
public func lanes(value: Int32): This
```

**功能：** 设置List组件的布局列数或行数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|List组件的布局列数或行数。<br/>初始值：1。<br/>取值范围：[1, +∞)。|

### func lanes(Int32, Length)

```cangjie
public func lanes(value: Int32, gutter!: Length): This
```

**功能：** 设置List组件的布局列数或行数。gutter为列间距，当列数大于1时生效。

规则如下：

* lanes为指定的数量时，根据指定的数量与List组件的交叉轴尺寸除以列数作为列的宽度。
* ListItemGroup在多列模式下也是独占一行，ListItemGroup中的ListItem按照List组件的lanes属性设置值来布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|List组件的布局列数或行数。<br/>初始值：1。<br/>取值范围：[1, +∞)。|
|gutter|[Length](cj-common-types.md#interface-length)|是|-| **命名参数。** 列间距。<br/>初始值：1。<br/>取值范围：[1, +∞)。|