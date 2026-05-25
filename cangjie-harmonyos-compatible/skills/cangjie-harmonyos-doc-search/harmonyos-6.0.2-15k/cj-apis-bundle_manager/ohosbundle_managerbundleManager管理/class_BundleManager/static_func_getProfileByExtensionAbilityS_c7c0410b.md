### static func getProfileByExtensionAbility(String, String, String)

```cangjie
public static func getProfileByExtensionAbility(moduleName: String, extensionAbilityName: String,
    metadataName!: String = ""): Array<String>
```

**功能：** 根据给定的moduleName、extensionAbilityName和metadataName（module.json中metadata标签下的name）获取相应配置文件的json格式字符串，返回对象为String数组。

配置信息资源的资源文件中使用引用定义的资源，在返回的JSON字符串中将保持资源引用的字符串格式，例如`$string: myResourceID`，其中`myResourceID`是工程在构建过程中为资源自动分配的资源ID。开发者可以使用`ohos/resource_manager`包中的相关接口来获取这类引用的资源。

如果配置文件信息采用了资源引用格式，则返回值将保持资源引用格式（例如$string: res_id），开发者可以通过资源管理模块的相关接口，来获取引用的资源。

> **说明：**
>
> - 拓展能力的配置信息资源在相应的module.json5文件中`module.extensionAbilities[].metadata`标签下定义。
> - 配置信息资源的数据内容以紧凑的JSON字符串格式返回的。
> - 一个拓展能力可以拥有零到若干个配置信息资源。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|moduleName|String|是|-|目标模块的名称。|
|extensionAbilityName|String|是|-|目标拓展能力的名称。|
|metadataName|String|否|""| **命名参数。** 目标配置信息资源的名称。组件的元信息名称，即module.json5配置文件中extensionAbilities标签下的metadata标签的name，默认值为空。<br>- 当`metadataName`为目标拓展能力的某配置信息资源的名称时，将只返回该配置信息的数据内容，此时返回的数组中只拥有一个元素。<br>- 当`metadataName`缺省，或为空字符串时，将返回通过模块名称和拓展能力名称确定的拓展能力的所有配置信息的数据内容，此时返回的数组中将拥有零到若干个元素。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|目标拓展能力的配置信息资源的数据内容。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[包管理子系统通用错误码](../../errorcodes/cj-errorcode-bundle.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |17700002|The specified module is not found.|
  |17700003|The specified ability is not found.|
  |17700024|The specified profile is not found in the HAP.|
  |17700026|The specified bundle is disabled.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

let moduleName = "entry"
let extensionAbilityName = "EntryFormAbility"
let metadataName = "ohos.extension.form"
let info = BundleManager.getProfileByExtensionAbility(moduleName, extensionAbilityName, metadataName: metadataName)
```