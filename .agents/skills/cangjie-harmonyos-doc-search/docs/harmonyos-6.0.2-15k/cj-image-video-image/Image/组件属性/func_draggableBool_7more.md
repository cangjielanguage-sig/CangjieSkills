### func draggable(Bool)

```cangjie
public func draggable(value: Bool): This
```

**功能：** 设置组件默认拖拽效果。

> **说明：**
>
> 不能和[onDragStart](../../source_zh_cn/arkui-cj/cj-universal-event-drag.md#func-ondragstartdrageventstring------unit)事件同时使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|设置组件默认拖拽效果，设置为true时，组件可拖拽，绑定的长按手势不生效。若用户需要设置自定义手势，则需要将draggable设置为false。<br>初始值：true。|

### func dynamicRangeMode(DynamicRangeMode)

```cangjie
public func dynamicRangeMode(value: DynamicRangeMode): This
```

**功能：** 设置期望展示的图像动态范围。

> **说明：**
>
> - svg类型图源不支持该属性。
> - 该属性仅在手机设备上生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[DynamicRangeMode](#enum-dynamicrangemode)|是|-|图像显示的动态范围。<br>初始值：DynamicRangeMode.STANDARD。|

### func fillColor(ResourceColor)

```cangjie
public func fillColor(value: ResourceColor): This
```

**功能：** 设置替换svg图片的填充颜色。仅对svg图源生效。

> **说明：**
>
> 如需对png图片进行修改颜色，可以使用[colorFilter](#func-colorfiltercolorfilter)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|设置填充颜色。<br>默认不对组件进行填充。当传入异常值时，系统将使用默认的主题色：浅色模式下为黑色，深色模式下为白色。|

### func fitOriginalSize(Bool)

```cangjie
public func fitOriginalSize(isFitOriginalSize: Bool): This
```

**功能：** 设置图片的显示尺寸是否跟随图源尺寸。图片组件尺寸未设置时，其显示尺寸是否跟随图源尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isFitOriginalSize|Bool|是|-|是否跟随图源尺寸。<br>初始值：false。|

### func interpolation(ImageInterpolation)

```cangjie
public func interpolation(interpolation: ImageInterpolation): This
```

**功能：** 设置图片的插值效果。

> **说明：**
>
> - 减轻低清晰度图片在放大显示的时候出现的锯齿问题，仅针对图片放大插值。
> - svg类型图源不支持该属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|interpolation|[ImageInterpolation](#enum-imageinterpolation)|是|-|图片的插值效果。<br>初始值：ImageInterpolation.Low。|

### func matchTextDirection(Bool)

```cangjie
public func matchTextDirection(isMatchTextDirection: Bool): This
```

**功能：** 设置图片是否跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isMatchTextDirection|Bool|是|-|是否跟随系统语言方向。<br>初始值：false。|

### func objectFit(ImageFit)

```cangjie
public func objectFit(objectFit: ImageFit): This
```

**功能：** 设置图片的填充效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|objectFit|[ImageFit](./cj-common-types.md#enum-imagefit)|是|-|图片的填充效果。<br>初始值：ImageFit.Cover。|