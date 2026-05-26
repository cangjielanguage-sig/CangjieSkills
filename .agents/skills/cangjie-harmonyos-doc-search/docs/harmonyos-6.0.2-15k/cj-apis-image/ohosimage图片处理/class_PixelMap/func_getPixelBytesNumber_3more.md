### func getPixelBytesNumber()

```cangjie
public func getPixelBytesNumber(): UInt32
```

**功能：** 获取图像像素的总字节数。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|图像像素的总字节数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
let pixelBytesNumber: UInt32 = pixelMap.getPixelBytesNumber()
```

### func marshalling(MessageSequence)

```cangjie
public func marshalling(sequence: MessageSequence): Unit
```

**功能：** 将PixelMap序列化后写入MessageSequence。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sequence|[MessageSequence](../IPCKit/cj-apis-rpc.md#class-messagesequence)|是|-|新创建的MessageSequence。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980097|IPC error.|
  |62980115|Invalid input parameter.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import kit.IPCKit.*

let color: Array<UInt8> = Array<UInt8>(96, repeat: 0) //96为需要创建的像素buffer大小，取值为：height * width *4
let opts: InitializationOptions = InitializationOptions(editable: true, pixelFormat: RGBA_8888,
    size: Size(height: 4, width: 6))
let pixelMap = createPixelMap(color, opts)
let data = MessageSequence.create()
pixelMap.marshalling(data)
```

### func unmarshalling(MessageSequence)

```cangjie
public func unmarshalling(sequence: MessageSequence): PixelMap
```

**功能：** 从MessageSequence中获取PixelMap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sequence|[MessageSequence](../IPCKit/cj-apis-rpc.md#class-messagesequence)|是|-|保存有PixelMap信息的MessageSequence。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](#class-pixelmap)|返回PixelMap。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980096|The operation failed.|
  |62980097|IPC error.|
  |62980115|Invalid input parameter.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import kit.IPCKit.*

let color: Array<UInt8> = Array<UInt8>(96, repeat: 0) //96为需要创建的像素buffer大小，取值为：height * width *4
let opts: InitializationOptions = InitializationOptions(editable: true, pixelFormat: RGBA_8888,
    size: Size(height: 4, width: 6))
let pixelMap = createPixelMap(color, opts)
let data = MessageSequence.create()
pixelMap.marshalling(data)
let pixelMap1 = pixelMap.unmarshalling(data)
```