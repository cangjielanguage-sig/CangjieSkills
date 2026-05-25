### static func off(CallbackType, Callback1Argument\<CountryCode>)

```cangjie
public static func off(`type`: CallbackType, callback: Callback1Argument<CountryCode>): Unit
```

**功能：** 取消订阅国家码变化事件。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CallbackType](#enum-callbacktype)|是|-|设置事件类型。type为CallbackType.countryCodeChange，表示取消订阅国家码信息变化事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[CountryCode](#class-countrycode)>|是|-|需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.off} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.                                           |
  |3301500 | Failed to query the area information.                                       |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.LocationKit.*

// 此处代码可添加在依赖项定义中
class TestCallbackcountryCodeChange <: Callback1Argument<CountryCode> {
    public init() {}
    public open func invoke(res: CountryCode): Unit {
        AppLog.info("Call invoke CountryCodeChange: ${res.country}")
    }
}

let testCallbackcountryCodeChange = TestCallbackcountryCodeChange()
GeoLocationManager.on(CallbackType.CountryCodeChange, testCallbackcountryCodeChange)
GeoLocationManager.off(CallbackType.CountryCodeChange, testCallbackcountryCodeChange)
```