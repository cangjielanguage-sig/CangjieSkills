### func alignListItem(ListItemAlign)

```cangjie
public func alignListItem(value: ListItemAlign): This
```

**功能：** 设置List交叉轴方向宽度大于ListItem交叉轴宽度 * lanes时，ListItem在List交叉轴方向的布局方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ListItemAlign](cj-common-types.md#enum-listitemalign)|是|-|交叉轴方向的布局方式。<br>初始值：ListItemAlign.Start。|

### func cachedCount(Int32)

```cangjie
public func cachedCount(value: Int32): This
```

**功能：** 设置列表中ListItem/ListItemGroup的预加载数量，懒加载场景只会预加载List显示区域外cachedCount的内容，非懒加载场景会全部加载。懒加载、非懒加载都只布局List显示区域+List显示区域外cachedCount的内容。

List设置cachedCount后，显示区域外上下各会预加载并布局cachedCount行ListItem。计算ListItem行数时，会计算ListItemGroup内部的ListItem行数。如果ListItemGroup内没有ListItem，则整个ListItemGroup算一行。

List下嵌套使用LazyForEach，并且LazyForEach下嵌套使用ListItemGroup时，LazyForEach会在List显示区域外上下各会创建cachedCount个ListItemGroup。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|列表中ListItem/ListItemGroup的预加载数量。<br/>初始值：根据屏幕内显示的节点个数设置，最大值为16。<br/>取值范围：[0, +∞)。|

### func chainAnimation(Bool)

```cangjie
public func chainAnimation(flag: Bool): This
```

**功能：** 设置当前List是否启用链式联动动效。

> **说明：**
>
> * 链式联动效果是指在手指划动过程中，手指拖动的ListItem是主动对象，相邻的ListItem为从动对象，主动对象驱动从动对象联动，驱动效果遵循弹簧物理动效。
> * 链式动效的驱动效果体现在ListItem之间的间距上。静止状态下的间距可以通过List组件space参数设置，如果不设置space参数并且启用了链式动效，该间距初始值：20.vp。
> * 链式动效启用后，List的分割线不显示。
> * 链式动效生效的前提是List处于单列模式并且边缘效果为EdgeEffect.Spring类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|flag|Bool|是|-|是否启用链式联动动效。<br>初始值：false，不启用链式联动。true，启用链式联动。|

### func contentEndOffset(Float64)

```cangjie
public func contentEndOffset(endOffset: Float64): This
```

**功能：** 设置内容区末尾偏移量。列表滚动到末尾位置时，列表内容与列表显示区域边界保留指定距离。

contentStartOffset + contentEndOffset超过List内容区长度后contentStartOffset和contentEndOffset会置0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|endOffset|Float64|是|-|内容区末尾偏移量。<br/>初始值：0.0。<br/>单位：vp。<br/>**说明：**<br/>设置为负数时，按初始值处理。|

### func contentEndOffset(Int64)

```cangjie
public func contentEndOffset(endOffset: Int64): This
```

**功能：** 设置内容区末尾偏移量。列表滚动到末尾位置时，列表内容与列表显示区域边界保留指定距离。

contentStartOffset + contentEndOffset超过List内容区长度后contentStartOffset和contentEndOffset会置0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|endOffset|Int64|是|-|内容区末尾偏移量。<br/>初始值：0。<br/>单位：vp。<br/>**说明：**<br/>设置为负数时，按初始值处理。|