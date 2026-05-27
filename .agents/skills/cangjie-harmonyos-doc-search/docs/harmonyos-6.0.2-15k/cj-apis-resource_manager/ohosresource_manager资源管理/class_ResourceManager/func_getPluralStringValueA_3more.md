### func getPluralStringValue(AppResource, Int64)

```cangjie
public func getPluralStringValue(resource: AppResource, num: Int64): String
```

**功能：** 获取资源对象的单复数字符串资源，并根据指定数量格式化字符串。此接口用于多工程应用内跨包访问。

> **说明：**
>
> 中文环境下，字符串不区分单复数；英文环境下，字符串区分单复数。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resource|[AppResource](#class-appresource)|是|-|资源对象。|
|num|Int64|是|-|数量值。|

**返回值：**

|类型|说明|
|:----|:----|
|String|指定资源对象的单复数字符串资源。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9001001|If the resId invalid.|
  |9001002|If the resource not found by resId.|
  |9001006|If the resource re-ref too much.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let res = @r(app.plural.test)
let resource = AppResource("com.example.myapplication", "entry", Int32(res.id))
resourceManager.getPluralStringValue(resource, 1)
```

### func getRawFd(String)

```cangjie
public func getRawFd(path: String): RawFileDescriptor
```

**功能：** 获取resources/rawfile目录下对应rawfile文件的descriptor。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|rawfile文件路径。|

**返回值：**

|类型|说明|
|:----|:----|
|[RawFileDescriptor](#class-rawfiledescriptor)|rawfile文件的descriptor。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9001005|If the resource not found by path.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*
import ohos.base.AppLog

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let rawfd = resourceManager.getRawFd("test.txt")
AppLog.info("${rawfd.fd} ${rawfd.offset} ${rawfd.length}")
```

### func getRawFileContent(String)

```cangjie
public func getRawFileContent(path: String): Array<UInt8>
```

**功能：** 获取resources/rawfile目录下对应的rawfile文件内容，返回字节数组。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|rawfile文件路径。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|rawfile文件的内容。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9001005|If the resource not found by path.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
resourceManager.getRawFileContent("test.txt")
```