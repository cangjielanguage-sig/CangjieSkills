## class Picture

```cangjie
public class Picture {}
```

**功能：** 一些包含特殊信息的图片可以解码为多图对象，多图对象一般包含主图、辅助图和元数据。其中主图包含图像的大部分信息，主要用于显示图像内容；辅助图用于存储与主图相关但不同的数据，展示图像更丰富的信息；元数据一般用来存储关于图像文件的信息。多图对象类用于读取或写入多图对象。在调用Picture的方法前，需要先通过[createPicture](#func-createpicturepixelmap)创建一个Picture实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

### func getMetadata(MetadataType)

```cangjie
public func getMetadata(metadataType: MetadataType): Metadata
```

**功能：** 获取主图的元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|metadataType|[MetadataType](#enum-metadatatype)|是|-|元数据类型，用于获取对应类型的元数据。|

**返回值：**

|类型|说明|
|:----|:----|
|[Metadata](#class-metadata)|返回元数据。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980115|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
  |7600202|Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type.|

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
```

### func setMetadata(MetadataType, Metadata)

```cangjie
public func setMetadata(metadataType: MetadataType, metadata: Metadata): Unit
```

**功能：** 获取主图的元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|metadataType|[MetadataType](#enum-metadatatype)|是|-|元数据的类型，用于设置对应的元数据。|
|metadata|[Metadata](#class-metadata)|是|-|元数据对象。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980115|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
  |7600202|Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type.|

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
pciture.setMetadata(EXIF_METADATA, metaData)
```