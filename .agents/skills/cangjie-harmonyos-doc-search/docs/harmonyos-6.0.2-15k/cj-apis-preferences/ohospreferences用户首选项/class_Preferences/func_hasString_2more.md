### func has(String)

```cangjie
public func has(key: String): Bool
```

**功能：** 检查缓存的Preferences实例中是否包含名为给定Key的存储键值对。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要检查的存储key名称。|

**返回值：**

| 类型| 说明|
| :---------------------- | :------------------------------------------------------------ |
| Bool | Bool值。返回Preferences实例是否包含给定key的存储键值对，true表示存在，false表示不存在。 |

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
import ohos.base.*

let preferences = Preferences.getPreferences(Global.getStageContext(), PreferencesOptions("mystore", "myGroupID")) // 需获取Context应用上下文，详见本文使用说明
let hasKey = preferences.has("startup")
if (hasKey) {
    AppLog.info("The key 'startup' is contained.")
} else {
    AppLog.info("The key 'startup' dose not contain.")
}
```

### func off(String, Callback1Argument\<String>)

```cangjie
public func off(tp: String, callback: Callback1Argument<String>): Unit
```

**功能：** 取消订阅数据变更。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tp|String|是|-|事件类型，固定值“change”或“multiProcessChange”。<br>change时，表示取消订阅数据变更。<br>multiProcessChange时，表示取消订阅进程间数据变更。                     |
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<String>|是|-|需要取消的回调函数，不填写则全部取消。String: 发生变化的Key的类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户首选项错误码](../../errorcodes/cj-errorcode-preferences.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息|
  | :-------- | :-------------------------------------- |
  | 401 | Parameter error. Possible causes:<br>1. Mandatory parameters are left unspecified;<br>2. Parameter verification failed.   |
  | 15500000 | Inner error.                   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*
import kit.ArkData.PreferencesValueType as PValueType

// 此处代码可添加在依赖项定义中
// 回调函数
class Callback <: Callback1Argument<String> {
    public func invoke(arg: String): Unit {
        AppLog.info("=========callback========= ${arg.toString()}======================")
    }
}

var str = "container"
var a = Preferences.getPreferences(Global.getStageContext(), str) // 需获取Context应用上下文，详见本文使用说明
var c = Callback()
a.on("change", c)
a.off("change", c)
a.put("kkk1", PValueType.string("vvv1"))
a.flush()
```