## func createPixelMap(InitializationOptions)

```cangjie
public func createPixelMap(opts: InitializationOptions): PixelMap
```

**功能：** 通过属性创建PixelMap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|opts|[InitializationOptions](#class-initializationoptions)|是|-|创建像素的属性，包括透明度、尺寸、缩略值、像素格式和是否可编辑。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](#class-pixelmap)|成功同步返回PixelMap对象，失败抛出异常。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :------- | :--------------------------------------------|
  |  401    | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let opts = InitializationOptions(editable: true, pixelFormat: RGBA_8888, size: Size(height: 4, width: 6))
let pixelMap = createPixelMap(opts)
```

## func createPixelMapFromParcel(MessageSequence)

```cangjie
public func createPixelMapFromParcel(sequence: MessageSequence): PixelMap
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
|[PixelMap](#class-pixelmap)|成功同步返回PixelMap对象，失败抛出异常。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980096|Operation failed.|
  |62980097|IPC error.|
  |62980115|Invalid input parameter.|
  |62980105|Failed to get the data.|
  |62980177|Abnormal API environment.|
  |62980178|Failed to create the PixelMap.|
  |62980179|Abnormal buffer size.|
  |62980180|FD mapping failed.|
  |62980246|Failed to read the PixelMap.|

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
let pixelMap2 = createPixelMapFromParcel(data)
```