### func put(String, PreferencesValueType)

```cangjie
public func put(key: String, value: PreferencesValueType): Unit
```

**功能：** 将数据写入缓存的Preferences实例中，可通过[flush](#func-flush)将Preferences实例持久化。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要修改的存储的Key，不能为空，最大长度限制为[MAX_KEY_LENGTH](#const-max_key_length)。|
|value|[PreferencesValueType](#enum-preferencesvaluetype)|是|-|存储的新值。支持Int64、Float64、String、Bool、 Array\<Bool>、Array\<Float64>、Array\<String>。|

**异常：**

- BusinessException：对应错误码如下表，详见[用户首选项错误码](./cj-errorcode-preferences.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15500000 | Inner error. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    var preferences = Preferences.getPreferences(Global.abilityContext, PreferencesOptions("mystore", dataGroupId:"myGroupID")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    preferences.put("Monday", PreferencesValueType.StringData("今天天气真好"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```