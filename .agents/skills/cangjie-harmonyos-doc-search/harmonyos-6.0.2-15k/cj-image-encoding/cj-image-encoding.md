# 使用ImagePacker完成图片编码

图片编码指将PixelMap编码成不同格式的存档图片，当前支持打包为JPEG、WebP、PNG 和 HEIF(不同硬件设备的支持情况有所不同) 格式，用于后续处理，如保存、传输等。

## 开发步骤

图片编码相关API的详细介绍请参见：[图片编码接口说明](../../../API_Reference/source_zh_cn/apis/ImageKit/cj-apis-image.md#class-imagepacker)。

### 图片编码进文件流

1. 创建图像编码ImagePacker对象。

    ```cangjie
    // 导入相关模块包。
    import kit.ImageKit.*

    let imagePackerApi = createImagePacker()
    ```

2. 设置编码输出流和编码参数。

    - format为图像的编码格式；quality为图像质量，范围从0-100，100为最佳质量。

        > **说明：**
        > 根据MIME标准，标准编码格式为image/jpeg。当使用image编码时，PackingOption.format设置为image/jpeg，image编码后的文件扩展名可设为.jpg或.jpeg，可在支持image/jpeg解码的平台上使用。

        ```cangjie
        var packOpts = PackingOption('image/jpeg', 98)
        ```

    - 编码为hdr内容(需要资源本身为hdr，支持jpeg格式)。

        ```cangjie
        packOpts.desiredDynamicRange = image.PackingDynamicRange.AUTO;
        ```

3. [创建PixelMap对象或创建ImageSource对象](./cj-image-decoding.md)。

4. 进行图片编码，并保存编码后的图片。

    方法一：通过PixelMap进行编码。

    ```cangjie
    // data 为打包获取到的文件流，写入文件保存即可得到一张图片。
    let data = imagePackerApi.packing(pixelMap, packOpts)
    ```

    方法二：通过imageSource进行编码。

    ```cangjie
    // data 为打包获取到的文件流，写入文件保存即可得到一张图片。
    let data = imagePackerApi.packing(imageSource, packOpts)
    ```

### 图片编码进文件

在编码时，开发者可以传入对应的文件路径，编码后的内存数据将直接写入文件。

方法一：通过PixelMap编码进文件。

```cangjie
import kit.CoreFileKit.*
// globalcontext需要在main_ability.cj中的func onCreate中赋值：globalcontext = this.context
var globalAbilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None
let path = globalAbilityContext.getOrThrow().cacheDir + '/pixel_map.jpg'

let file = FileFs.open(path, mode: OpenMode.CREATE.mode | OpenMode.READ_WRITE.mode)
// 直接打包进文件。
imagePackerApi.packToFile(pixelMap, IntNative(file.fd), packOpts)
FileFs.close(file.fd)
```

方法二：通过imageSource编码进文件。

```cangjie
import kit.CoreFileKit.*
// globalcontext需要在main_ability.cj中的func onCreate中赋值：globalcontext = this.context
var globalAbilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None
let filePath = globalAbilityContext.getOrThrow().cacheDir + '/image_source.jpg'
let file = FileFs.open(filePath, mode: OpenMode.CREATE.mode | OpenMode.READ_WRITE.mode)
// 直接打包进文件。
imagePackerApi.packToFile(imageSource, IntNative(file.fd), packOpts)
FileFs.close(file.fd)
```

### 图片编码保存进图库

可以将图片编码保存到应用沙箱，然后使用媒体文件管理相关接口[保存媒体库资源](../medialibrary/cj-photoAccessHelper-savebutton.md)。
