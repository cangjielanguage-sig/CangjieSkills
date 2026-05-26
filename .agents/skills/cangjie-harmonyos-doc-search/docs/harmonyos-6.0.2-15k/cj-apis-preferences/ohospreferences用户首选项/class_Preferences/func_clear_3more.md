### func clear()

```cangjie
public func clear(): Unit
```

**功能：** 清除缓存的Preferences实例中的所有数据，可通过[flush](#func-flush)将Preferences实例持久化。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户首选项错误码](../../errorcodes/cj-errorcode-preferences.md)。

  | 错误码ID | 错误信息                       |
  | :-------- | :------------------------------|
  | 15500000 | Inner error.                   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let preferences = Preferences.getPreferences(Global.getStageContext(), PreferencesOptions("mystore", "myGroupID")) // 需获取Context应用上下文，详见本文使用说明
preferences.put("myKey", PreferencesValueType.string("myValue"))
preferences.clear()
```

### func delete(String)

```cangjie
public func delete(key: String): Unit
```

**功能：** 从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](#func-flush)将Preferences实例持久化。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要删除的存储Key名称，不能为空。|

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

// 获取 Preferences 实例
let preferences = Preferences.getPreferences(Global.getStageContext(), "myStore") // 需获取Context应用上下文，详见本文使用说明
preferences.delete("startup")
```

### func flush()

```cangjie
public func flush(): Unit
```

**功能：** 将缓存的Preferences实例中的数据存储到用户首选项的持久化文件中。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户首选项错误码](../../errorcodes/cj-errorcode-preferences.md)。

  | 错误码ID | 错误信息                       |
  | :-------- | :------------------------------|
  | 15500000 | Inner error.                   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

let preferences = Preferences.getPreferences(Global.getStageContext(), PreferencesOptions("mystore", "myGroupID")) // 需获取Context应用上下文，详见本文使用说明
preferences.put("myKey", PreferencesValueType.string("myValue"))
preferences.flush()
```