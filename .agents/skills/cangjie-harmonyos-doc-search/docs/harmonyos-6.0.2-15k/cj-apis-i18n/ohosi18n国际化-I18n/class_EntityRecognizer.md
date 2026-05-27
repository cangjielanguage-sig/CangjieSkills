## class EntityRecognizer

```cangjie
public class EntityRecognizer {
    public init(locale!: ?String = None)
}
```

**功能：** 实体识别对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### init(?String)

```cangjie
public init(locale!: ?String = None)
```

**功能：** 创建实体识别对象的示例。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|?String|否|None| **命名参数。** 表示区域信息的字符串，由语言、脚本、国家或地区组成，例如zh-Hans-CN。None代表系统当前locale。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[I18n错误码](../../errorcodes/cj-errorcode-i18n.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|
  |890001|Invalid parameter. Possible causes: Parameter verification failed.|

### func findEntityInfo(String)

```cangjie
public func findEntityInfo(text: String): Array<EntityInfoItem>
```

**功能：** 识别文本中的实体信息。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要被识别的文本。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[EntityInfoItem](#class-entityinfoitem)>|文本中的实体信息列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let entity = EntityRecognizer(locale: "zh-CN")
let text1 = "如有疑问，请联系158****2312"
let result1 = entity.findEntityInfo(text1) // result1[0].type = "phone_number", result1[0].begin = 8, result1[0].end = 19
let text2 = "我们2023年12月1日一起吃饭吧。"
let result2 = entity.findEntityInfo(text2) // result2[0].type = "date", result2[0].begin = 2, result2[0].end = 12
```