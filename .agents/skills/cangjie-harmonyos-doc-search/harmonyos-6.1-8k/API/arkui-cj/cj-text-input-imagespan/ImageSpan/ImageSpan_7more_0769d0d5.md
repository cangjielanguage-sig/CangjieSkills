# ImageSpan

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

作为[Text](./cj-text-input-text.md)组件的子组件，用于显示行内图片。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?ResourceStr)

```cangjie
public init(value: ?ResourceStr)
```

**功能：** 创建ImageSpan组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|图片的数据源，支持本地图片和网络图片。|

### init(?PixelMap)

```cangjie
public init(value: ?PixelMap)
```

**功能：** 创建ImageSpan组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|图片的数据源，支持本地图片和网络图片。|

## 通用属性/通用事件

通用属性：支持[尺寸设置](./cj-universal-attribute-size.md)、[背景设置](./cj-universal-attribute-background.md)、[边框设置](./cj-universal-attribute-border.md)。

通用事件：仅支持[点击事件](./cj-universal-event-click.md#func-onclickclickevent---unit)。

## 组件属性

### func colorFilter(?ColorFilter)

```cangjie
public func colorFilter(filter: ?ColorFilter): This
```

**功能：** 设置图像的颜色滤镜效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filter|?[ColorFilter](./cj-image-video-image.md#class-colorfilter)|是|-|颜色滤镜效果。<br>初始值：ColorFilter([])。|

### func objectFit(?ImageFit)

```cangjie
public func objectFit(value: ?ImageFit): This
```

**功能：** 设置图片的缩放类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ImageFit](./cj-common-types.md#enum-imagefit)|是|-|图片的缩放类型。<br>初始值：ImageFit.Cover。|

### func verticalAlign(?ImageSpanAlignment)

```cangjie
public func verticalAlign(value: ?ImageSpanAlignment): This
```

**功能：** 设置图片基于行高的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ImageSpanAlignment](./cj-common-types.md#enum-imagespanalignment)|是|-|图片基于文本的对齐方式。<br>初始值：ImageSpanAlignment.Bottom。|

## 组件事件

### func onComplete(?ImageCompleteCallback)

```cangjie
public func onComplete(callback: ?ImageCompleteCallback): This
```

**功能：** 图片数据加载成功和解码成功时均触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[ImageCompleteCallback](./cj-image-video-image.md#type-imagecompletecallback)|是|-|回调函数，图片数据加载成功和解码成功时触发。参数：成功加载的图片尺寸。<br>初始值：{ _ => }。|

### func onError(?ImageErrorCallback)

```cangjie
public func onError(callback: ?ImageErrorCallback): This
```

**功能：** 图片加载异常时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[ImageErrorCallback](./cj-image-video-image.md#type-imageerrorcallback)|是|-|回调函数，图片加载出现异常时触发。参数：图片加载异常信息。<br>初始值：{ _ => }。|