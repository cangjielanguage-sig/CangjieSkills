### func initialOffset(Length, Length)

```cangjie
public func initialOffset(xOffset!: Length = 0.vp, yOffset!: Length = 0.vp): This
```

**功能：** 设置初始滚动偏移量。只在首次布局时生效，后续动态修改该属性值不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xOffset|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 水平滚动偏移。<br>**说明：**<br>当输入的大小为百分比时，初始滚动偏移量为Scroll组件主轴方向大小与百分比数值之积。|
|yOffset|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 垂直滚动偏移。<br>**说明：**<br>当输入的大小为百分比时，初始滚动偏移量为Scroll组件主轴方向大小与百分比数值之积。|

### func nestedScroll(NestedScrollOptions)

```cangjie
public func nestedScroll(value: NestedScrollOptions): This
```

**功能：** 设置向前和向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[NestedScrollOptions](./cj-scroll-swipe-common.md#class-nestedscrolloptions)|是|-|嵌套滚动选项。<br>初始值：scrollForward参数初始为NestedScrollMode.SELF_ONLY，scrollBackward参数初始为NestedScrollMode.SELF_ONLY。|

### func scrollBar(BarState)

```cangjie
public func scrollBar(barState: BarState): This
```

**功能：** 设置滚动条状态。如果容器组件无法滚动，则滚动条不显示。如果容器组件的子组件大小为无穷大，则滚动条不支持拖动和伴随滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|barState|[BarState](./cj-common-types.md#enum-barstate)|是|-|滚动条状态。<br>初始值：BarState.Auto。|

### func scrollBarColor(ResourceColor)

```cangjie
public func scrollBarColor(color: ResourceColor): This
```

**功能：** 设置滚动条的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滚动条的颜色。<br>初始值：0x182431（40%不透明度）。|

### func scrollBarWidth(Length)

```cangjie
public func scrollBarWidth(width: Length): This
```

**功能：** 设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Scroll组件主轴方向的高度，则滚动条的宽度会变为默认值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-|滚动条的宽度。<br>初始值：4.vp。<br>单位：vp。<br>设置为小于0的值时，按初始值处理。设置为0时，不显示滚动条。|

### func scrollSnap(ScrollSnapOptions)

```cangjie
public func scrollSnap(value: ScrollSnapOptions): This
```

**功能：** 设置Scroll组件的限位滚动模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ScrollSnapOptions](#class-scrollsnapoptions)|是|-|Scroll组件的限位滚动模式。|