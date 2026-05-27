### func get(String, PreferencesValueType)

```cangjie
public func get(key: String, defValue: PreferencesValueType): PreferencesValueType
```

**功能：** 从缓存的Preferences实例中获取键对应的值，如果该键不存在，返回默认数据defValue。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要获取的存储Key名称。|
|defValue|[PreferencesValueType](#enum-preferencesvaluetype)|是|-|默认返回值。支持Int64、Float64、String、Bool、 Array\<Bool>、Array\<Float64>、Array\<String>。|

**返回值：**

|类型|说明|
|:----|:----|
|[PreferencesValueType](#enum-preferencesvaluetype)|返回键对应的值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户首选项错误码](../../errorcodes/cj-errorcode-preferences.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                       |
  | :-------- | :------------------------------|
  | 401 | Parameter error. Possible causes:<br>1. Mandatory parameters are left unspecified;<br>2. Parameter verification failed.   |
  | 15500000 | Inner error.                   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

let preferences = Preferences.getPreferences(Global.getStageContext(), PreferencesOptions("mystore", "myGroupID")) // 需获取Context应用上下文，详见本文使用说明
var value = preferences.get("key", PreferencesValueType.integer(0))
match (value) {
    case PreferencesValueType.integer(n) => AppLog.info("获取到的值为${n}")
    case _ => AppLog.info("获取到的值并不是 Int")
}
```

### func getAll()

```cangjie
public func getAll(): HashMap<String, PreferencesValueType>
```

**功能：** 从缓存的Preferences实例中获取所有键值数据。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|HashMap\<String, [PreferencesValueType](#enum-preferencesvaluetype)>|HashMap对象，返回含有所有键值数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户首选项错误码](../../errorcodes/cj-errorcode-preferences.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                       |
  | :-------- | :------------------------------|
  | 401 | Parameter error. Possible causes:<br>1. Mandatory parameters are left unspecified;<br>2. Parameter verification failed.   |
  | 15500000 | Inner error.                   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

let preferences = Preferences.getPreferences(Global.getStageContext(), PreferencesOptions("mystore", "myGroupID")) // 需获取Context应用上下文，详见本文使用说明
var values = preferences.getAll()
for ((k, v) in values) {
    match (v) {
        case integer(n) => AppLog.info("获得到的键值对key: ${k} value: ${n}")
        case double(n) => AppLog.info("获得到的键值对key: ${k} value: ${n}")
        case string(n) => AppLog.info("获得到的键值对key: ${k} value: ${n}")
        case _ => AppLog.info("其他值")
    }
}
```