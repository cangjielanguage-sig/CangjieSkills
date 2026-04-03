### static func on(CallbackType, Callback1Argument\<Bool>)

```cangjie
public static func on(`type`: CallbackType, callback: Callback1Argument<Bool>): Unit
```

**功能：** 订阅位置服务状态变化。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CallbackType](#enum-callbacktype)|是|-|设置事件类型。type为CallbackType.locationEnabledChange，表示位置服务状态。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Bool>|是|-|回调函数。返回true表示位置信息开关已经开启；返回false表示位置信息开关已经关闭。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.on} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.                                           |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.LocationKit.*

// 此处代码可添加在依赖项定义中
class TestCallbackLocationEnabledChange <: Callback1Argument<Bool> {
    public init() {}
    public open func invoke(res: Bool): Unit {
        AppLog.info("Call invoke LocationEnabledChange: ${res}")
    }
}

let testCallbackLocationEnabledChange = TestCallbackLocationEnabledChange()
GeoLocationManager.on(CallbackType.LocationEnabledChange, testCallbackLocationEnabledChange)
```