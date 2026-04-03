### func getStringArrayValue(UInt32)

```cangjie
public func getStringArrayValue(resId: UInt32): Array<String>
```

**功能：** 获取指定资源ID对应的字符串数组。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|UInt32|是|-|资源ID值。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|资源ID值对应的字符串数组。|

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
    let res = @r(app.strarray.test)
    let result = resourceManager.getStringArrayValue(res.id)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getStringByName(String, Array\<ArgsValueType>)

```cangjie
public func getStringByName(resName: String, args: Array<ArgsValueType>): String
```

**功能：** 获取指定资源名称对应的字符串，并根据args参数对字符串进行格式化。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名称。|
|args|Array\<[ArgsValueType](#enum-argsvaluetype)>|是|-|格式化字符串资源参数。<br>支持参数类型：`%d`、`%f`、`%s`、`%%`、`%数字$d`、`%数字$f`、`%数字$s`。<br>说明：`%%`转义为`%`; `%数字$d`中的数字表示使用args中的第几个参数。<br>举例：`%%d`格式化后为`%d`字符串; `%1$d`表示使用第一个参数。|

**返回值：**

|类型|说明|
|:----|:----|
|String|资源名对应的格式化字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001003 | Invalid resource name. |
  | 9001004 | No matching resource is found based on the resource name. |
  | 9001006 | The resource is referenced cyclically. |
  | 9001008 | Failed to format the resource obtained based on the resource Name. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let result = resourceManager.getStringByName("test", ArgsValueType.StringValue("format string"), ArgsValueType.Int32Value(10), ArgsValueType.Float32Value(98.78))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```