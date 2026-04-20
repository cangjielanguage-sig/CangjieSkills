### func showAssetsCreationDialog(Array\<String>, Array\<PhotoCreationConfig>, Callback1Argument\<Array\<String>>)

```cangjie
public func showAssetsCreationDialog(srcFileUris: Array<String>, photoCreationConfigs: Array<PhotoCreationConfig>,
    callback: Callback1Argument<Array<String>>): Unit
```

**功能：** 调用接口拉起保存确认弹窗。用户同意保存后，返回已创建并授予保存权限的uri列表，该列表永久生效，应用可使用该uri写入图片/视频。如果用户拒绝保存，将返回空列表。弹框需要显示应用名称，无法直接获取应用名称，依赖于配置项的label和icon，因此调用此接口时请确保module.json5文件中的abilities标签中配置了label和icon项。

> **说明：**
>
> 当传入uri为沙箱路径时，可正常保存图片/视频，但无界面预览。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|srcFileUris|Array\<String>|是|-|需保存到媒体库中的图片/视频文件对应的媒体库uri。<br>**注意：**<br>- 一次弹窗最多保存100张图片。<br>- 仅支持处理图片、视频uri。<br>- 不支持手动拼接的uri，需调用接口获取。|
|photoCreationConfigs|Array\<[PhotoCreationConfig](#class-photocreationconfig)>|是|-|保存图片或视频到媒体库的配置，包括文件名等，与srcFileUris保持一一对应。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<Array\<String>>|是|-|回调函数，返回给应用的媒体库文件uri列表。uri已对应用授权，支持应用写入数据。如果生成uri异常，则返回批量创建错误码。<br>返回-3006表示不允许出现非法字符；返回-2004表示图片类型和后缀不符；返回-203表示文件操作异常。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14000011 | Internal system error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class MyCallback1<T> <: Callback1Argument<T> {
    public let callabck_: (T) -> Unit
    public init(callabck: (T) -> Unit) {
        callabck_ = callabck
    }
    public func invoke(err: ?BusinessException, arg: T): Unit {
        callabck_(arg)
    }
}

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let phAccessHelper = getPhotoAccessHelper(ctx)
    let callback = MyCallback1<Array<String>>(
        {
            arg: Array<String> =>
            Hilog.info(0, "AppLogCj", "oncallback: Array.size: ${arg.size}")
            for (str in arg) {
                Hilog.info(0, "AppLogCj", "oncallback: uri: ${str}")
            }
        }
    )
    // 获取需要保存到媒体库的位于应用沙箱的图片/视频uri
    // 实际场景请使用真实的uri
    let srcFileUris: Array<String> = ["file://media/Photo/37/IMG_1731463495_028/IMG_20241113_100315.jpg"]
    let photoCreationConfigs: Array<PhotoCreationConfig> = [
        PhotoCreationConfig(
            'jpg',
            PhotoType.Image,
            title: "test4",
            subtype: PhotoSubtype.Default
        )
    ]
    phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs, callback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```