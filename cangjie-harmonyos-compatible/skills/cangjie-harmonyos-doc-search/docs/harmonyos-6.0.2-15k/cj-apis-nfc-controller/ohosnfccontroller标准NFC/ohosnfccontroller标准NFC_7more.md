# ohos.nfc.controller（标准NFC）

本模块主要用于管理NFC状态，包括打开和关闭NFC，读取NFC的状态等。

## 导入模块

```cangjie
import kit.ConnectivityKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func isNfcOpen()

```cangjie
public func isNfcOpen(): Bool
```

**功能：** 查询NFC是否打开。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Bool|NFC是否打开。true: NFC是打开的；false: NFC是关闭的。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let isOpen = isNfcOpen()
AppLog.info("isNfcOpen：${isOpen}")
```

## func getNfcState()

```cangjie
public func getNfcState(): NfcState
```

**功能：** 查询NFC状态。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[NfcState](#enum-nfcstate)|NFC状态值，详细请见[NfcState](#enum-nfcstate)枚举值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let nfcState = getNfcState()
AppLog.info("nfcState：${nfcState}")
```

## func on(NfcControllerCallbackType, Callback1Argument\<NfcState>)

```cangjie
public func on(`type`: NfcControllerCallbackType, callback: Callback1Argument<NfcState>): Unit
```

**功能：** 注册NFC开关状态事件，通过Callback方式获取NFC状态的变化通知。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[NfcControllerCallbackType](#enum-nfccontrollercallbacktype)|是|要订阅的回调类型，固定填NfcStateChange。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<NfcState>|是|NFC状态改变通知的回调函数。|

**示例：**

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

class StateChangeCallback <: Callback1Argument<NfcState> {
    public func invoke(state: NfcState): Unit {
        AppLog.error("StateChangeCallback: ${toString(getNfcState())}")
    }
}

let cb = StateChangeCallback()
on(NfcControllerCallbackType.NfcStateChange, cb)
```

## func off(NfcControllerCallbackType, CallbackObject)

```cangjie
public func off(`type`: NfcControllerCallbackType, callback: CallbackObject): Unit
```

**功能：** 取消NFC开关状态事件的注册，取消后NFC状态变化时，就不会再收到Callback的通知。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[NfcControllerCallbackType](#enum-nfccontrollercallbacktype)|是|要订阅的回调类型，固定填NfcStateChange。|
|callback|[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|是|NFC状态改变通知的回调函数。|

**示例：**

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

class StateChangeCallback <: Callback1Argument<NfcState> {
    public func invoke(state: NfcState): Unit {
        AppLog.error("StateChangeCallback: ${toString(getNfcState())}")
    }
}

let cb = StateChangeCallback()
on(NfcControllerCallbackType.NfcStateChange, cb)
off(NfcControllerCallbackType.NfcStateChange, cb)
```