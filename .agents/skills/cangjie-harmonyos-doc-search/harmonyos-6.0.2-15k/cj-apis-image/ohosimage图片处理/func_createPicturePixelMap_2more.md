## func createPicture(PixelMap)

```cangjie
public func createPicture(mainPixelmap: PixelMap): Picture
```

**功能：** 通过主图的pixelmap创建一个Picture对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mainPixelmap|[PixelMap](#class-pixelmap)|是|-|主图的pixelmap。|

**返回值：**

|类型|说明|
|:----|:----|
|[Picture](#class-picture)|返回Picture对象。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :------- | :--------------------------------------------|
  | 62980115 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types.3.Parameter verification failed. |

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
```

## func createPixelMap(Array\<UInt8>, InitializationOptions)

```cangjie
public func createPixelMap(colors: Array<UInt8>, opts: InitializationOptions): PixelMap
```

**功能：** 通过属性创建PixelMap，默认采用BGRA_8888格式处理数据，目前只支持BGRA_8888格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colors|Array\<UInt8>|是|-|BGRA_8888格式的颜色数组。|
|opts|[InitializationOptions](#class-initializationoptions)|是|-|创建像素的属性，包括透明度，尺寸，缩略值，像素格式和是否可编辑。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](#class-pixelmap)|返回Pixelmap。<br>当创建的pixelmap大小超过原图大小时，返回原图pixelmap大小。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :------- | :--------------------------------------------|
  | 62980096 | If the operation failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let color: Array<UInt8> = Array<UInt8>(96, repeat: 0) //96为需要创建的像素buffer大小，取值为：height * width *4
let opts: InitializationOptions = InitializationOptions(editable: true, pixelFormat: RGBA_8888,
    size: Size(height: 4, width: 6))
let pixelMap = createPixelMap(color, opts)
```