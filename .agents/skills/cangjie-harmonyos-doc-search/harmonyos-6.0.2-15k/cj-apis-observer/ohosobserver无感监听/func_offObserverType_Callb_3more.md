## func off(ObserverType, Callback1Argument\<TabContentInfo>)

```cangjie
public func off(`type`: ObserverType, callback: Callback1Argument<TabContentInfo>): Unit
```

**功能：** 取消监听TabContent页面的切换事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ObserverType](#enum-observertype)|是|-|监听事件，固定为OBSERVER_TAB_CONTENT_UPDATE，即TabContent页面的切换事件。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[TabContentInfo](#class-tabcontentinfo)>|是|-|需要被注销的回调函数。该回调函数的参数TabContentInfo用于返回TabContent页面切换事件的信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error: type is not supported.|

## func off(ObserverType, ObserverOptions, Callback1Argument\<TabContentInfo>)

```cangjie
public func off(`type`: ObserverType, options: ObserverOptions, callback: Callback1Argument<TabContentInfo>): Unit
```

**功能：** 取消对指定Tabs组件的TabContent页面的切换事件的监听。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ObserverType](#enum-observertype)|是|-|监听事件，固定为OBSERVER_TAB_CONTENT_UPDATE，即TabContent页面的切换事件。|
|options|[ObserverOptions](#class-observeroptions)|是|-|指定监听的Tabs组件的id。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[TabContentInfo](#class-tabcontentinfo)>|是|-|需要被注销的回调函数。该回调函数的参数TabContentInfo用于返回TabContent页面切换事件的信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error: type is not supported.|

## func on(ObserverType, Callback1Argument\<ScrollEventInfo>)

```cangjie
public func on(`type`: ObserverType, callback: Callback1Argument<ScrollEventInfo>): Unit
```

**功能：** 监听滚动事件的开始和结束。

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