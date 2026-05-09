### func get(String, PreferencesValueType)

```cangjie
public func get(key: String, defValue: PreferencesValueType): PreferencesValueType
```

**功能：** 从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要获取的存储Key名称，不能为空，最大长度限制为[MAX_KEY_LENGTH](#const-max_key_length)。|
|defValue|[PreferencesValueType](#enum-preferencesvaluetype)|是|-|默认返回值。支持Int64、Float64、String、Bool、 Array\<Bool>、Array\<Float64>、Array\<String>。|

**返回值：**

|类型|说明|
|:----|:----|
|[PreferencesValueType](#enum-preferencesvaluetype)|返回键对应的值。|

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
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let preferences = Preferences.getPreferences(Global.abilityContext, PreferencesOptions("mystore", dataGroupId:"myGroupID")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    var value = preferences.get("key", PreferencesValueType.Integer(0))
    match (value) {
        case PreferencesValueType.Integer(n) => Hilog.info(0, "AppLogCj", "获取到的值为${n}")
        case _ => Hilog.info(0, "AppLogCj", "获取到的值并不是 Int")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getAll()

```cangjie
public func getAll(): HashMap<String, PreferencesValueType>
```

**功能：** 获取缓存的Preferences实例中的所有键值数据。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|HashMap\<String,[PreferencesValueType](#enum-preferencesvaluetype)>|HashMap对象，返回所有包含的键值数据。|

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
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let preferences = Preferences.getPreferences(Global.abilityContext, PreferencesOptions("mystore", dataGroupId:"myGroupID")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    var values = preferences.getAll()
    for ((k, v) in values) {
        match (v) {
            case Integer(n) => Hilog.info(0, "AppLogCj", "获得到的键值对key: ${k} value: ${n}")
            case Double(n) => Hilog.info(0, "AppLogCj", "获得到的键值对key: ${k} value: ${n}")
            case StringData(n) => Hilog.info(0, "AppLogCj", "获得到的键值对key: ${k} value: ${n}")
            case _ => Hilog.info(0, "AppLogCj", "其他值")
        }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```