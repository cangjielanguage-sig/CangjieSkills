### func scrollBar(?BarState)

```cangjie
public func scrollBar(barState: ?BarState): T
```

**功能：** 设置滚动条状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|barState|?[BarState](./cj-common-types.md#enum-barstate)|是|-|滚动条状态。<br>初始值：<br>List、Grid、Scroll组件初始值为：BarState.Auto。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回组件实例。|

### func scrollBarColor(?ResourceColor)

```cangjie
public func scrollBarColor(color: ?ResourceColor): T
```

**功能：** 设置滚动条的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滚动条的颜色。<br> 初始值：0x182431（40%不透明度）。为HEX格式颜色，支持rgb或者argb，示例：0xffffff。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回组件实例。|

### func scrollBarWidth(?Length)

```cangjie
public func scrollBarWidth(value: ?Length): T
```

**功能：** 设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过滚动组件主轴方向的高度，则滚动条的宽度会变为初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|滚动条的宽度。<br> 初始值：4 <br> 单位：vp <br> 取值范围：设置为小于0的值时，按初始值处理。设置为0时，不显示滚动条。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回组件实例。|

### func clipContent(?ContentClipMode)

```cangjie
public func clipContent(clip: ?ContentClipMode): T
```

**功能：** 设置滚动容器的内容层裁剪区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|clip|?[ContentClipMode](./cj-scroll-swipe-scroll.md#enum-contentclipmode)|是|-|裁剪只针对滚动容器的内容，即其子节点，背景不受影响。<br>初始值：Grid、Scroll的初始值为ContentClipMode.Boundary，List的初始值为ContentClipMode.ContentOnly。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回组件实例。|

### func clipContent(?RectShape)

```cangjie
public func clipContent(clip: ?RectShape): T
```

**功能：** 设置滚动容器的内容层裁剪区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|clip|?[RectShape](./cj-apis-shape.md#class-rectshape)|是|-|裁剪只针对滚动容器的内容，即其子节点，背景不受影响。通过RectShape传入自定义矩形区域时仅支持设置宽高和相对于组件左上角的[offset](./cj-universal-attribute-location.md#func-offsetlength-length)，不支持圆角。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回组件实例。|

### func enableScrollInteraction(?Bool)

```cangjie
public func enableScrollInteraction(value: ?Bool): T
```

**功能：** 设置是否支持滚动手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否支持滚动手势，当设置为false时，无法通过手指或者鼠标滚动，但不影响控制器[Scroller](./cj-scroll-swipe-scroll.md#class-scroller)的滚动接口。<br>初始值：true。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回组件实例。|