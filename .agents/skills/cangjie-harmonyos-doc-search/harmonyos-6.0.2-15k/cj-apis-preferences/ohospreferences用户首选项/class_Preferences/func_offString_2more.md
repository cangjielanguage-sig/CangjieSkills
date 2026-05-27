### func off(String)

```cangjie
public func off(tp: String): Unit
```

**功能：** 取消订阅数据变更。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tp|String|是|-|事件类型，固定值“change”或“multiProcessChange”。<br>change时，表示取消订阅数据变更。<br>multiProcessChange时，表示取消订阅进程间数据变更。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户首选项错误码](../../errorcodes/cj-errorcode-preferences.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                               |
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
a.off("change")
a.put("kkk1", PValueType.string("vvv1"))
a.flush()
```

### func on(String, Callback1Argument\<String>)

```cangjie
public func on(tp: String, callback: Callback1Argument<String>): Unit
```

**功能：** 订阅数据变更。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tp|String|是|-|事件类型，固定值“change”或“multiProcessChange”。<br>change时，表示订阅数据变更，订阅的Key的值发生变更后，在执行flush方法后，触发callback回调。<br>multiProcessChange时，表示订阅进程间数据变更，多个进程持有同一个首选项文件时，订阅的Key的值在任意一个进程发生变更后，执行flush方法后，触发callback回调。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<String>|是|-|回调函数。String: 发生变化的Key的类型。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*
import kit.ArkData.PreferencesValueType as PValueType

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
a.put("kkk1", PValueType.string("vvv1"))
a.flush()
```