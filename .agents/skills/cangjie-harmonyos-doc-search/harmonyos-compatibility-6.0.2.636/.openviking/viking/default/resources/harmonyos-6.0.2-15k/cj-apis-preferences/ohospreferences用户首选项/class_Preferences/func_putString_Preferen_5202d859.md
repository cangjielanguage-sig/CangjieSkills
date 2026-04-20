### func put(String, PreferencesValueType)

```cangjie
public func put(key: String, value: PreferencesValueType): Unit
```

**功能：** 将数据写入缓存的Preferences实例中，可通过[flush](#func-flush)将Preferences实例持久化。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要修改的存储的Key，不能为空。|
|value|[PreferencesValueType](#enum-preferencesvaluetype)|是|-|存储的新值。支持Int64、Float64、String、Bool、 Array\<Bool>、Array\<Float64>、Array\<String>。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户首选项错误码](../../errorcodes/cj-errorcode-preferences.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息|
  | :-------- | :------------------------------|
  | 401 | Parameter error. Possible causes:<br>1. Mandatory parameters are left unspecified;<br>2. Parameter verification failed.   |
  | 15500000 | Inner error.                   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

var preferences = Preferences.getPreferences(Global.getStageContext(), PreferencesOptions("mystore", "myGroupID")) // 需获取Context应用上下文，详见本文使用说明
preferences.put("Monday", PreferencesValueType.string("今天天气真好"))
```