### func scrollBar(BarState)

```cangjie
public func scrollBar(barState: BarState): This
```

**功能：** 设置滚动条状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|barState|[BarState](./cj-common-types.md#enum-barstate)|是|-|滚动条状态。<br>初始值：<br>List、Grid、Scroll组件初始值为：BarState.Auto，<br>WaterFlow组件初始值为BarState.Off。|

### func scrollBarColor(ResourceColor)

```cangjie
public func scrollBarColor(color: ResourceColor): This
```

**功能：** 设置滚动条的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滚动条的颜色。<br> 初始值：0x182431（40%不透明度）。为HEX格式颜色，支持rgb或者argb，示例：0xffffff。|

### func scrollBarWidth(Length)

```cangjie
public func scrollBarWidth(value: Length): This
```

**功能：** 设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过滚动组件主轴方向的高度，则滚动条的宽度会变为初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|滚动条的宽度。<br> 初始值：4 <br> 单位：vp <br> 取值范围：设置为小于0的值时，按初始值处理。设置为0时，不显示滚动条。|

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
|edgeEffect|[EdgeEffect](./cj-common-types.md#enum-edgeeffect)|是|-|滚动组件的边缘滑动效果，支持弹簧效果和阴影效果。<br>初始值：Grid、Scroll、WaterFlow组件初始值为EdgeEffect.None，List组件初始值为EdgeEffect.Spring。|
|options|[EdgeEffectOptions](#class-edgeeffectoptions)|是|-|组件内容大小小于组件自身时，是否开启滑动效果。设置为{ alwaysEnabled: true }会开启滑动效果，{ alwaysEnabled: false }不开启。<br>初始值：List、Grid、WaterFlow组件初始值为{ alwaysEnabled: false }，Scroll组件初始值为{ alwaysEnabled: true }。|

### func clipContent(ContentClipMode)

```cangjie
public func clipContent(clip: ContentClipMode): This
```

**功能：** 设置滚动容器的内容层裁剪区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|clip|[ContentClipMode](#enum-contentclipmode)|是|-|裁剪只针对滚动容器的内容，即其子节点，背景不受影响。<br>初始值：Grid、Scroll的初始值为ContentClipMode.BOUNDARY，List、WaterFlow的初始值为ContentClipMode.CONTENT_ONLY。|

### func clipContent(RectShape)

```cangjie
public func clipContent(clip: RectShape): This
```

**功能：** 设置滚动容器的内容层裁剪区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|clip|[RectShape](./cj-universal-attribute-shapclip.md#class-rectshape)|是|-|裁剪只针对滚动容器的内容，即其子节点，背景不受影响。通过RectShape传入自定义矩形区域时仅支持设置宽高和相对于组件左上角的[offset](./cj-universal-attribute-location.md#func-offsetlength-length)，不支持圆角。|