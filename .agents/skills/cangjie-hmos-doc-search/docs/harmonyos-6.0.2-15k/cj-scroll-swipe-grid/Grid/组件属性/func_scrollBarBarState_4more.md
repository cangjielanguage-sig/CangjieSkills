### func scrollBar(BarState)

```cangjie
public func scrollBar(value: BarState): This
```

**功能：** 设置滚动条状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BarState](cj-common-types.md#enum-barstate)|是|-|滚动条状态。<br/>初始值：BarState.Auto|

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
|color|[ResourceColor](cj-common-types.md#interface-resourcecolor)|是|-|滚动条的颜色。<br/>初始值：0x182431（40%不透明度）<br> 为HEX格式颜色，支持rgb或者argb，示例：0xffffff。|

### func scrollBarWidth(Length)

```cangjie
public func scrollBarWidth(value: Length): This
```

**功能：** 设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Grid组件主轴方向的高度，则滚动条的宽度会变为初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|滚动条的宽度。<br/>初始值：4<br/>单位：vp <br> 取值范围：设置为小于0的值时，按初始值处理。设置为0时，不显示滚动条。|

### func supportAnimation(Bool)

```cangjie
public func supportAnimation(isSupportAnimation: Bool): This
```

**功能：** 设置是否支持动画。当前支持GridItem拖拽动画。仅在滚动模式下（只设置rowsTemplate、columnsTemplate其中一个）支持动画。仅在大小规则的Grid中支持拖拽动画，跨行或跨列场景不支持。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isSupportAnimation|Bool|是|-|是否支持动画。<br/>初始值：false，不支持动画。|