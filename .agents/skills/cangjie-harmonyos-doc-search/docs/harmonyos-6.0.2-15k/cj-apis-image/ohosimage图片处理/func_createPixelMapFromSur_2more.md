## func createPixelMapFromSurface(String, Region)

```cangjie
public func createPixelMapFromSurface(surfaceId: String, region: Region): PixelMap
```

**功能：** 根据surfaceId和区域信息，创建一个PixelMap对象。该区域的大小由[Region](#struct-region).size指定。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|surfaceId|String|是|-|对应Surface的ID，可通过预览组件获取，如[XComponent](../../../source_zh_cn/arkui-cj/cj-rendering-drawing-xcomponent.md#xcomponent)组件。|
|region|[Region](#struct-region)|是|-|区域信息。[Region](#struct-region).size的宽高需和设置的预览流大小保持一致。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](#class-pixelmap)|成功同步返回PixelMap对象，失败抛出异常。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980115|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
  |62980105|Failed to get the data.|
  |62980178|Failed to create the PixelMap.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

//surfaceId 可通过预览组件获取，如XComponent组件。

let region = Region(ISize(height: 100, width: 100), 0, 0)
let pixelMap = createPixelMapFromSurface(surfaceId, region)
```

## func createPixelMapFromSurface(String)

```cangjie
public func createPixelMapFromSurface(surfaceId: String): PixelMap
```

**功能：** 根据Surface id和区域信息，创建一个PixelMap对象。该区域的大小由[Region](#struct-region).size指定。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|surfaceId|String|是|-|对应Surface的ID，可通过预览组件获取，如[XComponent](../../../source_zh_cn/arkui-cj/cj-rendering-drawing-xcomponent.md#xcomponent)组件。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](#class-pixelmap)|成功同步返回PixelMap对象，失败抛出异常。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980115|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
  |62980105|Failed to get the data.|
  |62980178|Failed to create the PixelMap.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

//surfaceId 可通过预览组件获取，如XComponent组件。

let pixelMap = createPixelMapFromSurface(surfaceId)
```