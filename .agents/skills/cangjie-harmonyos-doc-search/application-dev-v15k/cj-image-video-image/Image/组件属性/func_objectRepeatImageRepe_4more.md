### func objectRepeat(ImageRepeat)

```cangjie
public func objectRepeat(objectRepeat: ImageRepeat): This
```

**功能：** 设置图片的重复样式。

> **说明：**
>
> - 从中心点向两边重复，剩余空间不足放下一张图片时会截断。
> - svg类型图源不支持该属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|objectRepeat|[ImageRepeat](./cj-common-types.md#enum-imagerepeat)|是|-|图片的重复样式。<br>初始值：ImageRepeat.NoRepeat。|

### func renderMode(ImageRenderMode)

```cangjie
public func renderMode(renderMode: ImageRenderMode): This
```

**功能：** 设置图片渲染的模式。

> **说明：**
>
> - svg类型图源不支持该属性。
> - 设置 [ColorFilter](#func-colorfiltercolorfilter) 时，该属性设置不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|renderMode|[ImageRenderMode](#enum-imagerendermode)|是|-|图片渲染的模式为原色或黑色。<br>初始值：ImageRenderMode.Original。|

### func sourceSize(Length, Length)

```cangjie
public func sourceSize(width: Length, height: Length): This
```

**功能：** 将原始图片解码成 PixelMap 指定尺寸的图片。PixelMap资源不支持该函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-|图片解码后的宽度。<br>单位：vp。|
|height|[Length](./cj-common-types.md#interface-length)|是|-|图片解码后的高度。<br>单位：vp。|

### func syncLoad(Bool)

```cangjie
public func syncLoad(syncLoad: Bool): This
```

**功能：** 设置是否同步加载图片。

> **说明：**
>
> 建议加载尺寸较小的本地图片时将syncLoad设为true，因为耗时较短，在主线程上执行即可。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|syncLoad|Bool|是|-|是否同步加载图片，默认是异步加载。同步加载时阻塞UI线程，不会显示占位图。<br>初始值：false。|