### func save(AsyncCallback\<Array\<String>>, DocumentSaveOptions)

```cangjie
public func save(
    callback: AsyncCallback<Array<String>>,
    option!: DocumentSaveOptions = DocumentSaveOptions()
): Unit
```

**功能：** 通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。接口采用callback异步返回形式，传入参数DocumentSaveOptions对象，返回保存文件的URI数组。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Array\<String>>|是|-|callback返回documentPicker保存后的结果集。|
|option|[DocumentSaveOptions](#struct-documentsaveoptions)|否|DocumentSaveOptions()| **命名参数。** documentPicker保存选项。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.CoreFileKit.*

let actualContext: UIAbilityContext =Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let picker = DocumentViewPicker(actualContext)
let option = DocumentSaveOptions(newFileNames: ["DocumentViewPicker.txt"])
let saveCallback = {
    errorCode: Option<AsyncError>, data: Option<Array<String>> => match (errorCode) {
        case Some(e) =>
            AppLog.info("document save error: errcode is ${e.code}")
        case _ =>
            match (data) {
                case Some(value) =>
                    AppLog.info("documentUris is ${value}")
                case _ => AppLog.info("document save error: data is null")
            }
    }
}
picker.save(saveCallback, option: option)
```

### func select(AsyncCallback\<Array\<String>>, DocumentSelectOptions)

```cangjie
public func select(
    callback: AsyncCallback<Array<String>>,
    option!: DocumentSelectOptions = DocumentSelectOptions()
): Unit
```

**功能：** 通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。接口采用callback异步返回形式，传入参数DocumentSelectOptions对象，返回选择文件的URI数组。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Array\<String>>|是|-|callback返回documentPicker选择后的结果集。|
|option|[DocumentSelectOptions](#class-documentselectoptions)|否|DocumentSelectOptions()| **命名参数。** documentPicker选择选项。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.CoreFileKit.*

let actualContext: UIAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let picker = DocumentViewPicker(actualContext)
let option = DocumentSelectOptions(selectMode: DocumentSelectMode.MIXED)
let documentSelectCallback = {
    errorCode: Option<AsyncError>, data: Option<Array<String>> => match (errorCode) {
        case Some(e) =>
            AppLog.info("document select error: errcode is ${e.code}")
        case _ =>
            match (data) {
                case Some(value) =>
                    AppLog.info("documentUris is ${value}")
                case _ => AppLog.info("document select error: data is null")
            }
    }
}
picker.select(documentSelectCallback, option: option)
```