### static func setFormNextRefreshTime(String, Int32)

```cangjie
public static func setFormNextRefreshTime(formId: String, minute: Int32): Unit
```

**功能：** 设置指定卡片的下一次更新时间。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|formId|String|是|-|卡片标识。|
|minute|Int32|是|-|指定卡片多久之后更新，取值范围：大于等于5，单位：min。|

**异常：**

- IllegalArgumentException:

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |Parameter is error, please check|传入错误的参数。|检查传入的参数是否满足要求。|

- BusinessException：对应错误码的详细介绍请参见[卡片错误码](../../errorcodes/cj-errorcode-form.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16500050|IPC connection error.|
  |16500060|Service connection error.|
  |16500100|Failed to obtain configuration information.|
  |16501000|An internal functional error occurred.|
  |16501001|The ID of the form to be operated does not exist.|
  |16501002|The number of forms exceeds the maximum allowed.|
  |16501003|The form cannot be operated by the current application.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.FormKit.*
import kit.UIKit.{AppLog, BusinessException}

try {
    FormProvider.setFormNextRefreshTime("665702695", 7)
} catch (e: BusinessException) {
    AppLog.error("setFormNextRefreshTime error:${e.code}, ${e.message}")
}
```

### static func updateForm(String, FormBindingData)

```cangjie
public static func updateForm(formId: String, formBindingData: FormBindingData): Unit
```

**功能：** 更新指定的卡片。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|formId|String|是|-|请求更新的卡片标识。|
|formBindingData|[FormBindingData](cj-apis-app-form-formBindingData.md#class-formbindingdata)|是|-|用于更新的数据。|

**异常：**

- IllegalArgumentException:

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |Parameter is error, please check|传入错误的参数。|检查传入的参数是否满足要求。|

- BusinessException：对应错误码的详细介绍请参见[卡片错误码](../../errorcodes/cj-errorcode-form.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16500050|IPC connection error.|
  |16500060|Service connection error.|
  |16500100|Failed to obtain configuration information.|
  |16501000|An internal functional error occurred.|
  |16501001|The ID of the form to be operated does not exist.|
  |16501002|The number of forms exceeds the maximum allowed.|
  |16501003|The form cannot be operated by the current application.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.FormKit.*
import kit.UIKit.{AppLog, BusinessException}

let param = "{\"temperature\": \"22c\", \"time\": \"22:00\"}"
let bindingData = createFormBindingData(obj: param)
AppLog.info(bindingData.data)

try {
    FormProvider.updateForm("665702695", bindingData)
} catch (e: BusinessException) {
    AppLog.error("updateForm error:${e.code}, ${e.message}")
}
```