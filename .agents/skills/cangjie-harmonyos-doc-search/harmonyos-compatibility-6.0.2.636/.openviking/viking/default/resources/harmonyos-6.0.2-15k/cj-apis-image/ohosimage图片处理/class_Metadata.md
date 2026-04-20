## class Metadata

```cangjie
public class Metadata {}
```

**功能：** 图像元数据类，用于存储图像的元数据。目前支持的元数据类型可参考[MetadataType](#enum-metadatatype)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

### func getAllProperties()

```cangjie
public func getAllProperties(): HashMap<String, String>
```

**功能：** 获取图片中所有元数据的属性和值。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|HashMap\<String, String> |返回元数据拥有的所有属性的值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let color: Array<UInt8> = Array<UInt8>(96, repeat: 0) //96为需要创建的像素buffer大小，取值为：height * width *4
let opts: InitializationOptions = InitializationOptions(editable: true, pixelFormat: RGBA_8888,
    size: Size(height: 4, width: 6))
let pixelMap = createPixelMap(color, opts)
let picture = createPicture(pixelMap)
let metaData = pciture.getMetadata(EXIF_METADATA)
let properties = metaData.getAllProperties()
```