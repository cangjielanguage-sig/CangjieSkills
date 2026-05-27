### func unRegisterChange(String, ?Callback1Argument\<ChangeData>)

```cangjie
public func unRegisterChange(uri: String, callback!: ?Callback1Argument<ChangeData> = None): Unit
```

**功能：** 取消指定uri的监听，一个uri可以注册多个监听，存在多个callback监听时，可以取消指定注册的callback的监听；不指定callback时取消该uri的所有监听。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|PhotoAsset的uri, Album的uri或[DefaultChangeUri](#enum-defaultchangeuri)的值。|
|callback|?[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[ChangeData](#class-changedata)>|否|None| **命名参数。** 取消[registerChange](#func-registerchangestring-bool-callback1argumentchangedata)注册时的callback的监听，不填时，取消该uri的所有监听。注：off指定注册的callback后不会进入此回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |13900012|Permission denied.|
  |13900020|Invalid argument.|
  |14000011|System inner fail.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class MyCallback<T> <: Callback1Argument<T> {
    public let callabck_: (T) -> Unit
    public init(callabck: (T) -> Unit) {
        callabck_ = callabck
    }
    public open func invoke(arg: T): Unit {
        callabck_(arg)
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let callback1 = MyCallback<ChangeData>(
    {
        arg: ChangeData => AppLog.info(
            "onCallback1. ChangeData: type = ${arg.`type`.toString()}, uris.size: ${arg.uris.size}, extraUris.size = ${arg.extraUris.size}"
        )
    })

let predicates = DataSharePredicates()
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: ['title'], predicates: predicates)
let fetchResult: FetchResult<PhotoAsset> = phAccessHelper.getAssets(fetchOptions)
let firstPhotoAsset = fetchResult.getFirstObject()

phAccessHelper.registerChange(firstPhotoAsset.uri, false, callback1)
phAccessHelper.unRegisterChange(firstPhotoAsset.uri, callback: callback1)
phAccessHelper.unRegisterChange(firstPhotoAsset.uri)
```