### func alt(String)

```cangjie
public func alt(src: String): This
```

**功能：** 设置图片加载时显示的占位图。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|加载时显示的占位图，支持本地图片（png、jpg、bmp、svg、gif和heif类型），不支持网络图片。|

### func alt(AppResource)

```cangjie
public func alt(src: AppResource): This
```

**功能：** 设置图片加载时显示的占位图。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|加载时显示的占位图，支持本地图片（png、jpg、bmp、svg、gif和heif类型），不支持网络图片。|

### func alt(PixelMap)

```cangjie
public func alt(src: PixelMap): This
```

**功能：** 设置图片加载时显示的占位图。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)|是|-|加载时显示的占位图，支持PixelMap类型。<br>初始值：None。|

### func autoResize(Bool)

```cangjie
public func autoResize(autoResize: Bool): This
```

**功能：** 设置图片解码过程中是否对图源自动缩放。

> **说明：**
>
> 该操作会根据显示区域的尺寸决定用于绘制的图源尺寸，有利于减少内存占用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|autoResize|Bool|是|-|图片解码过程中是否对图源自动缩放。设置为true时，组件会根据显示区域的尺寸决定用于绘制的图源尺寸，有利于减少内存占用。如原图大小为1920x1080，而显示区域大小为200x200，则图片会降采样解码到200x200的尺寸，大幅度节省图片占用的内存。<br>初始值：false。|

### func colorFilter(ColorFilter)

```cangjie
public func colorFilter(value: ColorFilter): This
```

**功能：** 为图像设置颜色滤镜效果。

> **说明：**
>
> 设置该属性时，[renderMode](#func-rendermodeimagerendermode)属性设置不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ColorFilter](#class-colorfilter)|是|-|给图像设置颜色滤镜效果，入参为一个的4x5的RGBA转换矩阵。<br>矩阵第一行表示R（红色）的向量值，第二行表示G（绿色）的向量值，第三行表示B（蓝色）的向量值，第四行表示A（透明度）的向量值，4行分别代表不同的RGBA的向量值。<br>当矩阵对角线值为1，其余值为0时，保持图片原有色彩。<br>**计算规则：**<br>如果输入的滤镜矩阵为：<br>![colorfilter1](figures/colorfilter1.png)<br>像素点为像素点为[R, G, B, A]<br>则过滤后的颜色为 [R’, G’, B’, A’]<br>![colorfilter2](figures/colorfilter2.png)|

### func copyOption(CopyOptions)

```cangjie
public func copyOption(value: CopyOptions): This
```

**功能：** 设置图片是否可复制。

> **说明：**
>
> - 当copyOption设置为非CopyOptions.None时，支持使用长按、鼠标右击、快捷组合键'CTRL+C'等方式进行复制。
> - svg图片不支持复制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[CopyOptions](./cj-common-types.md#enum-copyoptions)|是|-|当图片是否可复制。<br>初始值：CopyOptions.None。|