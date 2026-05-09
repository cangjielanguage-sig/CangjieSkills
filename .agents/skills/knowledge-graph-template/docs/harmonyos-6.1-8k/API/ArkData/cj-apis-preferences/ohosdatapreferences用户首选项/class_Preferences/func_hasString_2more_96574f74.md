### func has(String)

```cangjie
public func has(key: String): Bool
```

**功能：** 检查缓存的Preferences实例中是否包含名为给定Key的存储键值对。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要检查的存储key名称，不能为空，最大长度限制为[MAX_KEY_LENGTH](#const-max_key_length)。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|Bool值。返回Preferences实例是否包含给定key的存储键值对，true表示存在，false表示不存在。|

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
    let hasKey = preferences.has("startup")
    if (hasKey) {
        Hilog.info(0, "AppLogCj", "The key 'startup' is contained.")
    } else {
        Hilog.info(0, "AppLogCj", "The key 'startup' dose not contain.")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func off(PreferencesEvent, ?Callback1Argument\<String>)

```cangjie
public func off(event: PreferencesEvent, callback!: ?Callback1Argument<String> = None): Unit
```

**功能：** 取消订阅数据变更/取消订阅进程间数据变更。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[PreferencesEvent](#enum-preferencesevent)|是|-|事件类型，表示取消订阅数据变更，或表示取消订阅进程间数据变更。|
|callback|?[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<String>|否|None|**命名参数。** 需要取消的回调函数，不填写则全部取消。<br> String: 发生变化的Key的类型。|

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
import ohos.callback_invoke.*
import ohos.business_exception.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

// 此处代码可添加在依赖项定义中
// 回调函数
class Callback <: Callback1Argument<String> {
    public func invoke(err: ?BusinessException, arg: String): Unit {
        Hilog.info(0, "AppLogCj", "=========callback========= ${arg.toString()}======================")
    }
}

try {
    var str = "container"
    var a = Preferences.getPreferences(Global.abilityContext, str) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    var c = Callback()
    a.on(PreferencesEvent.PreferencesChange, c)
    a.off(PreferencesEvent.PreferencesChange)
    a.put("kkk1", PreferencesValueType.StringData("vvv1"))
    a.flush()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```