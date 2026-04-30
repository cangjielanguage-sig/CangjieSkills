## func createPremultipliedPixelMap(PixelMap, PixelMap)

```cangjie
public func createPremultipliedPixelMap(src: PixelMap, dst: PixelMap): Unit
```

**功能：** 将PixelMap的透明通道非预乘模式转变为预乘模式，转换后的数据存入目标PixelMap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[PixelMap](#class-pixelmap)|是|-|源PixelMap对象。|
|dst|[PixelMap](#class-pixelmap)|是|-|目标PixelMap对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed|
  |62980103|The image data is not supported|
  |62980246|Failed to read the pixelMap|
  |62980248|Pixelmap not allow modify|

## func createUnpremultipliedPixelMap(PixelMap, PixelMap)

```cangjie
public func createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap): Unit
```

**功能：** 将PixelMap的透明通道预乘模式转变为非预乘模式，转换后的数据存入目标PixelMap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[PixelMap](#class-pixelmap)|是|-|源PixelMap对象。|
|dst|[PixelMap](#class-pixelmap)|是|-|目标PixelMap对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed|
  |62980103|The image data is not supported|
  |62980246|Failed to read the pixelMap|
  |62980248|Pixelmap not allow modify|