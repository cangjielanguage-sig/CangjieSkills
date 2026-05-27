### func off(WindowCallbackType)

```cangjie
public func off(callbackType: WindowCallbackType): Unit
```

**功能：** 关闭窗口对应事件的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|要关闭的监听事件。需要在 [WindowCallbackType](#enum-windowcallbacktype) 枚举范围内。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|
  |801|Capability not supported. Failed to call the API due to limited device capabilities.|
  |1300002|This window state is abnormal.|
  |1300003|This window manager service works abnormally.|

### func on(String, Callback1Argument\<UInt32>)

```cangjie
public func on(callbackType: String, callback: Callback1Argument<UInt32>): Unit
```

**功能：** 开启固定态软键盘高度变化的监听，当软键盘由本窗口唤出并存在重叠区域时通知键盘高度变化。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|String|是|-|监听事件，固定为WindowCallbackType.KeyboardHeightChange，即键盘高度变化事件。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<UInt32>|是|-|回调函数。返回当前的键盘高度，单位为px。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] Register callbackType failed: This window state is abnormal.|

### func on(WindowCallbackType, Callback1Argument\<Size>)

```cangjie
public func on(callbackType: WindowCallbackType, callback: Callback1Argument<Size>): Unit
```

**功能：** 开启窗口尺寸变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|监听事件类型，固定为WindowCallbackType.WindowSizeChange，即窗口尺寸变化事件。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[Size](cj-apis-measure.md#struct-size)>|是|-|回调函数。返回当前的窗口尺寸。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] Unregister callbackType failed: This window state is abnormal.|