## func off(WifiCallbackType, ?CallbackObject)

```cangjie
public func off(eventType: WifiCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消注册WLAN状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[WifiCallbackType](#enum-wificallbacktype)|是|-|回调事件。|
|callback|?[CallbackObject](../arkinterop/cj-api-callback_invoke.md#class-callbackobject)|否|None| **命名参数。** 状态改变回调函数。如果callback没有传入参数，将取消注册该事件关联的所有回调函数。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[WIFI错误码](./cj-errorcode-wifi-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2801000 | Operation failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*
import kit.PerformanceAnalysisKit.Hilog

class WifiCallback <: Callback1Argument<Int32> {
    public func invoke(err: ?BusinessException, arg: Int32) {
        Hilog.info(0, "test", "invoke success", "")
    }
}

try {
    let callback = WifiCallback()
    // Register event
    on(WifiScanStateChange, callback)
    // Unregister event
    off(WifiScanStateChange, callback: callback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func on(WifiCallbackType, Callback1Argument\<Int32>)

```cangjie
public func on(eventType: WifiCallbackType, callback: Callback1Argument<Int32>): Unit
```

**功能：** 注册WLAN状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[WifiCallbackType](#enum-wificallbacktype)|是|-|回调事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<Int32>|是|-|状态改变回调函数。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[WIFI错误码](./cj-errorcode-wifi-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2801000 | Operation failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*
import kit.PerformanceAnalysisKit.Hilog

class WifiCallback1 <: Callback1Argument<Int32> {
    public func invoke(err: ?BusinessException, arg: Int32) {
        Hilog.info(0, "test", "invoke success", "")
    }
}

try {
    let callback = WifiCallback1()
    // Register event
    on(WifiScanStateChange, callback)
    // Unregister event
    off(WifiScanStateChange, callback: callback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```