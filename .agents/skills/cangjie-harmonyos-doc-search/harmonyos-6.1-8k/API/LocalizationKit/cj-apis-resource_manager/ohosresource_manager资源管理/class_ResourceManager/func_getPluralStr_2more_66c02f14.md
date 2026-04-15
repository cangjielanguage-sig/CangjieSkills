### func getPluralStringByName(String, Int64)

```cangjie
public func getPluralStringByName(resName: String, num: Int64): String
```

**功能：** 获取指定资源名称，指定资源数量的单复数字符串。

> **说明**
>
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名称。|
|num|Int64|是|-|数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。|

**返回值：**

|类型|说明|
|:----|:----|
|String|根据指定数量获取指定资源名称表示的单复数字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001003 | Invalid resource name. |
  | 9001004 | No matching resource is found based on the resource name. |
  | 9001006 | The resource is referenced cyclically. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let result = resourceManager.getPluralStringByName("test", 1)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getPluralStringValue(UInt32, Int64)

```cangjie
public func getPluralStringValue(resId: UInt32, num: Int64): String
```

**功能：** 获取指定资源ID，指定资源数量的单复数字符串。

> **说明**
>
> 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|UInt32|是|-|资源ID值。|
|num|Int64|是|-|数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。|

**返回值：**

|类型|说明|
|:----|:----|
|String|根据指定数量获取指定ID字符串表示的单复数字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001001 | Invalid resource ID. |
  | 9001002 | No matching resource is found based on the resource ID. |
  | 9001006 | The resource is referenced cyclically. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.arkui.state_macro_manage.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let res = @r(app.plural.test)
    let result = resourceManager.getPluralStringValue(res.id, 1)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```