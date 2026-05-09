### func on(PreferencesEvent, Callback1Argument\<String>)

```cangjie
public func on(event: PreferencesEvent, callback: Callback1Argument<String>): Unit
```

**功能：** 订阅数据变更。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[PreferencesEvent](#enum-preferencesevent)|是|-|事件类型。<br> PreferencesChange 时，表示订阅数据变更，订阅的Key的值发生变更后，在执行flush方法后，触发callback回调。<br> PreferencesMultiProcessChange 时，表示订阅进程间数据变更，多个进程持有同一个首选项文件时，订阅的Key的值在任意一个进程发生变更后，执行flush方法后，触发callback回调。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<String>|是|-|回调函数。<br>String: 发生变化的Key的类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[用户首选项错误码](./cj-errorcode-preferences.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15500000 | Inner error. |
  | 15500019 | Failed to obtain the subscription service. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.callback_invoke.*
import ohos.business_exception.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

// 回调函数
class Callback1 <: Callback1Argument<String> {
    public func invoke(err: ?BusinessException, arg: String): Unit {
        Hilog.info(0, "AppLogCj", "=========callback========= ${arg.toString()}======================")
    }
}

try {
    var str = "container"
    var a = Preferences.getPreferences(Global.abilityContext, str) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    var c = Callback1()
    a.on(PreferencesEvent.PreferencesChange, c)
    a.put("kkk1", PreferencesValueType.StringData("vvv1"))
    a.flush()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```