# 显示图片（Image）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

开发者经常需要在应用中显示一些图片，例如：按钮中的icon、网络图片、本地图片等。在应用中显示图片需要使用Image组件实现，Image支持多种图片格式，包括png、jpg、bmp、svg、gif和heif，具体用法请参考[Image](../reference/arkui-cj/cj-image-video-image.md)组件。

Image通过调用接口来创建，接口调用形式如下：

```cangjie
Image(src: String | AppResource | PixelMap | ImageContent)
```

该接口通过图片数据源获取图片，支持本地图片和网络图片的渲染展示。其中，src是图片的数据源，加载方式请参考[加载图片资源](#加载图片资源)。

## 加载图片资源

Image支持加载存档图、多媒体像素图两种类型。

### 存档图类型数据源

存档图类型的数据源可以分为网络资源、Resource资源和base64。

- 网络资源

  引入网络图片需申请权限ohos.permission.INTERNET，具体申请方式请参考[声明权限](../security/AccessToken/cj-declare-permissions.md)。此时，Image组件的src参数为网络图片的链接。

  当前Image组件仅支持加载简单网络图片。

  Image组件首次加载网络图片时，需要请求网络资源，非首次加载时，默认从缓存中直接读取图片。

  网络图片必须支持RFC 9113标准，否则会导致加载失败。如果下载的网络图片大于10MB或一次下载的网络图片数量较多，建议使用[HTTP](../network/cj-http-request.md)工具提前预下载，提高图片加载性能，方便应用侧管理数据。

  ```cangjie
  Image("https://www.example.com/example.jpg") // 实际使用时请替换为真实地址
  ```

- Resource资源

  使用资源格式可以跨包/跨模块引入图片，resources文件夹下的图片都可以通过@r资源接口读取到并转换到AppResource格式。resources文件夹下的目录结构如下图所示：

  ![image-resource](figures/image-resource.jpg)

  调用方式：

  ```cangjie
  Image(@r(app.media.startIcon))
  ```

## 显示矢量图

Image组件可显示矢量图（svg格式的图片），svg标签文档请参考[svg说明](../reference/ImageKit/cj-apis-image.md#svg标签说明)。

svg格式的图片可以使用fillColor属性改变图片的绘制颜色。

```cangjie
Image(@r(app.media.cloud))
  .width(50)
  .fillColor(Color.Blue)
```

svg格式的原始图片如图：

![Imagesource](figures/Imagesource.png)

设置绘制颜色后的svg图片如图：

![Imagesource1](figures/Imagesource1.png)

### 矢量图引用位图

如果Image加载的Svg图源中包含对本地位图的引用，则Svg图源的路径应当设置在src/main/resources/base/media目录下，同时，本地位图的路径应设置为与Svg图源同级的相对路径。

Image加载的Svg图源路径设置方法如下所示：

```cangjie
Image('resource://rawfile/icon.svg')
  .width(50)
  .height(50)
```

Svg图源通过`<image>`标签的`xmlns:xlink`属性指定本地位图路径，本地位图路径设置为跟Svg图源同级的相对路径：

```cangjie
<svg width="200" height="200">
  <image width="200" height="200" xmlns:xlink="sky.png">
</svg>
```

文件工程路径示例如图：

![image path](figures/imagePath.png)