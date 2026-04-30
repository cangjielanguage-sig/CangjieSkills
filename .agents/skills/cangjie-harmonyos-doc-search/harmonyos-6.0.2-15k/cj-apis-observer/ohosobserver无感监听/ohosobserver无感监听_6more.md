# ohos.observer（无感监听）

提供UI组件行为变化的无感监听能力。

> **说明：**
>
> ohos.observer仅支持纯仓颉场景，不支持用于ArkTS与仓颉混合开发场景。

## 导入模块

```cangjie
import kit.UIKit.*
```

## func off(ObserverType, Callback1Argument\<ScrollEventInfo>)

```cangjie
public func off(`type`: ObserverType, callback: Callback1Argument<ScrollEventInfo>): Unit
```

**功能：** 取消监听滚动事件的开始和结束。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ObserverType](#enum-observertype)|是|-|监听事件，固定为OBSERVER_SCROLL_EVENT，即滚动事件的开始和结束。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[ScrollEventInfo](#class-scrolleventinfo)>|是|-|回调函数。返回滚动事件的信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error: type is not supported.|

## func off(ObserverType)

```cangjie
public func off(`type`: ObserverType): Unit
```

**功能：** 取消指定监听事件的监听。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ObserverType](#enum-observertype)|是|-|监听事件。|

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error: type is not supported.|

## func off(ObserverType, ObserverOptions, Callback1Argument\<ScrollEventInfo>)

```cangjie
public func off(`type`: ObserverType, options: ObserverOptions, callback: Callback1Argument<ScrollEventInfo>): Unit
```

**功能：** 取消监听滚动事件的开始和结束。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ObserverType](#enum-observertype)|是|-|监听事件，固定为OBSERVER_SCROLL_EVENT，即滚动事件的开始和结束。|
|options|[ObserverOptions](#class-observeroptions)|是|-|指定监听的滚动组件的id。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[ScrollEventInfo](#class-scrolleventinfo)>|是|-|回调函数。返回滚动事件的信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error: type is not supported.|

## func off(ObserverType, ObserverOptions)

```cangjie
public func off(`type`: ObserverType, options: ObserverOptions): Unit
```

**功能：** 取消对指定组件的指定监听事件的监听。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ObserverType](#enum-observertype)|是|-|监听事件。|
|options|[ObserverOptions](#class-observeroptions)|是|-|指定监听的组件的id。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error: type is not supported.|