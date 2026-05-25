### func clear()

```cangjie
public func clear(): Unit
```

**功能：** 清除缓存的Preferences实例中的所有数据，可通过[flush](#func-flush)将Preferences实例持久化。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

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
    let preferences = Preferences.getPreferences(Global.abilityContext, PreferencesOptions("mystore", dataGroupId:"myGroupID")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    preferences.put("myKey", PreferencesValueType.StringData("myValue"))
    preferences.clear()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func delete(String)

```cangjie
public func delete(key: String): Unit
```

**功能：** 从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](#func-flush)将Preferences实例持久化。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要删除的存储Key名称，不能为空，最大长度限制为[MAX_KEY_LENGTH](#const-max_key_length)。|

**异常：**

- BusinessException：对应错误码如下表，详见[用户首选项错误码](./cj-errorcode-preferences.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15500000 | Inner error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    // 获取 Preferences 实例
    let preferences = Preferences.getPreferences(Global.abilityContext, "myStore") // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    preferences.delete("startup")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func flush()

```cangjie
public func flush(): Unit
```

**功能：** 将缓存的Preferences实例中的数据存储到用户首选项的持久化文件中。

> **说明：**
>
> - 当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。
>
> - 只在XML存储模式下使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

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
    let preferences = Preferences.getPreferences(Global.abilityContext, PreferencesOptions("mystore", dataGroupId:"myGroupID")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    preferences.put("myKey", PreferencesValueType.StringData("myValue"))
    preferences.flush()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```