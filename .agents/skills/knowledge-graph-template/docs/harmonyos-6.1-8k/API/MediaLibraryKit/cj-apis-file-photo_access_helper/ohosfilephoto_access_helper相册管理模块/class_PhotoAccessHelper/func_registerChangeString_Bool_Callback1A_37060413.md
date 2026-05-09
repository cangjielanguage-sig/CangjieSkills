### func registerChange(String, Bool, Callback1Argument\<ChangeData>)

```cangjie
public func registerChange(uri: String, forChildUris: Bool, callback: Callback1Argument<ChangeData>): Unit
```

**功能：** 注册对指定uri的监听，使用callback方式返回结果。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|PhotoAsset的uri, Album的uri或[DefaultChangeUri](#enum-defaultchangeuri)的值。|
|forChildUris|Bool|是|-|是否模糊监听。uri为相册uri时：forChildUris为true，能监听到相册中文件的变化。如果是false，只能监听相册本身变化；uri为photoAsset时：forChildUris为true、false没有区别；uri为DefaultChangeUri时：forChildUris必须为true，如果为false将找不到该uri，收不到任何消息。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[ChangeData](#class-changedata)>|是|-|返回要监听的[ChangeData](#class-changedata)。注：uri可以注册多个不同的callback监听，[unregisterChange](#func-unregisterchangestring-callback1argumentchangedata)可以关闭该uri所有监听，也可以关闭指定callback的监听。。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900012 | Permission denied. |
  | 13900020 | Invalid argument. |

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
class MyCallback<T> <: Callback1Argument<T> {
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
    let callback1 = MyCallback<ChangeData>(
        {
            arg: ChangeData => Hilog.info(0, "AppLogCj",
                "onCallback1. ChangeData: type = ${arg.notifyType.toString()}, uris.size: ${arg.uris.size}, extraUris.size = ${arg.extraUris.size}"
            )
        })
    let predicates = DataSharePredicates()
    let fetchOptions: FetchOptions = FetchOptions(['title'], predicates)
    let fetchResult: PhotoAssetResult = phAccessHelper.getAssets(fetchOptions)
    let firstPhotoAsset = fetchResult.getFirstObject()
    phAccessHelper.registerChange(firstPhotoAsset.uri, false, callback1)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```