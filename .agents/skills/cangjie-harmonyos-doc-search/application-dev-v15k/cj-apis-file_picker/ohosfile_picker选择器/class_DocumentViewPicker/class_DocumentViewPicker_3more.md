## class DocumentViewPicker

```cangjie
public class DocumentViewPicker {
    public DocumentViewPicker(let abilityContext: UIAbilityContext)
}
```

**功能：** 文件选择器对象，用来支撑选择和保存各种格式文档。在使用前，需要先创建DocumentViewPicker实例。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

### DocumentViewPicker(UIAbilityContext)

```cangjie
public DocumentViewPicker(let abilityContext: UIAbilityContext)
```

**功能：** 创建DocumentViewPicker实例。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abilityContext|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|提供允许访问特定Ability的资源的能力。|

### func getSelectedIndex()

```cangjie
public func getSelectedIndex(): Int32
```

**功能：** 获取保存成功后的文件后缀类型的下标。

该方法只在调用[save](#func-saveasynccallbackarraystring-audiosaveoptions)时使用生效，其他场景下不可以使用。

该方法需要配置参数[DocumentSaveOptions](#struct-documentsaveoptions).fileSuffixChoices使用。

该方法返回的是所选后缀类型的下标(Int32)，所选的后缀类型是开发者所传的参数[DocumentSaveOptions](#struct-documentsaveoptions).fileSuffixChoices里的某个后缀类型，如果没有传参，并且调用了getSelectedIndex()方法，返回值为-1。

**系统能力：** SystemCapability.FileManagement.UserFileService.FolderSelection

**起始版本：** 16

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回保存成功后的文件后缀类型的下标。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.CoreFileKit.*

let actualContext: UIAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
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
            let index = picker.getSelectedIndex()
            AppLog.info("index is ${index}")
    }
}
picker.save(saveCallback, option: option)
```