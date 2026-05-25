### func alt(?ResourceStr)

```cangjie
public func alt(src: ?ResourceStr): This
```

**功能：** 设置图片加载时显示的占位图。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|加载时显示的占位图，支持本地图片（png、jpg、bmp、svg、gif和heif类型），不支持网络图片。<br>初始值：""。|

### func autoResize(?Bool)

```cangjie
public func autoResize(value: ?Bool): This
```

**功能：** 设置图片解码过程中是否对图源自动缩放。

> **说明：**
>
> 该操作会根据显示区域的尺寸决定用于绘制的图源尺寸，有利于减少内存占用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|图片解码过程中是否对图源自动缩放。设置为true时，组件会根据显示区域的尺寸决定用于绘制的图源尺寸，有利于减少内存占用。如原图大小为1920x1080，而显示区域大小为200x200，则图片会降采样解码到200x200的尺寸，大幅度节省图片占用的内存。<br>初始值：false|

### func fillColor(?ResourceColor)

```cangjie
public func fillColor(value: ?ResourceColor): This
```

**功能：** 设置替换svg图片的填充颜色。仅对svg图源生效。

> **说明：**
>
> 如需对png图片进行修改颜色，可以使用[colorFilter](#class-colorfilter)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|设置填充颜色。|

### func fitOriginalSize(?Bool)

```cangjie
public func fitOriginalSize(value: ?Bool): This
```

**功能：** 设置图片的显示尺寸是否跟随图源尺寸。图片组件尺寸未设置时，其显示尺寸是否跟随图源尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否跟随图源尺寸。<br>初始值：false。|

### func interpolation(?ImageInterpolation)

```cangjie
public func interpolation(value: ?ImageInterpolation): This
```

**功能：** 设置图片的插值效果，即缓解图片在缩放时的锯齿问题。

> **说明：**
>
> - 减轻低清晰度图片在放大显示的时候出现的锯齿问题，仅针对图片放大插值。
> - svg类型图源不支持该属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ImageInterpolation](./cj-common-types.md#enum-imageinterpolation)|是|-|图片的插值效果。<br>初始值：ImageInterpolation.Low。|

### func matchTextDirection(?Bool)

```cangjie
public func matchTextDirection(value: ?Bool): This
```

**功能：** 设置图片是否跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否跟随系统语言方向。<br>初始值：false。|

### func objectFit(?ImageFit)

```cangjie
public func objectFit(value: ?ImageFit): This
```

**功能：** 设置图片的填充效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ImageFit](./cj-common-types.md#enum-imagefit)|是|-|图片的填充效果。<br>初始值：ImageFit.Cover。|