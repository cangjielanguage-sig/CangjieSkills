## class MediaAssetDataHandler

```cangjie
public abstract class MediaAssetDataHandler<T> {}
```

**功能：** 媒体资源处理器，应用在onDataPrepared方法中可自定义媒体资源处理逻辑。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### func onDataPrepared(T, HashMap\<String, String>)

```cangjie
public open func onDataPrepared(data: T, map: HashMap<String, String>): Unit
```

**功能：** 媒体资源就绪通知，当所请求的图片资源准备就绪时系统会回调此方法。如果资源准备出错，则回调的data为undefined。

T支持Array\<Byte>, [ImageSource](../ImageKit/cj-apis-image.md#class-imagesource), [MovingPhoto](#class-movingphoto)和Bool四种数据类型。

map支持返回的信息：
| map键名  | 值说明 |
|:----------|:-------|
| 'quality'  | 图片质量。高质量为'high'，低质量为'low'。 |

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|T|是|-|已就绪的图片资源数据。泛型，支持Array\<Byte>, [ImageSource](../ImageKit/cj-apis-image.md#class-imagesource), [MovingPhoto](#class-movingphoto)和Bool四种数据类型。|
|map|HashMap\<String, String>|是|-|用于获取图片资源的额外信息，如图片质量。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.base.*
import std.collection.HashMap

// 此处代码可添加在依赖项定义中
class MediaDataHandler <: MediaAssetDataHandler<Bool> {
    public func onDataPrepared(data: Bool, map: HashMap<String, String>): Unit {
        AppLog.info("on video request status prepared")
    }
}

let handler = MediaDataHandler() //此回调的具体应用可查看下文示例代码
```