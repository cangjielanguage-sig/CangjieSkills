### func sliderInteractionMode(SliderInteraction)

```cangjie
public func sliderInteractionMode(value: SliderInteraction): This
```

**功能：** 设置用户与滑动条组件交互方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SliderInteraction](#enum-sliderinteraction)|是|-|用户与滑动条组件交互方式。<br/>初始值：SliderInteraction.SLIDE_AND_CLICK。|

### func stepColor(ResourceColor)

```cangjie
public func stepColor(value: ResourceColor): This
```

**功能：** 设置刻度颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|刻度颜色。<br/>初始值：<br/>\@r(sys.color.ohos_id_color_foreground)混合<br/> \@r(sys.color.ohos_id_alpha_normal_bg)透明度的颜色。|

### func stepSize(Length)

```cangjie
public func stepSize(value: Length): This
```

**功能：** 设置刻度大小（直径）。当值为0时，刻度点不显示，当值小于0时，取初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|刻度大小（直径）。<br/>初始值：4.vp。<br/>取值范围：[0, trackThickness)。|

### func trackBorderRadius(Length)

```cangjie
public func trackBorderRadius(value: Length): This
```

**功能：** 设置底板圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|底板圆角半径。<br/>初始值：style值为SliderStyle.OutSet初始值为2.vp。<br/>style值为SliderStyle.InSet初始值为10.vp。不支持百分比设置。设定值小于0时取初始值。|

### func trackColor(ResourceColor)

```cangjie
public func trackColor(value: ResourceColor): This
```

**功能：** 根据指定的Color设置滑轨的背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|滑轨的背景颜色。<br/>**说明：**<br/>设置渐变色时，若颜色断点颜色值为非法值或者渐变色断点为空时，渐变色不起效果。<br>初始值：@r(sys.color.ohos_id_color_component_normal)。|

### func trackThickness(Length)

```cangjie
public func trackThickness(value: Length): This
```

**功能：** 根据指定的Length设置滑轨的粗细。设置为小于等于0的值时，取初始值。

为保证滑块和滑轨的SliderStyle样式，blockSize跟随trackThickness同比例增减。

当style为SliderStyle.OutSet时，trackThickness ：blockSize = 1 ：4，当style为SliderStyle.InSet时，trackThickness ：blockSize = 5 ：3。

在变更trackThickness过程中，若trackThickness的大小或者blockSize的大小超过slider组件的width或者height（SliderStyle.OutSet时可能trackThickness没超过，但是blockSize超过了），取初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|滑轨的粗细。<br/>初始值：当参数style的值设置SliderStyle.OutSet 时为 4.0.vp，SliderStyle.InSet时为20.0.vp。|